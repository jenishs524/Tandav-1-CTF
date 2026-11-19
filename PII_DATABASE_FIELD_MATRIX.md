# PII Database Field Matrix

| Table.Field | Classification | Storage now | Read/write evidence |
|---|---|---|---|
| `users.website` | PII | AES-GCM | `EncryptedPIIText` in model; database ciphertext test |
| `users.affiliation` | PII | AES-GCM | `EncryptedPIIText` in model; tamper test |
| `users.country` | PII | AES-GCM | `EncryptedPIIText` in model; rotation test |
| `teams.website` | PII | AES-GCM | `EncryptedPIIText` in model; team database test |
| `teams.affiliation` | PII | AES-GCM | `EncryptedPIIText` in model; team database test |
| `teams.country` | PII | AES-GCM | `EncryptedPIIText` in model |
| `users.email` | PII/search key | Plaintext plus HMAC | Existing login/reset lookups require plaintext; `email_hmac` keyed index added |
| `teams.email` | PII/search key | Plaintext plus HMAC | Existing team lookups require plaintext; `email_hmac` keyed index added |
| `users.name` | Public PII | Plaintext | Public identity and existing search compatibility |
| `teams.name` | Public PII | Plaintext | Public team identity and existing search compatibility |
| `user_field_entries.value` | Potential PII | Plaintext JSON | Field definitions determine semantics; no automatic classification |
| `team_field_entries.value` | Potential PII | Plaintext JSON | Field definitions determine semantics; no automatic classification |
| `tracking.ip` | PII/security evidence | Plaintext | Security evidence; minimize/retention policy remains required |
| `submissions.ip` | PII/security evidence | Plaintext | Security evidence; retention policy remains required |
| `users.mfa_secret_encrypted` | Authentication secret | AES-GCM | MFA crypto tests |
| `users.mfa_recovery_codes` | Authentication secret | SHA-256 hashes | Recovery-code tests |
