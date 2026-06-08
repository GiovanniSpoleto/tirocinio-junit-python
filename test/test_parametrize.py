import pytest
from calcolatrice import somma

# @ValueSource
@pytest.mark.parametrize("numero", [1, 2, 3, 4, 5])
def test_numero_positivo(numero):
    assert numero > 0

# @CsvSource inline
@pytest.mark.parametrize("a, b, atteso", [
    (2,  3,  5),
    (0,  0,  0),
    (-1, 1,  0),
    (10, 5, 15),
])
def test_somma(a, b, atteso):
    assert somma(a, b) == atteso
