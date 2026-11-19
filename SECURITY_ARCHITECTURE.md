# Security Architecture

## Implemented in this phase

- Passwords use Argon2id with per-password salts for new hashes. Existing bcrypt-SHA256 hashes remain readable and are not silently exposed or deleted.
- Session cookies are HttpOnly and configurable as Secure in production; permanent-session lifetime remains configurable.
- HMAC signing for session integrity and verification values uses SHA-256 rather than SHA-1.
- CTF flag submissions are not written to application log formats.
- Rate-limit responses include `Retry-After`.
- Responses include CSP, frame protection, MIME sniffing protection, referrer controls, permissions controls, and HSTS when HTTPS is detected.

## Key files

- Password crypto: `Tandav/utils/crypto/__init__.py`
- Session/config: `Tandav/config.py`, `Tandav/config.ini`, `Tandav/utils/security/auth.py`
- HMAC: `Tandav/utils/security/signing.py`
- Security headers and CSRF/session processing: `Tandav/utils/initialization/__init__.py`
- Flag submission handling: `Tandav/api/v1/challenges.py`
- Tests: `tests/utils/test_passwords.py`, `tests/utils/test_ratelimit.py`

## Remaining production work

A dedicated MFA, RBAC, PII encryption, security-event dashboard, and infrastructure controls require application and deployment configuration beyond this phase. Do not enable preset credentials as a normal production administrator mechanism.
