import pytest
from unittest.mock import MagicMock, patch, call
from servizio_utenti import ServizioUtenti, UtenteRepository, DatabaseError

# ════════════════════════════════════════════════════════════════════════════
# SEZIONE 1 — unittest.mock con MagicMock
# Equivalente di Mockito in Java
# ════════════════════════════════════════════════════════════════════════════

class TestServizioUtentiConMock:
    """Test del ServizioUtenti usando unittest.mock — equivalente di Mockito"""

    def test_get_nome(self):
        """Stub: mock_repo restituisce dati fissi — non tocca il database"""
        # 1. Crea il mock del repository
        mock_repo = MagicMock()

        # 2. Definisci il comportamento (stub)
        mock_repo.trova.return_value = {"id": 1, "nome": "Mario", "stipendio": 1500}

        # 3. Usa il mock nel test
        servizio = ServizioUtenti(mock_repo)
        assert servizio.get_nome(1) == "Mario"

        # 4. Verifica che trova() sia stato chiamato con id=1 (mock)
        mock_repo.trova.assert_called_once_with(1)

    def test_get_stipendio(self):
        """Stub: verifica il calcolo dello stipendio"""
        mock_repo = MagicMock()
        mock_repo.trova.return_value = {"id": 1, "nome": "Mario", "stipendio": 1500}

        servizio = ServizioUtenti(mock_repo)
        assert servizio.get_stipendio(1) == 1500

        mock_repo.trova.assert_called_once_with(1)

    def test_salva_utente(self):
        """Verifica che salva() venga chiamato con i dati corretti"""
        mock_repo = MagicMock()

        servizio = ServizioUtenti(mock_repo)
        risultato = servizio.salva_utente(1, "Mario", 1500)

        assert risultato == True
        # Verifica che salva sia stato chiamato con i dati giusti
        mock_repo.salva.assert_called_once_with(
            {"id": 1, "nome": "Mario", "stipendio": 1500}
        )

    def test_errore_database(self):
        """Simula un errore del database con side_effect"""
        mock_repo = MagicMock()

        # side_effect fa lanciare un'eccezione quando trova() viene chiamato
        mock_repo.trova.side_effect = Exception("Connessione al database persa")

        servizio = ServizioUtenti(mock_repo)

        # Verifica che il servizio gestisca l'eccezione
        with pytest.raises(Exception, match="database"):
            servizio.get_nome(1)

    def test_mock_non_chiamato(self):
        """Verifica che un metodo NON venga chiamato"""
        mock_repo = MagicMock()
        mock_repo.trova.return_value = {"id": 1, "nome": "Mario", "stipendio": 1500}

        servizio = ServizioUtenti(mock_repo)
        servizio.get_nome(1)

        # salva() non deve essere mai chiamato durante get_nome
        mock_repo.salva.assert_not_called()


# ════════════════════════════════════════════════════════════════════════════
# SEZIONE 2 — patch: mock di funzioni standalone
# Impossibile con Mockito in Java — possibile in Python
# ════════════════════════════════════════════════════════════════════════════

class TestConPatch:
    """Test usando patch — mock di funzioni standalone"""

    def test_patch_funzione(self, mocker):
        """Mock di un metodo specifico con patch.object"""
        mock_trova = mocker.patch.object(
            UtenteRepository, "trova",
            return_value={"id": 1, "nome": "Luigi", "stipendio": 2000}
        )
        repo = UtenteRepository()
        servizio = ServizioUtenti(repo)
        assert servizio.get_nome(1) == "Luigi"
        mock_trova.assert_called_once_with(1)

# ════════════════════════════════════════════════════════════════════════════
# SEZIONE 3 — pytest-mock con fixture mocker
# Più comodo con pytest rispetto a with patch(...)
# ════════════════════════════════════════════════════════════════════════════

class TestConPytestMock:
    """Test usando pytest-mock — la fixture mocker"""

    def test_mocker_basic(self, mocker):
        """pytest-mock: non serve il blocco with"""
        mock_repo = mocker.MagicMock()
        mock_repo.trova.return_value = {"id": 1, "nome": "Anna", "stipendio": 1800}

        servizio = ServizioUtenti(mock_repo)
        assert servizio.get_nome(1) == "Anna"
        mock_repo.trova.assert_called_once_with(1)

    def test_mocker_patch(self, mocker):
        """pytest-mock: patch senza blocco with"""
        mock_trova = mocker.patch.object(
            UtenteRepository, "trova",
            return_value={"id": 2, "nome": "Paolo", "stipendio": 2200}
        )
        repo = UtenteRepository()
        servizio = ServizioUtenti(repo)
        assert servizio.get_nome(2) == "Paolo"
        mock_trova.assert_called_once_with(2)

    def test_chiamate_multiple(self, mocker):
        """Verifica più chiamate con valori diversi"""
        mock_repo = mocker.MagicMock()
        mock_repo.trova.side_effect = [
            {"id": 1, "nome": "Mario",  "stipendio": 1500},
            {"id": 2, "nome": "Luigi",  "stipendio": 2000},
        ]

        servizio = ServizioUtenti(mock_repo)
        assert servizio.get_nome(1) == "Mario"
        assert servizio.get_nome(2) == "Luigi"

        # Verifica che trova sia stato chiamato esattamente 2 volte
        assert mock_repo.trova.call_count == 2
