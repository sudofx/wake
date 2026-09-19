# =============================================================================
# PACKAGE BOUNDARY — intentionally tiny. Importing WAKE✳︎ should identify the package, not start work, mutate state, contact a provider, or create any hidden continuity.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""WAKE✳︎: disposable models, durable accountability."""

__version__ = "0.20.0"
