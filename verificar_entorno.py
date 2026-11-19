"""Muestra la versión de Python y de las librerías del proyecto, para la evidencia de entorno instalado."""
import platform
import shutil
import sys
from datetime import datetime
from importlib import metadata

LIBRERIAS = ["fastapi", "uvicorn", "pandas", "pysentimiento", "python-dotenv", "psycopg2-binary", "bcrypt"]
print("ReseñAI - verificación del entorno")
print("Fecha:", datetime.now().strftime("%d/%m/%Y %H:%M"))
print("Python:", sys.version.split()[0], "|", platform.system(), platform.release())
print("Entorno virtual activo:", "sí" if sys.prefix != getattr(sys, "base_prefix", sys.prefix) else "no")
print("Git instalado:", "sí" if shutil.which("git") else "no")
faltan = 0
for lib in LIBRERIAS:
    try:
        print(f"  {lib:<18} {metadata.version(lib)}")
    except metadata.PackageNotFoundError:
        print(f"  {lib:<18} NO INSTALADA")
        faltan += 1
print("Resultado:", "entorno listo" if faltan == 0 else f"faltan {faltan} librerías: ejecute pip install -r requirements.txt")
