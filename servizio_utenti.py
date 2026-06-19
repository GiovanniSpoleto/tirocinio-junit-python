class DatabaseError(Exception):
    pass

class UtenteRepository:
    """Rappresenta un repository che legge dal database reale."""

    def trova(self, id_utente):
        # In produzione si connetterebbe al database
        raise NotImplementedError("Connessione al database reale")

    def salva(self, utente):
        raise NotImplementedError("Scrittura sul database reale")


class ServizioUtenti:
    """Servizio che usa il repository — questo è il codice da testare."""

    def __init__(self, repository):
        self.repository = repository

    def get_nome(self, id_utente):
        utente = self.repository.trova(id_utente)
        return utente["nome"]

    def get_stipendio(self, id_utente):
        utente = self.repository.trova(id_utente)
        return utente["stipendio"]

    def salva_utente(self, id_utente, nome, stipendio):
        utente = {"id": id_utente, "nome": nome, "stipendio": stipendio}
        self.repository.salva(utente)
        return True
