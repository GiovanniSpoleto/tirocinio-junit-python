# Fix applicati a TEMPY (detector.py)

Questo file è `detector.py` del progetto TEMPY (repository originale: https://github.com/danieldavidf/TEMPY),
con due bug corretti durante questo tirocinio.

## Bug 1 — Non-Functional Statement non rilevato dopo "def"
Nella funzione `non_functional_statement`, la condizione originale escludeva erroneamente
il caso in cui `pass` si trova subito dopo la riga `def`. Rimossa la condizione
`and source.content[i-1].find("def ") == -1`.

## Bug 2 — Falso positivo "Unknown Test" con pytest.raises/warns
Nella funzione `how_many_assertions`, non venivano riconosciuti `pytest.raises(...)`
e `pytest.warns(...)` come forme di verifica valide. Aggiunti i controlli corrispondenti.

Fix applicato e verificato il 4/10/2026, commit locale nel repository TEMPY: a448d9e.
Dettagli completi, codice prima/dopo e test di verifica in bug_verificati_tempy.pdf.
