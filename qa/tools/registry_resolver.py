"""Load ui_path_registry.json next to this file (qa/tools)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _default_registry_path() -> Path:
    return Path(__file__).resolve().parent / "ui_path_registry.json"


class RegistryResolver:
    def __init__(self, registry_path: Path | None = None):
        self.path = registry_path or _default_registry_path()
        self._alias_to_ref: dict[str, str] = {}
        self._data: dict[str, Any] = {}
        if self.path.is_file():
            self._data = json.loads(self.path.read_text(encoding="utf-8"))
            for row in self._data.get("paths") or []:
                if isinstance(row, dict) and "alias" in row and "ref" in row:
                    self._alias_to_ref[str(row["alias"])] = str(row["ref"])

    def ref(self, alias: str) -> str | None:
        return self._alias_to_ref.get(alias)

    def require_ref(self, alias: str) -> str:
        r = self.ref(alias)
        if not r:
            raise KeyError(
                f"ui_path_registry: unknown alias {alias!r} (registry={self.path}); "
                f"ItemNotFound risk — add entry or fix alias"
            )
        return r

    def all_aliases(self) -> frozenset[str]:
        return frozenset(self._alias_to_ref.keys())


def resolve_path(alias: str, registry_path: Path | None = None) -> str:
    return RegistryResolver(registry_path).require_ref(alias)
