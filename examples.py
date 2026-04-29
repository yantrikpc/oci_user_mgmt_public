from __future__ import annotations

from .models import AuditReport


EXAMPLE_REPORT: AuditReport = {
    "query": "user@example.com",
    "domains_checked": [
        {
            "id": "domain-id",
            "display_name": "Default",
            "description": "Example domain",
            "url": "https://example.identity.oraclecloud.com",
        }
    ],
    "matches": [
        {
            "domain": {
                "id": "domain-id",
                "display_name": "Default",
            },
            "user": {
                "id": "user-id",
                "user_name": "user@example.com",
                "display_name": "Example User",
                "emails": ["user@example.com"],
                "active": True,
            },
            "groups": [
                {
                    "id": "group-id",
                    "display_name": "ExampleGroup",
                    "password_policies": [
                        {
                            "id": "policy-id",
                            "name": "defaultPasswordPolicy",
                            "priority": None,
                        }
                    ],
                }
            ],
            "user_security": {
                "locked_status": None,
                "password_expired": None,
            },
        }
    ],
    "summary": {
        "domain_count": 1,
        "match_count": 1,
    },
}
