from typing import List, Dict
from collections import Counter

def calcularBalanceFinal(globalCsvData: List[Dict[str, str]]):
    """
    Devuelve el balance total de las transacciones del archivo csv, 
    considerando que el credito es positivo, y debito negativo
    """
    balanceFinal=0

    for row in globalCsvData:
        
        tipo = row.get("tipo","").strip().lower()
        
        if "crédito" in tipo:
            monto=float(row.get("monto", 0))
        elif "débito" in tipo:
            monto=float(row.get("monto", 0))*-1
        
        balanceFinal+=monto

    return balanceFinal

def calcularTransaccionMontoMayor(globalCsvData: List[Dict[str, str]]):
    """
    Calcula el valor maximo de transaccion con su id respectivo
    """

    return max(globalCsvData
               ,key=lambda row: float(row.get("monto", "0").replace(",", "").strip())
               )


def contarTransaccionesPorTipo(globalCsvData: List[Dict[str, str]]):
    """
    Cuenta el numero de transacciones de cada tipo
    """
    tipos = [row.get("tipo", "Desconocido").strip().lower() for row in globalCsvData]
    return Counter(tipos)
