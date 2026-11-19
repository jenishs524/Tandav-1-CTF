# Production Deployment Checklist

| Requirement | Status |
|---|---|
| HTTPS and secure cookies | REQUIRES EXTERNAL CONFIGURATION |
| Trusted reverse proxy | PARTIALLY IMPLEMENTED |
| WAF/upstream DDoS | REQUIRES EXTERNAL CONFIGURATION |
| Host firewall/exposed ports | REQUIRES EXTERNAL CONFIGURATION |
| Database network isolation | REQUIRES EXTERNAL CONFIGURATION |
| Redis private/authenticated access | REQUIRES EXTERNAL CONFIGURATION |
| Secret-management service | REQUIRES EXTERNAL CONFIGURATION |
| Encrypted backup | REQUIRES EXTERNAL CONFIGURATION |
| Backup restoration test | REQUIRES EXTERNAL CONFIGURATION |
| Docker non-root execution | IMPLEMENTED AND TESTED |
| Docker resource limits | NOT IMPLEMENTED |
| Container challenge isolation | REQUIRES EXTERNAL CONFIGURATION |

## Exact deployment blockers

- Encrypt and migrate PII before public deployment.
- Provide live Redis, TLS, private networking, secrets, firewall, backup, and restore verification.
- Complete route-specific permission test coverage.
- Execute and verify submission cleanup against an isolated staging copy.
- Establish anti-cheat review and appeal procedures.
