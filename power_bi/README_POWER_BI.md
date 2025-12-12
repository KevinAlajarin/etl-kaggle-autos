# Guía de Construcción Power BI

## 1. Conexión de Datos
El método profesional es conectar directamente a la Base de Datos, no al CSV.

1.  Abre Power BI Desktop.
2.  Clic en **Obtener datos** -> **SQL Server**.
3.  Servidor: `LOCALHOST\SQLEXPRESS` (o tu servidor definido en .env).
4.  Base de datos: `CarSalesDB`.
5.  Modo de conectividad: **Import** (recomendado para este volumen de datos).
6.  Selecciona la tabla `fact_cars` y las vistas `vw_analytics_brand_performance`.

## 2. Modelado
* Verifica que la columna `price` y `kilometers` sean numéricas (decimal/entero).
* Crea una medida DAX para el precio promedio en USD:
    ```DAX
    Avg Price USD = CALCULATE(AVERAGE(fact_cars[price]), fact_cars[currency] = "Dólares")
    ```

## 3. Diseño del Reporte
Utiliza un diseño de grid limpio.

* **Encabezado:** Logo, Título "Análisis Mercado Automotor Arg", Última fecha de actualización.
* **Izquierda (Panel de Filtros):** Slicers para `Brand`, `Body Type`, `Year`.
* **Arriba (Tarjetas KPI):** Usa la medida `Avg Price USD` y `Count Rows`.
* **Centro:** Gráfico de dispersión (Scatter Plot) de Precio vs Km.
* **Abajo:** Gráfico de Barras de `Avg Price USD` por `Brand`.

## 4. Publicación
Guarda el archivo como `Argentina_Car_Analysis.pbix`.