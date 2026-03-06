"""
Programa principal del gestor de tareas.

Este módulo contiene el menú principal que permite al usuario
interactuar con el sistema de gestión de tareas.
"""

from tareas import (
    cargar_tareas,
    guardar_tareas,
    agregar_tarea,
    listar_tareas,
    completar_tarea,
    eliminar_tarea
)



def menu():
    """Muestra el menú principal del programa."""
    
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    """Función principal del programa."""
    
    tareas = cargar_tareas()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                listar_tareas(tareas)

            elif opcion == "2":
                descripcion = input("Ingrese descripción de la tarea: ")
                agregar_tarea(tareas, descripcion)

            elif opcion == "3":
                indice = int(input("Número de tarea a completar: "))
                completar_tarea(tareas, indice)

            elif opcion == "4":
                indice = int(input("Número de tarea a eliminar: "))
                eliminar_tarea(tareas, indice)

            elif opcion == "5":
                guardar_tareas(tareas)
                print("Tareas guardadas. ¡Hasta luego!")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número válido.")

        except IndexError:
            print("La tarea indicada no existe.")


if __name__ == "__main__":
    main()