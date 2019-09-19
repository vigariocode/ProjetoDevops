import pytest
from Principal import somar
from Principal import subtrair

def test_somar():
    assert somar(2,4)==6

def test_subtrair():
    assert subtrair(9,5)==4