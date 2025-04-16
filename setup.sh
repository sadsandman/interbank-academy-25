python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Entorno virtual activado y dependencias instaladas."
echo "Ejecuta el siguiente comando para su verificacion:"
echo " .venv/bin/python main.py report --file test/data.csv full-report"
