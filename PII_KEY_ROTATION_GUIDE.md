# PII Key Rotation Guide

## Encryption key

1. Generate a new 32-byte key and base64-encode it.
2. Set `PII_ENCRYPTION_KEY_PREVIOUS` to the old key.
3. Set `PII_ENCRYPTION_KEY` to the new key.
4. Deploy and verify reads of old ciphertext.
5. Re-encrypt active PII in batches using the staging migration utility.
6. Remove `PII_ENCRYPTION_KEY_PREVIOUS` only after all ciphertext is re-encrypted and backup verification succeeds.

## Search key

1. Generate a new 32-byte search key.
2. Recompute email HMAC values using `pii_search_index`.
3. Update `email_hmac` for users and teams in a staging batch.
4. Switch `PII_SEARCH_KEY` only after all index values are updated.
5. Preserve old search keys only for a documented transition period if queries must continue.

## Failure handling

- Invalid or missing encryption keys fail writes.
- Reads of ciphertext without a valid current or previous key fail closed.
- Never log key values or plaintext PII.
- Rotate MFA encryption and PII encryption separately.
