import pandas as pd
from pathlib import Path

def cargarData(archivo) -> pd.DataFrame:
    """Lee pasamos el nombre del archivo."""
    cwd = Path.cwd() # Ruta principal
    ROOT = cwd.parent   # sube de notebooks/ a la raíz
    file_path = ROOT / 'data' / 'raw' / archivo

    return pd.read_excel(file_path)