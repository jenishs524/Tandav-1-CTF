# Incident Response

1. **Classify**: account compromise, admin compromise, data breach, flag leak, DDoS, database compromise, or secret exposure.
2. **Contain**: disable compromised accounts, revoke sessions/tokens, block abusive endpoints, isolate affected hosts, and preserve logs.
3. **Rotate**: secret keys, database credentials, SMTP/OAuth credentials, API tokens, and signing keys as applicable.
4. **Preserve evidence**: retain immutable audit and security logs with access controls.
5. **Recover**: restore from verified backups, invalidate cached sessions, and validate database integrity and flag confidentiality.
6. **Review**: identify root cause, improve controls, notify stakeholders according to policy, and document corrective actions.

For likely flag leakage, rotate affected flags and invalidate duplicate or inconsistent score events through an administrator-reviewed process. Do not automatically ban legitimate users based on isolated suspicious submissions.
