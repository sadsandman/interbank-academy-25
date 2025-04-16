import typer
from ptb_cli.commands import report

app = typer.Typer()
app.add_typer(report.app, name="report")

if __name__ == "__main__":
    app()