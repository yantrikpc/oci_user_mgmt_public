# `user_mgmt` Minimal Public Interface

This folder contains a public-safe interface for an OCI user audit framework.

The goal of the framework is to take a user identifier, search for that user across OCI identity domains, and return a structured report showing the user's domain, group membership, IAM policy context, password policy context, and selected user security attributes.

This package is intentionally minimal. It exposes the public API shape and data model, but it does not include the full implementation, OCI request wiring, secret handling, or environment-specific logic.

## What The Framework Does

At a high level, the framework is designed to:

- accept a user identifier as input
- search for that user in one or more OCI identity domains
- collect the groups the user belongs to
- map IAM policies for those groups
- map password policies for those groups
- return a normalized report in text or JSON form

## Inputs

The minimal public API is centered on a single audit request.

Typical input fields are:

- `user_name`
  The user login, email, or directory identifier to search for.
- `profile`
  The OCI config profile name to use, such as `DEFAULT`.
- `config_file`
  The OCI configuration file path, usually `~/.oci/config`.

Example conceptual call:

```python
report = audit_user(
    "user@example.com",
    profile="DEFAULT",
    config_file="~/.oci/config",
)
```

## Outputs

The framework returns a structured dictionary-like report.

Typical top-level output fields are:

- `query`
  The input user name that was searched.
- `domains_checked`
  The domains scanned during the audit.
- `matches`
  Matching user records and their associated group/policy details.
- `summary`
  Aggregate counts such as how many domains were checked and how many matches were found.

Each match typically contains:

- `domain`
  Basic identity domain details
- `user`
  User summary fields
- `groups`
  User groups, with IAM and password policy details
- `user_security`
  Lock, reset, or password-related security state when available

See [examples.py](./examples.py) for a sample output shape.

## Public Files

- [api.py](./api.py)
  Top-level public interface
- [models.py](./models.py)
  Report and data-shape definitions
- [providers.py](./providers.py)
  Abstract provider interface
- [examples.py](./examples.py)
  Example report structure

## Why This Is Minimal

This public package intentionally excludes:

- internal module breakdown
- request sequencing
- matching and fallback logic
- secret storage and passphrase retrieval
- OCI SDK implementation details
- logging and operational behavior

Use this version when you want to document the framework contract without publishing the internal working code.
