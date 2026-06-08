import csv
import os
import pytest
from calcolatrice import somma

def carica_csv(nome_file):
    percorso = os.path.join(os.path.dirname(__file__), nome_file)
    try:
        with open(percorso, newline="", encoding="utf-8") as f:
            return [(int(r[0]), int(r[1]), int(r[2])) for r in csv.reader(f)]
    except FileNotFoundError:
        pytest.fail(f"File non trovato: {percorso}")
    except (ValueError, IndexError) as e:
        pytest.fail(f"Formato CSV non valido: {e}")

@pytest.mark.parametrize("a, b, atteso", carica_csv("test_data.csv"))
def test_somma_da_file(a, b, atteso):
    assert somma(a, b) == atteso
