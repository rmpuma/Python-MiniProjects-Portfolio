from pathlib import Path
import shutil
import os


def main():
    clear_console()
    print("Bienvenido a tu Recetario")
    # Ruta base donde están las categorías
   # Edita esta ruta para que apunte a la carpeta donde están tus recetas
    carpeta = Path("C:/Users/TuUsuario/Documents/Recetas")

    print(f"Las Recetas estan almacenadas en {carpeta}")

    recetas = []  # Lista vacía para guardar nombres de carpetas
    for archivo in carpeta.rglob("*.txt"):
        if archivo.is_file():
            recetas.append(archivo)

    # Mostrar cantidad total
    print(f"\nTienes {len(recetas)} receta(s) en total.\n")

    while True:
        opcion = input("""
        Elige una de las siguientes opciones:
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoría
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Finalizar programa
                """)

        if opcion == "1":
            read_recipe(carpeta)
        elif opcion == "2":
            create_recipe(carpeta)
        elif opcion == "3":
            create_category(carpeta)
        elif opcion == "4":
            delete_recipe(carpeta)
        elif opcion == "5":
            delete_category(carpeta)
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_recipe(carpeta):
    while True:
        # Obtener todas las categorías (subcarpetas)
        categorias = []
        for c in carpeta.iterdir():
            if c.is_dir():
                categorias.append(c.name)

        # Mostrar categorías disponibles
        print("Categorias disponibles:")
        for cat in categorias:
            print(f"- {cat}")
        name_category = input(
            "Elige la categoria de la receta que deseas leer: ").strip().lower()
        category_path = carpeta / name_category

        if not category_path.exists():
            print("La categoria no existe.")
            continue

        recipes = []
        for r in category_path.iterdir():
            if r.is_file():
                recipes.append(r.name)

        print("Recetas disponibles:")
        for rec in recipes:
            print(f"- {rec}")

        name_recipe = input("Elige la receta que deseas leer: ")
        if name_recipe == "":
            print("El nombre no puede estar vacio")
            continue

        invalid_chars = set('\/:*?"<>|')
        if any(char in invalid_chars for char in name_recipe):
            print("El nombre tiene caracteres no permitidos")
            continue
        recipe_path = category_path / f"{name_recipe}.txt"

        # Leer el archivo si existe
        if recipe_path.exists():
            archivo = open(recipe_path, 'r', encoding='utf-8')
            contenido = archivo.read()
            print(f"\n📖 Contenido de '{name_recipe}.txt':\n")
            print(contenido)
            archivo.close()
            break
        else:
            print("⚠️ La receta no existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("🚫 Operación cancelada.")
                break
            continue

        """ Leer el archivo si existe de forma avanzada
        if recipe_path.exists():
            print(f"\n📖 Contenido de '{name_recipe}.txt':\n")
            with open(recipe_path, 'r', encoding='utf-8') as archivo:
                print(archivo.read())
            break
        else:
            print("⚠️ La receta no existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("🚫 Operación cancelada.")
                break
            continue"""


def create_recipe(carpeta):
    while True:
        # Obtener todas las categorías (subcarpetas)
        categorias = []
        for c in carpeta.iterdir():
            if c.is_dir():
                categorias.append(c.name)

        # Mostrar categorías disponibles
        print("\n📂 Categorías disponibles:")
        for cat in categorias:
            print(f"- {cat}")

        # Solicitar al usuario que elija una categoría
        name_category = input("\n Elige la categoría de tu receta: ").strip()
        categoria_path = carpeta / name_category

        # Validar si la categoría existe
        if not categoria_path.exists():
            print("⚠️ La categoría no existe.")
            continue

        # Pedir nombre para la receta
        name_recipe = input(
            "\n📝 Escribe el nombre de la receta que deseas crear: ").strip()

        # Validar que no esté vacío
        if name_recipe == "":
            print("⚠️ El nombre no puede estar vacío.")
            continue

        # Validar caracteres no permitidos
        invalid_chars = set(r'\/:*?"<>|')
        if any(char in invalid_chars for char in name_recipe):
            print("⚠️ El nombre contiene caracteres no permitidos.")
            continue

        # Crear la ruta completa del archivo de receta
        recipe_path = categoria_path / f"{name_recipe}.txt"

        # Verificar si ya existe
        if recipe_path.exists():
            print(f"\n⚠️ La receta '{name_recipe}' ya existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("🚫 Operación cancelada.")
                break
            continue

        # Capturar contenido de la receta (multi-línea)
        print("\n✏️ Escribe tu receta. Pulsa Enter dos veces para terminar:\n")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        recipe_content = "\n".join(lines)

        # Guardar receta en archivo
        with open(recipe_path, "w", encoding="utf-8") as file:
            file.write(recipe_content)

        print(
            f"\n✅ La receta '{name_recipe}' fue creada correctamente en la categoría '{name_category}'.")

        # Mostrar contenido guardado
        print("\n📄 Contenido de la receta:")
        with open(recipe_path, "r", encoding="utf-8") as file:
            print(file.read())

        # Preguntar si desea modificar algo
        retry = input(
            "\n¿Deseas hacer algún cambio en tu receta? (s para sí / cualquier otra tecla para finalizar): ")
        if retry.lower() != 's':
            print("📁 Receta guardada con éxito.")
            break


def create_category(carpeta):
    while True:
        categorias = []
        for c in carpeta.iterdir():
            if c.is_dir():
                categorias.append(c.name)

        print("\nCategorías disponibles:")
        for cat in categorias:
            print(f"- {cat}")

        name_category = input(
            "\nEscribe el nombre de la categoría que deseas crear: ").strip()

        if name_category == "":
            print("⚠️ El nombre no puede estar vacío.")
            continue

        invalid_chars = set(r'\/:*?"<>|')
        tiene_caracteres_invalidos = False

        for char in name_category:
            if char in invalid_chars:
                tiene_caracteres_invalidos = True
                break

        if tiene_caracteres_invalidos:
            print("⚠️ El nombre contiene caracteres no permitidos.")
            continue

        categoria_path = carpeta / name_category

        if categoria_path.exists() and categoria_path.is_dir():
            print(f"\nLa categoría '{name_category}' ya existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("Operación cancelada.")
                break
        else:
            categoria_path.mkdir()
            print(
                f"\n✅ La categoría '{name_category}' fue creada correctamente.")
            break


def delete_recipe(carpeta):
    while True:
        # Recorremos los elementos de la carpeta y filtramos solo las carpetas
        categorias = []  # Lista vacía para guardar nombres de carpetas
        for c in carpeta.iterdir():
            if c.is_dir():
                categorias.append(c.name)

        # Verificamos si hay categorias
        if not categorias:
            print("No existen categorías.")
            break

        # Mostramos las categorías disponibles
        print("\nCategorías disponibles:")
        for cat in categorias:
            print(f"- {cat}")

        # ⌨Pedimos al usuario un nombre
        name_category = input(
            "\nEscribe el nombre de la categoría en la que se encuentra la receta que deseas eliminar: ")
        categoria_path = carpeta / name_category

        if not categoria_path.exists() or not categoria_path.is_dir():
            print(f"⚠️ La categoría '{name_category}' no existe.")
            continue

        recetas = []
        for archivo in categoria_path.iterdir():
            if archivo.is_file() and archivo.suffix == ".txt":
                recetas.append(archivo.stem)

        if not recetas:
            print(f"La categoría '{name_category}' no contiene recetas.")
            continue

        print("\nRecetas disponibles en esta categoría:")
        for r in recetas:
            print(f"- {r}")

        # Pedir nombre para la receta
        name_recipe = input(
            "\n📝 Escribe el nombre de la receta que deseas eliminar: ").strip().lower()

        # Validar que no esté vacío
        if name_recipe == "":
            print("⚠️ El nombre no puede estar vacío.")
            continue

        # Validar caracteres no permitidos
        invalid_chars = set('\/:*?"<>|')
        if any(char in invalid_chars for char in name_recipe):
            print("⚠️ El nombre contiene caracteres no permitidos.")
            continue

        # Crear la ruta completa del archivo de receta
        recipe_path = categoria_path / f"{name_recipe}.txt"

        # Verificamos si la receta existe
        if recipe_path.exists():
            confirm = input(
                f"¿Estás seguro que deseas eliminar la receta '{name_recipe}'? (s/n): ")
            if confirm.lower() == 's':
                recipe_path.unlink()
                print(f"Receta '{recipe_path}' eliminada.")
                break
            else:
                print("Operación cancelada.")
                break
        else:
            # La receta no existe: opción de reintentar o salir
            print(f"\nLa receta '{recipe_path}' no existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("Operación cancelada.")
                break


def delete_category(carpeta):
    while True:
        # Recorremos los elementos de la carpeta y filtramos solo las carpetas
        categorias = []  # Lista vacía para guardar nombres de carpetas
        for c in carpeta.iterdir():
            if c.is_dir():
                categorias.append(c.name)

        # Verificamos si hay algo que eliminar
        if not categorias:
            print("No hay categorías para eliminar.")
            break

        # Mostramos las categorías disponibles
        print("\nCategorías disponibles:")
        for cat in categorias:
            print(f"- {cat}")

        # ⌨Pedimos al usuario un nombre
        name_category = input(
            "\nEscribe el nombre de la categoría que deseas eliminar: ")
        categoria_path = carpeta / name_category

        # Verificamos si la ruta existe y es carpeta
        if categoria_path.exists() and categoria_path.is_dir():
            if not any(categoria_path.iterdir()):
                # Carpeta vacía: usar rmdir()
                confirm = input(
                    f"La categoría '{name_category}' está vacía. ¿Deseas eliminarla? (s/n): ")
                if confirm.lower() == 's':
                    categoria_path.rmdir()
                    print(f"Categoría '{name_category}' eliminada.")
                    break
                else:
                    print("Operación cancelada.")
                    break
            else:
                # Carpeta con contenido: usar rmtree()
                confirm = input(
                    f"La categoría '{name_category}' contiene archivos. ¿Eliminar todo su contenido? (s/n): ")
                if confirm.lower() == 's':
                    shutil.rmtree(categoria_path)
                    print(
                        f"Categoría '{name_category}' eliminada con todo su contenido.")
                    break
                else:
                    print("Operación cancelada.")
                    break
        else:
            # La carpeta no existe: opción de reintentar o salir
            print(f"\nLa categoría '{name_category}' no existe.")
            retry = input(
                "¿Deseas intentar con otro nombre? (s para sí / cualquier otra tecla para cancelar): ")
            if retry.lower() != 's':
                print("Operación cancelada.")
                break


main()
