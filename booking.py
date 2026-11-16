"""Simplified booking validation for the workshop."""


def can_book(quantity, available):
    """Return whether an integer quantity fits non-negative available capacity.

    Input types and non-negative capacity are validated by the caller.
    """
    return 1 <= quantity <= available
