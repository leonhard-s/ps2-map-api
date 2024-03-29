"""Endpoint definitions for the API."""

from .bases import router as bases
from .continents import router as continents
from .outfits import router as outfit
from .servers import router as servers

# NOTE: app.py expects this __all__ export to only contain routers. Non-router
# things will make it very sad.
#
# This is intentional. Add an isinstance check to app.py if you deem non-router
# things in the __all__ list necessary.

__all__ = [
    'bases',
    'continents',
    'outfit',
    'servers'
]
