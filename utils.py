"""
Funciones auxiliares del programa.
"""

import os


def limpiar_pantalla():
    """Limpia la consola."""
    
    os.system("cls" if os.name == "nt" else "clear")