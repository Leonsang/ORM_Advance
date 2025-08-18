# Proyecto ORM Avanzado

Este proyecto es una demostración de cómo construir un sistema ORM (Object-Relational Mapping) en Python utilizando SQLAlchemy. Permite gestionar objetos de una base de datos de forma sencilla y potente.

## Características

- **Abstracción de la Base de Datos**: Gracias a SQLAlchemy, es fácil cambiar entre diferentes motores de BD (SQLite, PostgreSQL, MySQL, etc.).
- **Gestión de Sesiones**: Utiliza un patrón de sesión para agrupar transacciones y garantizar la integridad de los datos.
- **Patrón Repositorio**: Separa la lógica de acceso a datos de la lógica de negocio.
- **Entorno Virtual con `uv`**: Usa `uv` para una gestión de dependencias y entornos rápida y moderna.

## Cómo Empezar

1.  **Activar el entorno virtual**:
    ```bash
    # En Windows
    .venv\Scripts\activate
    ```
    ```bash
    # En Linux/macOS
    source .venv/bin/activate
    ```

2.  **Instalar dependencias**:
    ```bash
    uv pip install sqlalchemy
    ```

3.  **Ejecutar la demostración**:
    ```bash
    python src/main.py
    ```
