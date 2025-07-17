init(autoreset=True)
crear_tabla()
from db import crear_tabla, agregar_producto
from colorama import init, Fore, Style
import sqlite3

init(autoreset=True)
crear_tabla()

print(f"{Fore.CYAN}{Style.BRIGHT} BIENVENIDOS A LA TIENDA DE PRODUCTOS EL BIGUA")

while True:
    print(f"\n{Fore.YELLOW}----- Menú de Productos -----{Style.RESET_ALL}")
    print("1. Agregar Productos")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Eliminar Producto")
    print("5. Actualizar Producto")
    print("6. Salir")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ").title().strip()
        descripcion = input("Descripción: ").strip()
        try:
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio: "))
        except ValueError:
            print(f"{Fore.RED}Cantidad o precio inválido.{Style.RESET_ALL}")
            continue
        categoria = input("Categoría: ").title().strip()
        agregar_producto(nombre, descripcion, cantidad, precio, categoria)
        print(f"{Fore.GREEN}Producto agregado con éxito.{Style.RESET_ALL}")

    elif opcion == "2":
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, categoria, precio FROM productos")
        productos = cursor.fetchall()
        conn.close()

        if not productos:
            print(f"{Fore.YELLOW}No hay productos registrados.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}--- Lista de Productos ---{Style.RESET_ALL}")
            for p in productos:
                print(f"ID: {p[0]}, Nombre: {p[1]}, Categoría: {p[2]}, Precio: ${p[3]:.2f}")

    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ").title().strip()
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, categoria, precio FROM productos WHERE nombre = ?", (nombre,))
        producto = cursor.fetchone()
        conn.close()
        if producto:
            print(f"{Fore.GREEN}Producto encontrado: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]:.2f}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")

    elif opcion == "4":
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM productos")
        productos = cursor.fetchall()

        if not productos:
            print(f"{Fore.YELLOW}No hay productos para eliminar.{Style.RESET_ALL}")
        else:
            for p in productos:
                print(f"ID: {p[0]} - {p[1]}")
            try:
                id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
                cursor.execute("DELETE FROM productos WHERE id = ?", (id_eliminar,))
                conn.commit()
                print(f"{Fore.GREEN}Producto eliminado con éxito.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}ID inválido.{Style.RESET_ALL}")
        conn.close()

    elif opcion == "5":
        try:
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        except ValueError:
            print(f"{Fore.RED}ID inválido.{Style.RESET_ALL}")
            continue

        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(f"{Fore.RED}No existe un producto con ese ID.{Style.RESET_ALL}")
            conn.close()
            continue

        print(f"{Fore.CYAN}Producto actual:{Style.RESET_ALL}")
        print(f"Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

        nombre = input("Nuevo nombre: ").title().strip()
        descripcion = input("Nueva descripción: ").strip()
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        categoria = input("Nueva categoría: ").title().strip()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, id_producto))
        conn.commit()
        conn.close()

        print(f"{Fore.GREEN}Producto actualizado correctamente.{Style.RESET_ALL}")

    elif opcion == "6":
        print(f"{Fore.BLUE}{Style.BRIGHT}Gracias por usar la tienda de EL BIGUA. ¡Hasta pronto!{Style.RESET_ALL}")
        break

    else:
        print(f"{Fore.RED}Opción inválida. Intente nuevamente.{Style.RESET_ALL}")