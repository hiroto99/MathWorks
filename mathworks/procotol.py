import abc
from typing import TypeVar

P = TypeVar('P')

@abc.runtime_checkable
class SupportsPos(abc.Protocol[P]):
    """An ABC with one abstract method __pos__ that is covariant in its return type."""
    __slots__ = ()

    @abc.abstractmethod
    def __pos__(self) -> P:
        pass