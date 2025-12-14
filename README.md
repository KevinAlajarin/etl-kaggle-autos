# 🇦🇷 Análisis del Mercado Automotor Argentino

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2019%2B-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)
![ETL](https://img.shields.io/badge/Pipeline-ETL-green)

Un proyecto *End-to-End* de Ingeniería de Datos y Business Intelligence que analiza la depreciación y valoración de vehículos usados en Argentina. El sistema ingesta datos crudos, los procesa y normaliza, los almacena en un Data Warehouse y los visualiza para la toma de decisiones.

## 🏗️ Arquitectura del Proyecto

El flujo de datos sigue una arquitectura lineal robusta:

1.  **Ingesta (Extract):** Lectura de datos crudos (CSV) provenientes de web scraping (Kaggle).
2.  **Procesamiento (Transform):**
    * Limpieza de datos con Pandas (Manejo de nulos, tipado).
    * **Normalización de Moneda:** Separación crítica entre ARS (Pesos) y USD (Dólares).
    * **Reglas de Negocio:** Eliminación de outliers y estandarización de nombres.
3.  **Carga (Load):** Persistencia en **SQL Server** usando SQLAlchemy y ODBC.
4.  **Modelado:** Creación de Vistas SQL (`vw_analytics`) para pre-calcular métricas.
5.  **Visualización:** Dashboard interactivo en **Power BI**.

<img width="1151" height="364" alt="image" src="https://github.com/user-attachments/assets/ac1d8269-db9c-483c-a98d-a7f4eb20d02d" />

### Diagrama de Flujo
```text
[CSV Raw Data] 
      ⬇
(Python ETL Pipeline) ➡ [Validación & Limpieza]
      ⬇
[(SQL Server DB)] 
      ⬇
[Vistas Analíticas] ➡ [Power BI Dashboard]
📂 Estructura del Repositorio
Plaintext

car_sales_dashboard/
├── data/                  # Datos crudos y procesados
├── etl_pipeline/          # Código fuente del ETL (Python)
│   ├── config.py          # Configuración de entorno y logs
│   ├── extract.py         # Módulo de lectura
│   ├── clean.py           # Lógica de limpieza y normalización
│   ├── transform.py       # Enriquecimiento de datos
│   ├── validate.py        # Quality Checks
│   ├── load.py            # Carga a SQL Server
│   └── run_pipeline.py    # Orquestador principal
├── sql_scripts/           # Scripts DDL para SQL Server
├── power_bi/              # Archivo .pbix del Dashboard
├── docs/                  # Documentación adicional
├── requirements.txt       # Dependencias de Python
└── .env.example           # Plantilla de variables de entorno
🚀 Instalación y Ejecución
Prerrequisitos
Python 3.8+

SQL Server (Express, Developer o Enterprise)

Power BI Desktop

1. Configuración del Entorno Python
Bash

# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/car_sales_dashboard.git](https://github.com/TU_USUARIO/car_sales_dashboard.git)
cd car_sales_dashboard

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
2. Configuración de Base de Datos
Crea una copia del archivo .env.example, renómbralo a .env y configura tu string de conexión (DATABASE_URI).

Ejecuta los scripts SQL en tu servidor en el siguiente orden:

sql_scripts/01_create_database.sql

sql_scripts/02_create_tables.sql

3. Ejecución del Pipeline ETL
Este comando ejecutará la extracción, validación y carga de datos:

Bash

python -m etl_pipeline.run_pipeline
Si la ejecución es exitosa, verás los logs indicando la inserción de filas en la DB.

4. Visualización
Ejecuta el script sql_scripts/03_analytical_views.sql para generar las vistas necesarias.

Abre el archivo power_bi/Argentina_Car_Analysis.pbix.

Si es necesario, actualiza el origen de datos (Data Source) apuntando a tu instancia local de SQL Server.

Insights Clave:

Identificación de oportunidades de mercado (Bajo Kilometraje / Precio).

Análisis de depreciación por marca.

Comparativa de segmentos de precios en Dólares.

🛠️ Stack Tecnológico
Lenguaje: Python (Pandas, SQLAlchemy, PyODBC).

Base de Datos: Microsoft SQL Server.

Visualización: Microsoft Power BI (DAX, Data Modeling).

Gestión de Configuración: Dotenv.

Logging: Python Logging estándar.
```

Desarrollado por Kevin ALajarin - 2025
