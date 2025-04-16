@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt

echo Entorno virtual activado y dependencias instaladas.
echo Ejecuta el siguiente comando para su verificacion: 
echo .venv\Scripts\python ptb_cli\main.py report --file archivo.csv full-report