from hypothesis import given, strategies as st
from calcolatrice import somma, moltiplicazione

@given(st.integers(), st.integers())
def test_somma_commutativa(a, b):
    assert somma(a, b) == somma(b, a)

@given(st.integers())
def test_somma_zero_neutrale(a):
    assert somma(a, 0) == a

@given(st.integers())
def test_moltiplica_per_uno_neutrale(a):
    assert moltiplicazione(a, 1) == a

@given(st.integers(min_value=1), st.integers(min_value=1))
def test_somma_positivi_e_positiva(a, b):
    assert somma(a, b) > 0
