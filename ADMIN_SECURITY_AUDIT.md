# Admin Security Audit

## Route inventory

Admin routes include users, teams, challenges, submissions, statistics, scoreboard, notifications, pages, modules, audiences, plugins, import/export, CSV, configuration, reset, and file operations.

## Controls

- Global MFA requirement for administrators.
- Central permission names for users, challenges, submissions, config, pages, and uploads.
- Permission deny behavior on mapped admin/API namespaces.
- Session security version for revocation.
- Reauthentication helper for sensitive operations.
- Append-only audit event model.
- Privileged role and permission mass-assignment protection.

## Status

| Requirement | Status |
|---|---|
| Mandatory MFA | IMPLEMENTED AND TESTED |
| Backend authorization | PARTIALLY IMPLEMENTED |
| Granular route permission mapping | PARTIALLY IMPLEMENTED |
| Audit event model | IMPLEMENTED BUT NOT TESTED |
| Participant denial tests | PARTIALLY IMPLEMENTED |
| Sensitive reauthentication integration | IMPLEMENTED BUT NOT TESTED |

All route handlers need route-specific permission decorators and automated participant/admin test coverage.
