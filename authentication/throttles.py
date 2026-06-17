from rest_framework.throttling import AnonRateThrottle


class AuthRateThrottle(AnonRateThrottle):
    """Login / register only — not applied to normal authenticated app traffic."""

    scope = "auth"
