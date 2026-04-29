from __future__ import annotations

from typing import Any, TypedDict


class GroupPolicy(TypedDict, total=False):
    id: str | None
    name: str | None
    description: str | None
    priority: int | None
    password_expires_after: int | None
    min_length: int | None
    max_length: int | None
    min_lower_case: int | None
    min_upper_case: int | None
    min_numerals: int | None
    max_incorrect_attempts: int | None
    lockout_duration: int | None
    password_strength: str | None


class UserGroup(TypedDict, total=False):
    id: str | None
    display_name: str | None
    description: str | None
    policies: list[dict[str, Any]]
    password_policies: list[GroupPolicy]


class UserSummary(TypedDict, total=False):
    id: str | None
    user_name: str | None
    display_name: str | None
    emails: list[str]
    active: bool | None
    creation_date: str | None


class DomainSummary(TypedDict, total=False):
    id: str | None
    display_name: str | None
    description: str | None
    url: str | None


class UserSecurity(TypedDict, total=False):
    locked_status: Any
    password_expired: Any
    password_expiry_date: Any
    last_password_reset_time: Any
    raw_fields: dict[str, Any]


class AuditMatch(TypedDict, total=False):
    domain: DomainSummary
    user: UserSummary
    groups: list[UserGroup]
    user_security: UserSecurity


class AuditReport(TypedDict, total=False):
    query: str
    domains_checked: list[DomainSummary]
    matches: list[AuditMatch]
    summary: dict[str, int]
