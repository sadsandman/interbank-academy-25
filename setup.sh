python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Entorno virtual activado y dependencias instaladas."
echo "Ejecuta el siguiente comando para su verificacion:
     .venv/bin/python ptb_cli/main.py report --file archivo.csv full-report"
