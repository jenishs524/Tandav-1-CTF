# Infrastructure Security

## Current application controls

- Application runs as UID 1001 in Docker.
- Redis-backed cache is used when configured.
- Reverse proxy and trusted-host controls exist.
- HTTP security headers exist.
- Upload and database volumes are mounted locally.

## External configuration

| Control | Status |
|---|---|
| Cloudflare WAF | REQUIRES EXTERNAL CONFIGURATION |
| Upstream DDoS mitigation | REQUIRES EXTERNAL CONFIGURATION |
| TLS 1.2+ | REQUIRES EXTERNAL CONFIGURATION |
| Host firewall | REQUIRES EXTERNAL CONFIGURATION |
| Database private network | REQUIRES EXTERNAL CONFIGURATION |
| Secure secrets manager | REQUIRES EXTERNAL CONFIGURATION |
| Encrypted backups | REQUIRES EXTERNAL CONFIGURATION |
| Backup restoration testing | REQUIRES EXTERNAL CONFIGURATION |
| Container/dependency scanning | REQUIRES EXTERNAL CONFIGURATION |
| Redis authentication/private network | REQUIRES EXTERNAL CONFIGURATION |
