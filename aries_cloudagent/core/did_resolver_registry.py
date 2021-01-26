"""In memmory storage for registering did resolvers."""

import logging
from typing import Sequence

LOGGER = logging.getLogger(__name__)


class DIDResolverRegistry:
    """Registry for did resolvers."""

    def __init__(self):
        """Initialize list for did resolvers."""
        self._resolvers = []
        LOGGER.debug("Resolvers listed")

    @property
    def did_resolvers(
        self,
    ) -> Sequence[str]:  # Todo: add priority filtering and return copy
        """Accessor for a list of all did resolvers."""
        return self._resolvers

    def register(self, resolver) -> None:
        """Register a resolver."""
        LOGGER.debug("Registering resolver %s", resolver)
        self._resolvers.append(resolver)
