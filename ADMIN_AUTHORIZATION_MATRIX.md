# Administrator Authorization Matrix

| Area | Controls | Status |
|---|---|---|
| Login and MFA | Session MFA gate and MFA enrollment | IMPLEMENTED AND TESTED |
| Admin HTML routes | `admins_only` plus mapped or deny-unknown permission logic | IMPLEMENTED AND TESTED |
| Admin API routes | Server-side decorators and namespace permission mapping | PARTIALLY IMPLEMENTED |
| Role changes | `type` and permissions require admin config permission | IMPLEMENTED AND TESTED |
| Privilege escalation | Participant privileged mass assignment blocked | IMPLEMENTED AND TESTED |
| Session revocation | Security version check | IMPLEMENTED AND TESTED |
| Audit events | Append-only model/helper | IMPLEMENTED BUT NOT TESTED |
| Sensitive reauthentication | 15-minute helper | IMPLEMENTED BUT NOT TESTED |
| Unknown namespace behavior | Deny unknown privileged namespace | IMPLEMENTED AND TESTED |

Every administrator route should still receive a route-specific test; broad suite coverage does not replace full route coverage.
