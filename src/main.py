from .database import create_database, get_db
from .models import Producto
from .repository import (
    create_producto,
    get_productos,
    get_producto,
    update_producto,
    delete_producto,
)

def run_demo():
    """
    Ejecuta una demostración de las funcionalidades del ORM.
    """
    # 1. Crear la base de datos y las tablas
    print("Creando la base de datos y las tablas...")
    create_database()
    print("¡Base de datos creada!")

    # Obtener una sesión de la base de datos
    db_session_generator = get_db()
    db = next(db_session_generator)

    try:
        # 2. Crear nuevos productos
        print("\n--- Creando productos ---")
        p1 = create_producto(db, {"nombre": "Laptop", "descripcion": "Laptop de alto rendimiento", "precio": 1200.50})
        p2 = create_producto(db, {"nombre": "Mouse", "descripcion": "Mouse inalámbrico", "precio": 25.00})
        p3 = create_producto(db, {"nombre": "Teclado", "descripcion": "Teclado mecánico", "precio": 75.99})
        print(f"Creado: {p1.nombre} (ID: {p1.id})")
        print(f"Creado: {p2.nombre} (ID: {p2.id})")
        print(f"Creado: {p3.nombre} (ID: {p3.id})")

        # 3. Consultar todos los productos
        print("\n--- Consultando todos los productos ---")
        todos_los_productos = get_productos(db)
        for p in todos_los_productos:
            print(f"ID: {p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

        # 4. Consultar un producto específico
        print("\n--- Consultando un producto (ID: 1) ---")
        producto_uno = get_producto(db, 1)
        if producto_uno:
            print(f"Encontrado: {producto_uno.nombre}")

        # 5. Actualizar un producto
        print("\n--- Actualizando precio del producto (ID: 1) ---")
        producto_actualizado = update_producto(db, 1, {"precio": 1150.00})
        if producto_actualizado:
            print(f"Actualizado: {producto_actualizado.nombre}, Nuevo Precio: ${producto_actualizado.precio}")

        # 6. Eliminar un producto
        print("\n--- Eliminando producto (ID: 3) ---")
        producto_eliminado = delete_producto(db, 3)
        if producto_eliminado:
            print(f"Eliminado: {producto_eliminado.nombre}")

        # 7. Verificar la lista final de productos
        print("\n--- Lista final de productos ---")
        productos_finales = get_productos(db)
        for p in productos_finales:
            print(f"ID: {p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

    finally:
        # Cerrar la sesión
        print("\nCerrando sesión de la base de datos.")
        db.close()


if __name__ == "__main__":
    run_demo()
