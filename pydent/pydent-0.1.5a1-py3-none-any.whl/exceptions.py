"""
Trident exceptions
"""

from requests.exceptions import RequestException, ConnectTimeout


class TridentRequestError(IOError):
    """There was an ambiguous exception that occurred handling your request."""


class AquariumError(IOError):
    """Aquarium raised an error"""


class ForbiddenRequestError(Exception):
    """Raised when Trident attempts to make a request after requests have been
    explicitly turned off."""


class TridentJSONDataIncomplete(RequestException):
    """JSON data contains a null value and may be incomplete."""


class TridentLoginError(RequestException):
    """Trident is not properly connected to the server.
     Verify login credentials are correct."""


class TridentTimeoutError(ConnectTimeout):
    """Trident took too long to respond"""


class TridentModelNotFoundError(AttributeError):
    """Trident could not find model in list of models."""


class AquariumModelError(Exception):
    """An error occurred with this Aquarium model"""


class NoSessionError(Exception):
    """There was no session attached to the model, but one is required."""
