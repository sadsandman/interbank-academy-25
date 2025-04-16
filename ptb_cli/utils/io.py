import csv
from pathlib import Path
from typing import List, Dict

def read_csv(filePath: str) -> List[Dict[str,str]]:
    """
    Lee un archivo csv
    filePath: ruta de ubicacion del archivo
    """
    path = Path(filePath)

    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {filePath}")
    
    with path.open(newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
    
