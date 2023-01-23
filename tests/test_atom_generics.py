# Test A.t and A[int].t and A[int] is A[int] -> True

from typing import Generic, TypeVar

from atom.api import Atom, Int, Value, Str, List

T = TypeVar("T", bound=object)


def test_generics():
    class A(Atom, Generic[T]):
        t: T

    assert isinstance(A.t, Value)
    assert isinstance(A[int].t, Int)

    assert A[int] is A[int]


def test_double_generics():
    U = TypeVar("U", bound=object)

    class A(Atom, Generic[T, U]):

        t: T
        u: U

    assert isinstance(A[int, str].t, Int)
    assert isinstance(A[int, str].u, Str)


def test_list():
    class A(Atom, Generic[T]):

        l: list[T]

    assert isinstance(A.l, List)
    assert isinstance(A[int].l.validate_mode[1], Value)
    assert isinstance(A[int].l, List)
    assert isinstance(A[int].l.validate_mode[1], Int)
