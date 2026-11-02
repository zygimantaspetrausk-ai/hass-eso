"""Mūsų namai kopija: ESO kelias pašalintas (jis skaitė pašto dėžutę per IMAP).

Liko tik klaidų klasės, kurias naudoja Ignitis klientas, ir ESOClient
užkaištis, kad senas kodas nesuveiktų net per klaidą.
"""


class ESOError(Exception):
    """Base error for provider client failures."""


class ESOConnectionError(ESOError):
    """Raised when the provider service cannot be reached."""


class ESOAuthError(ESOError):
    """Raised when the supplied credentials are rejected."""


class ESOTwoFactorError(ESOError):
    """Kept for compatibility; ESO two-factor login is not supported."""


class ESOClient:
    """ESO provider is disabled in this fork."""

    def __init__(self, *args, **kwargs):
        raise ESOAuthError("ESO teikėjas šioje kopijoje išjungtas – naudokite Ignitis")
