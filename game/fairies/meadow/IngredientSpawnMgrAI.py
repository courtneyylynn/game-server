"""
Runtime ingredient spawner — creates and manages DistributedSpawnStackAI objects.

Reads configuration from IngredientSpawnData.build_active_spawn_pools() and creates
one SpawnPool per active (zone_id, item_id) pair. Each pool:
  - spawns max_stacks items at random positions within the zone's map bounds
  - respawns one item at a new random position after collection (rarity timing)
  - rejects spawn points inside ZONE_EXCLUSIONS (when populated)
  - keeps MIN_DISTANCE between stacks in the same pool

Started once by FairiesAIRepository.createObjects().
"""
import random

from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.meadow.DistributedSpawnStackAI import DistributedSpawnStackAI
from game.fairies.meadow.IngredientSpawnData import ActiveSpawnPool, build_active_spawn_pools

MIN_DISTANCE = 400
MAX_POSITION_ATTEMPTS = 50
COLLECT_DELETE_DELAY_SEC = 1.5


class SpawnPool:
    notify = DirectNotifyGlobal.directNotify.newCategory("SpawnPool")

    def __init__(self, air, mgr: "IngredientSpawnMgrAI", config: ActiveSpawnPool) -> None:
        self.air = air
        self.mgr = mgr
        self.config = config
        self.activeStacks: set[DistributedSpawnStackAI] = set()

    def start(self) -> None:
        for _ in range(self.config.max_stacks):
            self.spawn()

        self.notify.info(
            "Started %s spawning with %d stacks in zone %d (rarity=%s)"
            % (
                self.config.display_name,
                len(self.activeStacks),
                self.config.zone_id,
                self.config.rarity.name.lower(),
            )
        )

    def onCollected(self, stack: DistributedSpawnStackAI) -> None:
        if stack not in self.activeStacks:
            return

        self.activeStacks.discard(stack)
        stack.spawnMgr = None

        taskSerial = self.mgr.nextTaskSerial()
        deleteTaskName = "ingredient-delete-%d" % taskSerial
        taskMgr.doMethodLater(
            COLLECT_DELETE_DELAY_SEC,
            self._deleteStackTask,
            deleteTaskName,
            extraArgs=[stack],
        )

        delay = random.uniform(self.config.respawn_min_sec, self.config.respawn_max_sec)
        taskSerial = self.mgr.nextTaskSerial()
        taskName = "ingredient-respawn-%d-%d-%d" % (taskSerial, self.config.zone_id, self.config.item_id)
        taskMgr.doMethodLater(delay, self._respawnTask, taskName)

        print(
            "%s collected in zone %d; respawning in %.1fs (%d active)"
            % (self.config.display_name, self.config.zone_id, delay, len(self.activeStacks))
        )

    def spawn(self) -> DistributedSpawnStackAI | None:
        if len(self.activeStacks) >= self.config.max_stacks:
            return None

        pos = self._randomPosition()
        if pos is None:
            self.notify.warning(
                "Could not find valid spawn point for %s in zone %d after %d attempts"
                % (self.config.display_name, self.config.zone_id, MAX_POSITION_ATTEMPTS)
            )
            return None

        x, y = pos
        stack = DistributedSpawnStackAI(self.air)
        stack.spawnMgr = self
        stack.setItemID(self.config.item_id)
        stack.setName(self.config.display_name)
        stack.setPosition(x, y)
        stack.setColorIDs([])
        stack.setItemCount(1)
        stack.setServingSize(1)
        stack.generateWithRequired(self.config.zone_id)

        self.activeStacks.add(stack)
        return stack

    def _randomPosition(self) -> tuple[int, int] | None:
        bounds = self.config.bounds

        for _ in range(MAX_POSITION_ATTEMPTS):
            x = random.randint(bounds.x_min, bounds.x_max)
            y = random.randint(bounds.y_min, bounds.y_max)

            if self._isValidSpawnPoint(x, y):
                return x, y

        return None

    def _isValidSpawnPoint(self, x: int, y: int) -> bool:
        if not self._isFarEnough(x, y):
            return False

        for exclusion in self.config.exclusions:
            if (
                exclusion.x_min <= x <= exclusion.x_max
                and exclusion.y_min <= y <= exclusion.y_max
            ):
                return False

        return True

    def _isFarEnough(self, x: int, y: int) -> bool:
        minDistSq = MIN_DISTANCE * MIN_DISTANCE

        for stack in self.activeStacks:
            sx, sy = stack.getPosition()
            dx, dy = x - sx, y - sy

            if dx * dx + dy * dy < minDistSq:
                return False

        return True

    def _deleteStackTask(self, stack: DistributedSpawnStackAI) -> int:
        stack.requestDelete()
        return Task.done

    def _respawnTask(self, task: Task) -> int:
        self.spawn()
        return Task.done


class IngredientSpawnMgrAI:
    notify = DirectNotifyGlobal.directNotify.newCategory("IngredientSpawnMgrAI")

    def __init__(self, air) -> None:
        self.air = air
        self.pools: list[SpawnPool] = []
        self._taskSerial = 0

    def start(self) -> None:
        for poolConfig in build_active_spawn_pools():
            pool = SpawnPool(self.air, self, poolConfig)
            pool.start()
            self.pools.append(pool)

        self.notify.info("Started %d ingredient spawn pools" % len(self.pools))

    def nextTaskSerial(self) -> int:
        self._taskSerial += 1
        return self._taskSerial
