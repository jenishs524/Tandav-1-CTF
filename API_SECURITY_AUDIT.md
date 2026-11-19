# API Security Audit

## Route inventory

API v1 resources include challenges, users, teams, flags, submissions, files, exports, pages, notifications, modules, audiences, awards, hints, topics, tags, unlocks, comments, scoreboard, and statistics.

## Status

| Check | Status |
|---|---|
| Authentication decorators | IMPLEMENTED AND TESTED |
| CSRF nonce handling | IMPLEMENTED AND TESTED |
| Admin MFA gate | IMPLEMENTED AND TESTED |
| Privileged mass-assignment guard | IMPLEMENTED AND TESTED |
| Input validation | PARTIALLY IMPLEMENTED |
| IDOR/BOLA object checks | PARTIALLY IMPLEMENTED |
| Sensitive serialization | PARTIALLY IMPLEMENTED |
| Redis endpoint limits | IMPLEMENTED BUT NOT TESTED |
| Request/response size limits | REQUIRES EXTERNAL CONFIGURATION |

Critical remaining work: test every participant credential against every admin API and apply object-level checks to team, user, flag, file, export, and submission resources.
