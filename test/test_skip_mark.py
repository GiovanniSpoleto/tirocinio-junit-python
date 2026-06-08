import pytest
import sys
from calcolatrice import somma

# @Disabled
@pytest.mark.skip(reason="funzionalità ancora da implementare")
def test_da_fare():
    assert somma(2, 2) == 5

# @DisabledOnOs
@pytest.mark.skipif(sys.platform == "win32", reason="solo Linux")
def test_solo_linux():
    assert somma(1, 1) == 2

# @Tag("veloce")
@pytest.mark.veloce
def test_somma_veloce():
    assert somma(2, 3) == 5

# @Tag("lento")
@pytest.mark.lento
def test_somma_lento():
    assert somma(100, 200) == 300
