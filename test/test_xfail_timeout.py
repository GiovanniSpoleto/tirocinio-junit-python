import pytest
import time
from calcolatrice import somma, divisione

# ════════════════════════════════════════════════════════════════════════════
# SEZIONE 1 — xfail
# Equivalente di @expectedFailure in unittest
# Non esiste in JUnit — @Disabled salta il test, xfail lo esegue
# ════════════════════════════════════════════════════════════════════════════

# Caso 1 — test che fallisce come atteso → XFAIL
@pytest.mark.xfail(reason="bug noto: somma non gestisce i float")
def test_somma_float():
    assert somma(0.1, 0.2) == 0.3
    # 0.1 + 0.2 = 0.30000000000000004 in Python — bug noto floating point
    # il test fallisce → XFAIL — atteso, non blocca la suite

# Caso 2 — funzionalità non ancora implementata → XFAIL
@pytest.mark.xfail(reason="funzione modulo non ancora implementata")
def test_modulo():
    from calcolatrice import modulo   # non esiste ancora
    assert modulo(10, 3) == 1

# Caso 3 — xfail condizionale — solo su certe piattaforme
@pytest.mark.xfail(
    condition=True,
    reason="comportamento non definito in questa versione"
)
def test_divisione_intera():
    assert divisione(7, 2) == 3   # restituisce 3.5, non 3 → XFAIL

# Caso 4 — strict=True: se passa inaspettatamente diventa FAILED
@pytest.mark.xfail(strict=True, reason="questo NON deve mai passare")
def test_somma_sbagliata():
    assert somma(2, 2) == 99   # sbagliato → XFAIL con strict

# Caso 5 — unittest equivalente: @expectedFailure
import unittest

class TestExpectedFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_somma_float_unittest(self):
        """Equivalente di xfail in unittest"""
        self.assertEqual(0.1 + 0.2, 0.3)
        # fallisce come atteso → ok


# ════════════════════════════════════════════════════════════════════════════
# SEZIONE 2 — Timeout
# Equivalente parziale di @Timeout in JUnit
# Non nativo in Python — richiede plugin pytest-timeout
# ════════════════════════════════════════════════════════════════════════════

# Caso 1 — test veloce che passa entro il timeout
@pytest.mark.timeout(2)
def test_somma_veloce():
    """Deve completarsi entro 2 secondi"""
    assert somma(2, 3) == 5

# Caso 2 — test lento che supera il timeout → FAILED
@pytest.mark.timeout(1)
@pytest.mark.xfail(reason="questo test supera il timeout intenzionalmente")
def test_operazione_lenta():
    """Simula un'operazione che supera il timeout"""
    time.sleep(2)   # dorme 2 secondi ma il timeout è 1
    assert somma(2, 3) == 5

# Caso 3 — timeout su una funzione più complessa
@pytest.mark.timeout(5)
def test_somma_multipla():
    """Esegue molte somme — deve completarsi entro 5 secondi"""
    risultato = 0
    for i in range(1000):
        risultato = somma(risultato, i)
    assert risultato == 499500

