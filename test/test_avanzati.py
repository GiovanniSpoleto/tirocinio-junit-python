import pytest
import pytest_check as check
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

# @DisplayName
def test_somma_numeri_positivi():
    """La somma di due numeri positivi deve essere positiva"""
    assert somma(2, 3) == 5

def test_somma_numeri_negativi():
    """La somma di due numeri negativi deve essere negativa"""
    assert somma(-2, -3) == -5

# @Nested
class TestSomma:
    """Gruppo di test per la funzione somma"""

    def test_con_positivi(self):
        assert somma(2, 3) == 5

    def test_con_negativi(self):
        assert somma(-2, -3) == -5

    def test_con_zero(self):
        assert somma(0, 5) == 5


class TestDivisione:
    """Gruppo di test per la funzione divisione"""

    def test_normale(self):
        assert divisione(10, 2) == 5

    def test_per_zero(self):
        with pytest.raises(ValueError):
            divisione(10, 0)

# assertAll
def test_calcolatrice_completa():
    """Verifica tutte le operazioni senza fermarsi al primo errore"""
    check.equal(somma(2, 3),           5)
    check.equal(sottrazione(10, 3),    7)
    check.equal(moltiplicazione(4, 3), 12)
    check.equal(divisione(10, 2),      5)
