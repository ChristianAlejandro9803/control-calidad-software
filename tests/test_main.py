import sys
import os

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import saludar

def test_saludo():
    assert saludar() == "Hola mundo"
