# Test A.t and A[int].t and A[int] is A[int] -> True

from typing import Generic, TypeVar

from atom.api import Atom, Int, Value


def test_generics():
    T = TypeVar("T", bound=object)

    class A(Atom, Generic[T]):
        t: T

    assert isinstance(A.t, Value)
    assert isinstance(A[int].t, Int)

    assert A[int] is A[int]
