# Security Implementation

| Change | Files | Test |
|---|---|---|
| Argon2id password hashing with bcrypt-SHA256 verification fallback | `Tandav/utils/crypto/__init__.py` | `tests/utils/test_passwords.py` |
| SHA-256 HMAC signing default | `Tandav/utils/security/signing.py` | Focused password/config suite |
| Secure-cookie configuration and HTTPS HSTS | `Tandav/config.py`, `Tandav/config.ini`, `Tandav/utils/initialization/__init__.py` | `tests/test_config.py` |
| Rate-limit `Retry-After` header | `Tandav/utils/decorators/__init__.py` | `tests/utils/test_ratelimit.py` |
| Security response headers | `Tandav/utils/initialization/__init__.py` | Existing app/config tests |
| Flag values removed from submission log messages | `Tandav/api/v1/challenges.py` | Code review plus focused challenge tests remain recommended |
| Mandatory MFA enrollment and verification for administrators | `Tandav/utils/decorators/__init__.py`, `Tandav/utils/initialization/__init__.py`, `Tandav/auth.py`, `Tandav/utils/security/mfa.py` | Preset-admin/API MFA denial test and focused MFA tests |
| MFA secrets AES-GCM encrypted; recovery codes SHA-256 hashed | `Tandav/utils/security/mfa.py`, `Tandav/models/__init__.py` | PII/MFA crypto round-trip tests |
| Submitted values removed from new solve/fail/partial records | `Tandav/plugins/challenges/__init__.py`, `Tandav/schemas/submissions.py` | Flag and submission tests |
| Static flag comparison uses constant-time HMAC-style digest comparison | `Tandav/plugins/flags/__init__.py` | Static/regex flag tests |
| Administrator permission map and audit event model | `Tandav/utils/security/admin.py`, `Tandav/models/__init__.py` | Audit model tests remain required |
| PII AES-GCM key rotation fallback | `Tandav/utils/crypto/__init__.py` | AES-GCM rotation test |
| Existing submission cleanup migration | `migrations/versions/c3d4e5f6a7b8_add_audit_and_submission_cleanup.py` | Migration not executed against a production copy |

## Verification

Focused validation: 20 tests passed.

Runtime verification confirmed:
- New passwords start with `$argon2id$`.
- Correct and incorrect passwords behave as expected.
- Existing bcrypt-SHA256 credentials continue to verify.

The CSP uses existing application assumptions and should be validated in staging before production because inline script/style usage may require a nonce-based tightening.
