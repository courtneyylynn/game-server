from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

_PACIFIC_STD = timezone(timedelta(hours=-8))
_PACIFIC_DST = timezone(timedelta(hours=-7))


def _nth_weekday_of_month(year: int, month: int, weekday: int, n: int) -> date:
    first = date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return first + timedelta(days=offset + 7 * (n - 1))


def _us_dst_start_local(year: int) -> datetime:
    return datetime(
        year,
        3,
        _nth_weekday_of_month(year, 3, 6, 2).day,
        2,
        0,
        tzinfo=_PACIFIC_STD,
    )


def _us_dst_end_local(year: int) -> datetime:
    return datetime(
        year,
        11,
        _nth_weekday_of_month(year, 11, 6, 1).day,
        2,
        0,
        tzinfo=_PACIFIC_DST,
    )


def _pacific_tz_at(when: datetime) -> timezone:
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    utc = when.astimezone(timezone.utc)
    dst_start = _us_dst_start_local(utc.year).astimezone(timezone.utc)
    dst_end = _us_dst_end_local(utc.year).astimezone(timezone.utc)
    if dst_start <= utc < dst_end:
        return _PACIFIC_DST
    return _PACIFIC_STD


def _to_pacific_local(when: datetime) -> datetime:
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return when.astimezone(_pacific_tz_at(when))


def current_spin_day(now: datetime | None = None) -> int:
    if now is None:
        now = datetime.now(timezone.utc)
    local = _to_pacific_local(now)
    return local.year * 10000 + local.month * 100 + local.day


def can_spin_today(last_spin_day: int, now: datetime | None = None) -> bool:
    if last_spin_day <= 0:
        return True
    return last_spin_day < current_spin_day(now)


def played_flag_for_client(last_spin_day: int, now: datetime | None = None) -> int:
    return 0 if can_spin_today(last_spin_day, now) else 1
