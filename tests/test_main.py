import sys
import os

# Añadir la carpeta 'app' al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app.saludo import saludar

def test_saludo():
    assert saludar() == "Hola mundo"
#SOLO ES UN COMENTARIO PARA GUARDAR LOS CAMBIOS...