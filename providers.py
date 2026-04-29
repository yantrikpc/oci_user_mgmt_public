from __future__ import annotations

from typing import Any, Protocol


class IdentityProvider(Protocol):
    """Abstract provider interface for directory and policy lookups."""

    def search_user(self, user_name: str) -> list[dict[str, Any]]:
        """Return matching users."""

    def list_user_groups(self, user_id: str) -> list[dict[str, Any]]:
        """Return groups for a user."""

    def list_group_policies(self, group_ids: list[str]) -> dict[str, list[dict[str, Any]]]:
        """Return password policies keyed by group id."""
