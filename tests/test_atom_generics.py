# Test A.t and A[int].t and A[int] is A[int] -> True
import pytest 
import sys 
from typing import Generic, TypeVar 

from atom.api import (

Atom,
Int,
Str,
Dict,
Value,
Bool,
Instance,




)

def test_generics() :
    T = TypeVar("T", bound= object)

    class A(Atom, Generic[T]):
        t: T
    assert isinstance(A.t, Value)
    assert isinstance(A[int].t, Int)
    

    

