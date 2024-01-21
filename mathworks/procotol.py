import abc
from typing import TypeVar, runtime_checkable, Protocol

P = TypeVar('P')

@runtime_checkable
class SupportsPos(Protocol[P]):
    """An ABC with one abstract method __pos__ that is covariant in its return type."""
    __slots__ = ()

    @abc.abstractmethod
    def __pos__(self) -> P:
        pass