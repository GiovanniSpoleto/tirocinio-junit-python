import pytest
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

def test_somma():
    assert somma(2, 3) == 5

def test_sottrazione():
    assert sottrazione(10, 3) == 7

def test_moltiplicazione():
    assert moltiplicazione(4, 3) == 12

def test_divisione():
    assert divisione(10, 2) == 5

def test_divisione_per_zero():
    with pytest.raises(ValueError):
        divisione(10, 0)
