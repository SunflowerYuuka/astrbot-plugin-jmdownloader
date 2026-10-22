from collections.abc import Iterable
from typing import Any


def normalize_group_ids(values: Any) -> set[str]:
    """Normalize configured group IDs and ignore empty or invalid entries."""
    if isinstance(values, str):
        values = values.replace(",", "\n").splitlines()
    if not isinstance(values, Iterable):
        return set()

    group_ids: set[str] = set()
    for value in values:
        normalized = str(value).strip()
        if normalized.isdigit():
            group_ids.add(normalized)
    return group_ids


def group_access_allowed(
    mode: str,
    group_id: str,
    whitelist: Any,
    blacklist: Any,
) -> bool:
    """Check whether a group may use the download command."""
    normalized_mode = str(mode or "disabled").strip().lower()
    normalized_group_id = str(group_id).strip()
    if normalized_mode == "whitelist":
        return normalized_group_id in normalize_group_ids(whitelist)
    if normalized_mode == "blacklist":
        return normalized_group_id not in normalize_group_ids(blacklist)
    return True
