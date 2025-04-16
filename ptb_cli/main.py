import typer
from typing import List,Dict
from ptb_cli.commands import report
from ptb_cli.utils.io import read_csv

app = typer.Typer()

@app.callback()
def fecth_data(file: str = typer.Option(..., "--file", "-f", help="Ruta del CSV")):
    """
    Carga el archivo csv 
    """
    try:
        globalCsvData = read_csv(file)
        report.set_data(globalCsvData)  # Carga la data en report.py
    except FileNotFoundError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=2)


app.add_typer(report.app, name="report")

if __name__ == "__main__":
    app()
