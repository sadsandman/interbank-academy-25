import typer
from pathlib import Path
from typing import List, Dict
from ptb_cli.utils.io import read_csv
from ptb_cli.utils.dataAnalisis import (
    calcularBalanceFinal,
    calcularTransaccionMontoMayor,
    contarTransaccionesPorTipo,
)

app = typer.Typer()

globalCsvData: List[Dict[str, str]] = []  # inicializacion de variable de archivo csv

@app.callback()
def fetch_data(
    ctx: typer.Context,
    file: str = typer.Option(None, "--file", "-f", help="Ruta del CSV")
):
    
    """
    Inicializa el el la variable globalCsvData
    verificando que el archivo exista
    En todo caso no se use la opcion -f
    finalizara sin cargar el archivo para la ejecuccion del comando HELP
    """
    if ctx.resilient_parsing:
        return

    if file is None:
        typer.secho("Debes especificar un archivo con --file", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    try:
        path = Path(file)
        if not path.exists():
            raise FileNotFoundError(f"El archivo '{file}' no existe.")

        global globalCsvData
        globalCsvData = read_csv(file)
    except (FileNotFoundError, ValueError) as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)


@app.command(name="full-report"
            ,help=("Genera un reporte completo,"
                    "incluyendo balance final, "
                    " Transaccion de mayor monto "
                    "y Conteo de transacciones"))
def full_report():
    """
    Comando que genera un reporte completo  
    Funciones implementadas hasta ahora:
    calcularBalanceFinal,calcularTransaccionMontoMayor, contarTransaccionesPorTipo
    """
    balanceFinal=calcularBalanceFinal(globalCsvData)
    transaccionDeMontoMayor=calcularTransaccionMontoMayor(globalCsvData)
    cantidadDeTransacciones=contarTransaccionesPorTipo(globalCsvData)



    print("Reporte de transacciones")
    print("---------------------------------------------")

    ## Display de balance de transacciones total
    print("Balance Final : ", round(float(balanceFinal),2))

    ## Display de transaccion de mayor monto
    print("Transacción de Mayor Monto: ID "
          ,transaccionDeMontoMayor['id']
          ," - "
          ,round(float(transaccionDeMontoMayor['monto']),2))
    
    ## Display de conteo de transacciones por tipo
    print("Conteo de Transacciones: Crédito: "
          ,cantidadDeTransacciones['crédito']
          ," Débito: "
          ,cantidadDeTransacciones['débito']
          )