# Security Configuration

## Application settings

| Setting | Safe default/requirement |
|---|---|
| `SECRET_KEY` | External secret, rotated through a controlled procedure |
| `SESSION_COOKIE_HTTPONLY` | `true` |
| `SESSION_COOKIE_SECURE` | `true` in production |
| `SESSION_COOKIE_SAMESITE` | `Lax` or stricter after compatibility testing |
| `PERMANENT_SESSION_LIFETIME` | Shorter for administrative deployments |
| `TRUSTED_HOSTS` | Exact production host allowlist |
| `RATELIMIT_DISABLE` | Must be false in production |

## Operational checks

- Confirm password hashes use `$argon2id$` for newly created accounts.
- Confirm HTTPS produces HSTS.
- Confirm CSP and frame headers are present.
- Confirm rate-limited responses include `Retry-After`.
- Confirm submission logs do not contain submitted flag values.
- Confirm database and Redis credentials are supplied through secrets, never source control.
