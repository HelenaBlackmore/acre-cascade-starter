"""Utility functions."""

from typing import Any, Callable, Type, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])


class implements:  # pylint: disable=invalid-name
    """Mark a function as implementing an interface."""

    def __init__(self, interface: Type):
        """Instantiate the decorator.

        Args:
            interface: the interface that is implemented
        """
        self.interface = interface

    def __call__(self, func: _F) -> _F:
        """Take a function and return it unchanged."""
        super_method = getattr(self.interface, func.__name__, None)
        assert super_method is not None, f"'{func.__name__}' does not exist in {self.interface}"
        # Remove until pytorch update their docstrings
        # assert super_method.__doc__, f"'{super_method}' has no docstring"
        return func
