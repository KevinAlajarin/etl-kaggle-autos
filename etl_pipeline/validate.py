import pandas as pd
from etl_pipeline.config import logger

def validate_data(df: pd.DataFrame) -> bool:
    try:
        logger.info("Iniciando fase de Validacion...")
        
        # REGLA 1: No puede haber precios negativos o cero
        invalid_prices = df[df['price'] <= 0]
        if not invalid_prices.empty:
            logger.warning(f"Se detectaron {len(invalid_prices)} registros con precio <= 0. Se van a descartar.")
            # En un entorno estricto, esto podría detener el pipeline. Aquí filtramos.
            df.drop(invalid_prices.index, inplace=True)

        # REGLA 2: No puede haber años futuros
        # Dejamos un margen de error por modelos 2024 lanzados en 2023
        invalid_years = df[df['year'] > 2025] 
        if not invalid_years.empty:
            logger.warning(f"Se detectaron {len(invalid_years)} registros con año futuro improbable.")
            df.drop(invalid_years.index, inplace=True)

        # REGLA 3: Kilometraje no negativo
        if (df['kilometers'] < 0).any():
             logger.error("Existen kilómetros negativos.")
             return False

        logger.info("Validacion completada.")
        return True # Retorna True si paso (o se corrigio) todo lo critico

    except Exception as e:
        logger.error(f"Error en Validacion: {e}")
        raise