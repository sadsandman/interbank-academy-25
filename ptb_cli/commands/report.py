import typer
from ptb_cli.utils.io import read_csv
from ptb_cli.utils.dataAnalisis import (calcularBalanceFinal
                                        ,calcularTransaccionMontoMayor
                                        ,contarTransaccionesPorTipo
                                        )
from typing import List, Dict

app = typer.Typer()

globalCsvData: List[Dict[str, str]] = []

def set_data(data):
    global globalCsvData
    globalCsvData = data



@app.command(name="full-report"
            ,help=("Genera un reporte completo,"
                    "incluyendo balance final, "
                    " Transaccion de mayor monto "
                    "y Conteo de transacciones"))
def full_report():
    """
    Comando que genera un reporte completo 
    """
    balanceFinal=calcularBalanceFinal(globalCsvData)
    transaccionDeMontoMayor=calcularTransaccionMontoMayor(globalCsvData)
    cantidadDeTransacciones=contarTransaccionesPorTipo(globalCsvData)
    print(balanceFinal)
    print(transaccionDeMontoMayor)
    print(cantidadDeTransacciones)
    