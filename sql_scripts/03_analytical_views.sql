USE CarSalesDB;
GO

-- VISTA 1: Análisis de Precios Promedio por Marca (Solo Dolares para consistencia)
CREATE OR ALTER VIEW vw_analytics_brand_performance AS
SELECT 
    brand,
    COUNT(*) as total_cars_listed,
    AVG(price) as avg_price_usd,
    MIN(price) as min_price_usd,
    MAX(price) as max_price_usd,
    AVG(car_age) as avg_age_years
FROM fact_cars
WHERE currency = 'Dolares'
GROUP BY brand;
GO

-- VISTA 2: Depreciacion (Año vs Precio)
CREATE OR ALTER VIEW vw_analytics_depreciation AS
SELECT 
    year,
    car_age,
    AVG(price) as avg_price_usd,
    AVG(kilometers) as avg_kilometers
FROM fact_cars
WHERE currency = 'Dolares'
GROUP BY year, car_age;
GO