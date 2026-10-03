"""Shared WAKE error contracts that do not imply storage authority."""


class IntegrityError(RuntimeError):
    """Signal that durable/replayed WAKE evidence cannot be trusted safely."""

