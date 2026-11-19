# PII Encryption Test Report

## Executed

Command:

```text
.venv/bin/python -m pytest tests/test_pii_encryption.py tests/utils/test_passwords.py -q
```

Result: 13 passed.

## Coverage

- Database writes store `v1:` ciphertext for user/team PII.
- Database reads return plaintext only to application code.
- AES-GCM tampering rejects ciphertext.
- Missing and invalid encryption keys reject writes/reads.
- Previous-key decryption succeeds during rotation.
- Current-key mismatch fails closed.
- Legacy plaintext record recovery is tested on a local database.
- Email and team HMAC lookup indexes are tested.
- Public user/team serialization excludes affiliation and country.

## Broader compatibility

Command:

```text
.venv/bin/python -m pytest tests/users/test_profile.py tests/teams/test_teams.py tests/api/v1/test_users.py tests/api/v1/test_teams.py -q
```

Result: 91 passed.

## Limitations

- Migration utility has not been executed against production.
- No staging backup restoration was externally executed.
- Custom JSON field values remain partially classified.
- Email remains plaintext in the existing lookup column; only a keyed index was added.
