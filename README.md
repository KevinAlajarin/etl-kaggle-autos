# 🚗 Argentina Car Sales Dashboard

Este proyecto implementa un flujo de trabajo de Inteligencia de Negocios (BI) completo para analizar el mercado automotor argentino.

## 🏗 Arquitectura
1.  **ETL (Python):** Extracción, limpieza y enriquecimiento de datos con Pandas.
2.  **Data Warehouse (SQL Server):** Almacenamiento estructurado y vistas analíticas.
3.  **Visualización (Power BI):** Dashboard interactivo para la toma de decisiones.

## 🚀 Cómo Ejecutar el Proyecto

### 1. Configuración del Entorno
* Instala Python 3.10+
* Crea un entorno virtual: `python -m venv venv`
* Activa el entorno e instala dependencias:
    ```bash
    pip install -r requirements.txt
    ```
* Configura las variables de entorno:
    * Renombra `.env.example` a `.env`.
    * Edita `.env` con tus credenciales de SQL Server.

### 2. Base de Datos
* Abre SQL Server Management Studio (SSMS).
* Ejecuta `sql_scripts/01_create_database.sql`.

### 3. Ejecución del ETL
* Desde la terminal, en la raíz del proyecto:
    ```bash
    python -m etl_pipeline.run_pipeline
    ```
* Verifica los logs en la consola o en `etl_pipeline.log`.
* Verifica que la tabla `fact_cars` se haya creado en SQL Server.

### 4. Vistas SQL
* Ejecuta `sql_scripts/03_analytical_views.sql` en SSMS para generar las tablas virtuales para Power BI.

### 5. Power BI
* Sigue las instrucciones en `power_bi/README_POWER_BI.md`.