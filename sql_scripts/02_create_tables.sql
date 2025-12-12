USE CarSalesDB;
GO

IF EXISTS (SELECT * FROM sys.tables WHERE name = 'fact_cars')
DROP TABLE fact_cars;
GO

CREATE TABLE fact_cars (
    sku_id BIGINT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(100),
    year INT,
    color VARCHAR(50),
    fuel_type VARCHAR(30),
    door INT,
    gear VARCHAR(30),
    motor VARCHAR(100),
    body_type VARCHAR(50),
    kilometers INT,
    currency VARCHAR(20),
    price DECIMAL(18, 2),
    car_age INT,
    price_segment VARCHAR(50),
    km_category VARCHAR(50)
);
GO