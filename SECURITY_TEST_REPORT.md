# Security Test Report

## Executed

Command:

```text
.venv/bin/python -m pytest tests/utils/test_passwords.py tests/utils/test_ratelimit.py tests/test_config.py Tandav/plugins/flags/tests/test_flags.py -q
```

Result: 20 passed.

## Coverage

- Argon2id password generation
- Password mismatch rejection
- Legacy bcrypt-SHA256 verification
- Preset administrator behavior
- Reverse proxy settings
- Trusted hosts
- Server-sent events
- Login rate limiting
- AES-256-GCM PII and MFA secret round trips
- MFA recovery-code hashing
- Static and regex flag comparison
- Preset-admin API access denial before MFA enrollment
- Privileged-field mass assignment rejection
- PII AES-GCM previous-key decryption

## Additional required tests

- MFA enrollment and enforcement
- Admin authorization and privilege escalation
- IDOR/BOLA across user/team/challenge APIs
- SQL/XSS/CSRF input cases
- Duplicate solve transactions under concurrency
- Public API/response flag absence
- Upload file signatures and traversal
- Security header assertions
- Session revocation after password changes
