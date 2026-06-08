import pytest
from calcolatrice import somma, divisione

@pytest.fixture
def numeri():
    return {"a": 10, "b": 2}

def test_somma(numeri):
    assert somma(numeri["a"], numeri["b"]) == 12

def test_divisione(numeri):
    assert divisione(numeri["a"], numeri["b"]) == 5
