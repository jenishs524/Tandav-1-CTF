# Flag Security Audit

## Storage and records

- Raw challenge flags remain stored in `Flags.content` as required for challenge administration and server-side validation.
- New solves, fails, partials, and rate-limit records write `provided=None`.
- Public challenge/flag APIs do not expose challenge flags.
- Existing submission values are identified by `Submissions.provided IS NOT NULL`.
- A reviewed migration records only submission IDs and cleanup state before clearing values.

## Status

| Requirement | Status |
|---|---|
| Server-side flag validation | IMPLEMENTED AND TESTED |
| Constant-time static comparison | IMPLEMENTED AND TESTED |
| Regex verification | IMPLEMENTED AND TESTED |
| Submission raw retention prevention | IMPLEMENTED AND TESTED |
| Reversible cleanup procedure | PARTIALLY IMPLEMENTED |
| Existing flag cleanup migration | IMPLEMENTED BUT NOT TESTED |
| Flag-free public responses | IMPLEMENTED BUT NOT TESTED |
| Transactional duplicate scoring | IMPLEMENTED AND TESTED |

The cleanup migration requires an encrypted database backup taken immediately before execution. It cannot restore individual deleted values after backup cleanup.
