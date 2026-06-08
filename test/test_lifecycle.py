import pytest

# @BeforeEach + @AfterEach
@pytest.fixture
def risorsa():
    print("\nApertura risorsa")
    dati = {"connesso": True, "valore": 42}
    yield dati
    print("Chiusura risorsa")
    dati["connesso"] = False

def test_valore(risorsa):
    assert risorsa["valore"] == 42

def test_connessione(risorsa):
    assert risorsa["connesso"] == True


# @BeforeAll + @AfterAll
@pytest.fixture(scope="session")
def server():
    print("\nAvvio server")
    stato = {"attivo": True}
    yield stato
    print("Spegnimento server")
    stato["attivo"] = False

def test_server_attivo(server):
    assert server["attivo"] == True

def test_server_risponde(server):
    assert server["attivo"] == True
