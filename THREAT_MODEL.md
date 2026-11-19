# Threat Model

## Protected assets

- Participant accounts and password material
- Administrator sessions and authorization decisions
- CTF flags and score events
- PII, team membership, submissions, exports, and uploads
- Database credentials, Redis, signing secrets, and backup data

## Primary threats

- Credential stuffing, brute force, session theft, and account enumeration
- Privilege escalation and unauthorized admin API use
- Flag disclosure, duplicate scoring, submission races, and score manipulation
- SQL/XSS/CSRF/SSRF/path traversal and unrestricted uploads
- DDoS and abusive automated submissions
- Secret exposure and exposed debug or database configuration

## Mitigations in this phase

- Argon2id password hashing with salt and legacy bcrypt-SHA256 verification compatibility
- Existing CSRF nonce enforcement retained
- Endpoint-specific rate limits retained and `Retry-After` added
- Submission lock and database solve uniqueness retained
- Flag values removed from application log format strings
- Security headers added at the application response boundary

## Residual risk

MFA, fine-grained RBAC, PII encryption, distributed abuse evidence, log restrictions, backup testing, vulnerability scanning, and incident tooling require implementation and operations outside the demonstrated baseline.
