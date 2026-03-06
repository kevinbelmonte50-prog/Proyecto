"""
Módulo para gestionar las tareas.
"""

import json
from tabulate import tabulate


ARCHIVO = "data.json"


def cargar_tareas():
    """Carga las tareas desde un archivo JSON."""
    
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except:
        return []


def guardar_tareas(tareas):
    """Guarda las tareas en un archivo JSON."""
    
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)


def agregar_tarea(tareas, descripcion):
    """Agrega una nueva tarea."""
    
    tareas.append({
        "descripcion": descripcion,
        "completada": False
    })


def listar_tareas(tareas):
    """Muestra todas las tareas."""
    
    tabla = []

    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else "Pendiente"
        tabla.append([i, tarea["descripcion"], estado])

    print(tabulate(tabla, headers=["ID", "Tarea", "Estado"]))


def completar_tarea(tareas, indice):
    """Marca una tarea como completada."""
    
    tareas[indice]["completada"] = True


def eliminar_tarea(tareas, indice):
    """Elimina una tarea."""
    
    tareas.pop(indice)