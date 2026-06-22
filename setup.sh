#!/bin/bash

# ============================================================
# setup.sh — Script per replicare l'ambiente di test
# Tirocinio Interno — Laurea Triennale in Informatica
# Testing di unità in Python: confronto con JUnit 6.0.3
# ============================================================

echo "======================================================"
echo " Setup ambiente di test"
echo "======================================================"

# 1. Verifica che Python 3 sia installato
echo ""
echo "[1/5] Verifica Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "ERRORE: Python 3 non trovato."
    echo "Installalo con: sudo apt install python3 python3-venv"
    exit 1
fi
echo "OK — $(python3 --version)"

# 2. Verifica che python3-venv sia disponibile
echo ""
echo "[2/5] Verifica python3-venv..."
if ! python3 -m venv --help &> /dev/null; then
    echo "ERRORE: python3-venv non trovato."
    echo "Installalo con: sudo apt install python3-venv"
    exit 1
fi
echo "OK"

# 3. Crea il virtual environment
echo ""
echo "[3/5] Creazione virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment già esistente — lo uso"
else
    python3 -m venv venv
    echo "OK — virtual environment creato in ./venv"
fi

# 4. Attiva il venv e installa i pacchetti
echo ""
echo "[4/5] Installazione pacchetti da requirements.txt..."
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo "OK — pacchetti installati:"
pip list | grep -E "pytest|hypothesis|pytest-check"

# 5. Esegui tutti i test per verificare
echo ""
echo "[5/5] Esecuzione di tutti i test..."
echo ""
pytest test/ -v --html=report.html --self-contained-html

echo ""
echo "======================================================"
echo " Setup completato!"
echo ""
echo " Per eseguire i test in futuro:"
echo "   source venv/bin/activate"
echo "   pytest test/ -v"
echo "======================================================"
