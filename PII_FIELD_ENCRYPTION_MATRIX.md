# PII Field Encryption Matrix

| Field | Classification | Current storage | Status |
|---|---|---|---|
| `Users.email` | PII/index key | Plaintext | NOT IMPLEMENTED |
| `Users.name` | PII | Plaintext | NOT IMPLEMENTED |
| `Users.website` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Users.affiliation` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Users.country` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `UserFieldEntries.value` | PII | Plaintext JSON | NOT IMPLEMENTED |
| `Teams.email` | PII/index key | Plaintext | NOT IMPLEMENTED |
| `Teams.website` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Teams.affiliation` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Teams.country` | PII | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Tracking.ip` | PII/security evidence | Plaintext | PARTIALLY IMPLEMENTED |
| `Submissions.ip` | PII/security evidence | Plaintext | PARTIALLY IMPLEMENTED |
| `Users.mfa_secret_encrypted` | Authentication secret | AES-GCM ciphertext | IMPLEMENTED AND TESTED |
| `Users.mfa_recovery_codes` | Authentication secret | SHA-256 hashes | IMPLEMENTED AND TESTED |

AES-GCM database integration and key-rotation tests are operational for profile PII. Existing-record encryption, email/name/custom-field encryption, backup restoration, and export policy remain incomplete.
