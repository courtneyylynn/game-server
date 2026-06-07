"""
Runtime ingredient spawner — creates and manages DistributedSpawnStackAI objects.

Reads configuration from IngredientSpawnData.build_active_spawn_pools() and creates
one SpawnPool per active (zone_id, item_id) pair. Each pool:
  - spawns max_stacks items at random positions within the zone's map bounds
  - respawns one item at a new random position after collection (rarity timing)
  - rejects spawn points inside ZONE_EXCLUSIONS (when populated)
  - keeps MIN_DISTANCE between all stacks in the same zone (cross-pool)

Started once by FairiesAIRepository.createObjects().
"""
import random

from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.meadow.DistributedSpawnStackAI import DistributedSpawnStackAI
from game.fairies.meadow.IngredientSpawnData import ActiveSpawnPool, SpawnExclusionZone, build_active_spawn_pools

MIN_DISTANCE = 100
MAX_POSITION_ATTEMPTS = 100
FALLBACK_CANDIDATE_ATTEMPTS = 30
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
        self.mgr.unregisterStack(self.config.zone_id, stack)
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

        self.notify.debug(
            "%s collected in zone %d; respawning in %.1fs (%d active)"
            % (self.config.display_name, self.config.zone_id, delay, len(self.activeStacks))
        )

    def spawn(self) -> DistributedSpawnStackAI | None:
        if len(self.activeStacks) >= self.config.max_stacks:
            return None

        position = self._randomPosition()
        if position is None:
            self.notify.warning(
                "Failed to find valid spawn point for %s in zone %d"
                % (self.config.display_name, self.config.zone_id)
            )
            return None

        x, y = position
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
        self.mgr.registerStack(self.config.zone_id, stack)
        return stack

    def _randomPosition(self) -> tuple[int, int] | None:
        bounds = self.config.bounds
        exclusions = self.config.exclusions
        zone_id = self.config.zone_id

        for _ in range(MAX_POSITION_ATTEMPTS):
            x = random.randint(bounds.x_min, bounds.x_max)
            y = random.randint(bounds.y_min, bounds.y_max)

            if self.mgr.isValidSpawnPoint(zone_id, x, y, exclusions):
                return x, y

        best: tuple[int, int] | None = None
        bestDistSq = -1.0

        for _ in range(FALLBACK_CANDIDATE_ATTEMPTS):
            x = random.randint(bounds.x_min, bounds.x_max)
            y = random.randint(bounds.y_min, bounds.y_max)

            if not self.mgr.isPointOutsideExclusions(x, y, exclusions):
                continue

            nearestDistSq = self.mgr.nearestStackDistanceSq(zone_id, x, y)
            if nearestDistSq > bestDistSq:
                bestDistSq = nearestDistSq
                best = (x, y)

        if best is not None and bestDistSq >= MIN_DISTANCE * MIN_DISTANCE:
            return best

        return best

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
        self._zoneStacks: dict[int, set[DistributedSpawnStackAI]] = {}

    def registerStack(self, zone_id: int, stack: DistributedSpawnStackAI) -> None:
        self._zoneStacks.setdefault(zone_id, set()).add(stack)

    def unregisterStack(self, zone_id: int, stack: DistributedSpawnStackAI) -> None:
        stacks = self._zoneStacks.get(zone_id)
        if stacks is not None:
            stacks.discard(stack)

    def isPointOutsideExclusions(
        self, x: int, y: int, exclusions: tuple[SpawnExclusionZone, ...]
    ) -> bool:
        for exclusion in exclusions:
            if (
                exclusion.x_min <= x <= exclusion.x_max
                and exclusion.y_min <= y <= exclusion.y_max
            ):
                return False

        return True

    def nearestStackDistanceSq(self, zone_id: int, x: int, y: int) -> float:
        minDistSq = float("inf")

        for stack in self._zoneStacks.get(zone_id, ()):
            sx, sy = stack.getPosition()
            dx, dy = x - sx, y - sy
            distSq = dx * dx + dy * dy

            if distSq < minDistSq:
                minDistSq = distSq

        return minDistSq

    def isValidSpawnPoint(
        self,
        zone_id: int,
        x: int,
        y: int,
        exclusions: tuple[SpawnExclusionZone, ...],
        ignore_stack: DistributedSpawnStackAI | None = None,
    ) -> bool:
        if not self.isPointOutsideExclusions(x, y, exclusions):
            return False

        minDistSq = MIN_DISTANCE * MIN_DISTANCE

        for stack in self._zoneStacks.get(zone_id, ()):
            if stack is ignore_stack:
                continue

            sx, sy = stack.getPosition()
            dx, dy = x - sx, y - sy

            if dx * dx + dy * dy < minDistSq:
                return False

        return True

    def start(self) -> None:
        poolConfigs = sorted(build_active_spawn_pools(), key=lambda config: config.zone_id)

        for poolConfig in poolConfigs:
            pool = SpawnPool(self.air, self, poolConfig)
            pool.start()
            self.pools.append(pool)

        self.notify.info("Started %d ingredient spawn pools" % len(self.pools))

    def nextTaskSerial(self) -> int:
        self._taskSerial += 1
        return self._taskSerial
