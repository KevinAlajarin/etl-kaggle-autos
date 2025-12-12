-- Ejecutar esto primero en SSMS
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'CarSalesDB')
BEGIN
    CREATE DATABASE CarSalesDB;
END
GO