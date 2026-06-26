#!/bin/bash
cd "$(dirname "$0")"

echo "Installerer avhengigheter..."
pip install -q -r requirements.txt

echo ""
echo "========================================="
echo " Kommunal Beredskapsmodul – PoC"
echo " Åpne http://localhost:8000 i nettleseren"
echo "========================================="
echo ""

python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
