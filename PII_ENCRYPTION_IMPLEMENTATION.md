# PII Encryption Implementation

## Implemented

- AES-256-GCM encryption for `Users.website`, `Users.affiliation`, `Users.country`, `Teams.website`, `Teams.affiliation`, and `Teams.country`.
- SQLAlchemy `EncryptedPIIText` read/write type.
- Ciphertext stored as `v1:<base64(nonce+ciphertext)>`.
- AES-GCM authentication rejects nonce/ciphertext/tamper changes.
- Previous-key fallback for staged key rotation.
- Keyed SHA-256 HMAC indexes for normalized user and team email values.
- Public user/team serialization excludes affiliation and country.
- Test-only keys are isolated through the test harness.

## Code paths

- Write and read: `Tandav/models/__init__.py`, `Tandav/utils/crypto/__init__.py`
- Public serialization: `Tandav/schemas/users.py`, `Tandav/schemas/teams.py`
- Keyed lookup: `pii_search_index()` and `email_hmac`
- Migration: `migrations/versions/d4e5f6a7b8c9_add_pii_search_indexes.py`
- Staging migration utility: `scripts/migrate_pii.py`

## Not yet fully integrated

- `Users.email`, `Teams.email`, and `Users.name` remain plaintext where lookup/public profile compatibility requires it.
- Arbitrary `UserFieldEntries.value` and `TeamFieldEntries.value` JSON values are not classified and are not automatically encrypted.
- Full export encryption requires a deployment-level backup/export policy.

## Decision

**PARTIALLY INTEGRATED**. AES-GCM is active for actual profile PII database writes and reads, but email/name/custom-field classification and migration of existing records are incomplete.
