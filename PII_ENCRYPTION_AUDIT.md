# PII Encryption Audit

## Sensitive fields

- `Users.email`
- `Users.name`
- `Users.website`
- `Users.affiliation`
- `Users.country`
- `UserFieldEntries.value`
- `Teams.email`
- `Teams.website`
- `Teams.affiliation`
- `Tracking.ip`
- `Submissions.ip`
- MFA secret and recovery codes

## Status

| Requirement | Status |
|---|---|
| AES-256-GCM helper | IMPLEMENTED AND TESTED |
| External key environment | IMPLEMENTED AND TESTED |
| Previous-key rotation fallback | IMPLEMENTED AND TESTED |
| MFA secret encryption | IMPLEMENTED AND TESTED |
| Hashed recovery codes | IMPLEMENTED AND TESTED |
| Database read/write integration | PARTIALLY IMPLEMENTED |
| Existing-record migration | NOT IMPLEMENTED |
| API encrypted-field suppression | PARTIALLY IMPLEMENTED |

Email is intentionally retained in plaintext where uniqueness/index lookup is required. Other retrievable PII requires a deliberate column migration and key-management procedure.
