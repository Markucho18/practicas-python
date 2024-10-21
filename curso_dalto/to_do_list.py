# Definir una lista vacía para almacenar las tareas
tareas = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- To-Do List ---")
    print("1. Ver todas las tareas")
    print("2. Agregar una nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Función para ver las tareas
def ver_tareas():
    if len(tareas) == 0:
        print("\nNo hay tareas en la lista.")
    else:
        print("\nLista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. {tarea['descripcion']} [{estado}]")

# Función para agregar una nueva tarea
def agregar_tarea():
    descripcion = input("\nEscribe la descripción de la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    print("Tarea agregada.")

# Función para marcar una tarea como completada
def completar_tarea():
    ver_tareas()
    if len(tareas) > 0:
        numero = int(input("\nElige el número de la tarea que completaste: "))
        if 0 < numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")

# Función para eliminar una tarea
def eliminar_tarea():
    ver_tareas()
    if len(tareas) > 0:
        numero = int(input("\nElige el número de la tarea que deseas eliminar: "))
        if 0 < numero <= len(tareas):
            tareas.pop(numero - 1)
            print("Tarea eliminada.")
        else:
            print("Número de tarea inválido.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("\nSaliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar la función principal
# Comprueba si se esta ejecutando como archivo principal o en segundo plano/como modulo importado
if __name__ == "__main__":
    main()
