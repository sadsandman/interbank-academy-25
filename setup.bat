@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt

echo Entorno virtual activado y dependencias instaladas.
echo Ejecuta el siguiente comando para su verificacion: 
echo .venv\Scripts\python main.py report --file test/data.csv full-report
