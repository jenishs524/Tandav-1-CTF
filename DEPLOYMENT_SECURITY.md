# Deployment Security

## Required production configuration

- Set `SECRET_KEY` through environment-managed secrets; do not rely on the generated `.tandav_secret_key`.
- Set `SESSION_COOKIE_SECURE=true` and terminate TLS at the trusted reverse proxy.
- Set `TRUSTED_HOSTS` to the exact application hostnames.
- Configure trusted proxy forwarding only for known proxies.
- Configure Redis with authentication and private-network access.
- Use a least-privilege database account and encrypted database connections.
- Store uploads outside public web roots and mount only through authorized download endpoints.
- Run the container non-root and keep the image minimized and patched.

## External infrastructure requirements

CDN/WAF/DDoS protection, private database networking, host firewall rules, centralized logs, backup encryption, malware scanning, secret KMS, and container/dependency scanning require provider-specific deployment integration.
