# Testing di unità in Python — Confronto con JUnit 6.0.3

Tirocinio Interno — Laurea Triennale in Informatica

Questo repository contiene il codice scritto durante lo studio del framework
JUnit 6.0.3 e il confronto sistematico con gli strumenti di testing disponibili
in Python (pytest, unittest, hypothesis).

## Struttura del progetto

```
tirocinio-junit-python/
├── calcolatrice.py                   # Codice da testare
├── pytest.ini                        # Configurazione pytest (mark personalizzati)
├── requirements.txt                  # Pacchetti Python necessari
├── setup.sh                          # Script per replicare l'ambiente
└── test/
    ├── test_calcolatrice.py          # @Test, assertEquals, assertThrows — pytest
    ├── test_calcolatrice_unittest.py # setUp, assertEqual, assertRaises — unittest
    ├── test_fixture.py               # @BeforeEach con fixture — pytest
    ├── test_lifecycle.py             # @BeforeEach/@AfterEach/@BeforeAll/@AfterAll
    ├── test_parametrize.py           # @ParameterizedTest, @ValueSource, @CsvSource
    ├── test_csv.py                   # @CsvFileSource — dati da file esterno
    ├── test_data.csv                 # Dati per test_csv.py
    ├── test_skip_mark.py             # @Disabled, @Tag, @EnabledOnOs
    ├── test_avanzati.py              # @Nested, @DisplayName, assertAll
    └── test_theories.py              # Theories — property-based testing con hypothesis
```

## Requisiti

- Python 3.13 o superiore
- Linux (testato su Ubuntu 24)

## Setup e esecuzione

### Metodo 1 — Script automatico (consigliato)

```bash
git clone https://github.com/tuonome/tirocinio-junit-python
cd tirocinio-junit-python
chmod +x setup.sh
./setup.sh
```

Lo script crea il virtual environment, installa i pacchetti ed esegue tutti i test.

### Metodo 2 — Manuale

```bash
git clone https://github.com/tuonome/tirocinio-junit-python
cd tirocinio-junit-python

# Crea e attiva il virtual environment
python3 -m venv venv
source venv/bin/activate

# Installa i pacchetti
pip install -r requirements.txt

# Esegui tutti i test
pytest test/ -v
```

## Eseguire i test singolarmente

```bash
# Attiva il venv prima
source venv/bin/activate

# Test base con pytest
pytest test/test_calcolatrice.py -v

# Test base con unittest
python -m unittest test/test_calcolatrice_unittest.py -v

# Lifecycle — BeforeEach/AfterEach/BeforeAll/AfterAll
pytest test/test_lifecycle.py -v -s

# Test parametrizzati
pytest test/test_parametrize.py -v

# Dati da file CSV
pytest test/test_csv.py -v

# Skip e tag
pytest test/test_skip_mark.py -v

# Filtraggio per tag
pytest test/test_skip_mark.py -v -m veloce
pytest test/test_skip_mark.py -v -m lento
pytest test/test_skip_mark.py -v -m "not lento"

# Nested, DisplayName, assertAll
pytest test/test_avanzati.py -v

# Property-based testing con hypothesis
pytest test/test_theories.py -v

# Tutti i test insieme
pytest test/ -v
```

## Funzionalità JUnit confrontate

| Funzionalità JUnit | Libreria Python | File |
|---|---|---|
| `@Test` | pytest | `test_calcolatrice.py` |
| `setUp/tearDown` | unittest | `test_calcolatrice_unittest.py` |
| `@BeforeEach/@AfterEach` | pytest fixture + yield | `test_lifecycle.py` |
| `@BeforeAll/@AfterAll` | pytest fixture scope="session" | `test_lifecycle.py` |
| `assertEquals` | assert nativo | `test_calcolatrice.py` |
| `assertThrows` | pytest.raises | `test_calcolatrice.py` |
| `@ParameterizedTest + @ValueSource` | @pytest.mark.parametrize | `test_parametrize.py` |
| `@CsvSource` | parametrize + tuple | `test_parametrize.py` |
| `@CsvFileSource` | carica_csv() manuale | `test_csv.py` |
| `@Disabled` | @pytest.mark.skip | `test_skip_mark.py` |
| `@Tag` | @pytest.mark.nome | `test_skip_mark.py` |
| `@EnabledOnOs` | @pytest.mark.skipif | `test_skip_mark.py` |
| `@Nested` | classi annidate | `test_avanzati.py` |
| `@DisplayName` | docstring | `test_avanzati.py` |
| `assertAll` | pytest-check | `test_avanzati.py` |
| `Theories/@DataPoints` | hypothesis | `test_theories.py` |

## Ambiente

- Python 3.13.7
- pytest 9.0.3
- hypothesis 6.152.9
- pytest-check 2.8.0
- Linux Ubuntu 24

## Fonti

- JUnit User Guide v6.0.3
- https://docs.pytest.org
- https://docs.python.org/3/library/unittest.html
- https://hypothesis.readthedocs.io
- https://github.com/okken/pytest-check
