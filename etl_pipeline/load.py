import pandas as pd
from sqlalchemy import create_engine, types
from etl_pipeline.config import logger, DBConfig, DATA_PROCESSED

def load_data(df: pd.DataFrame):
    try:
        logger.info("Iniciando fase de Carga (Load)...")

        # 1. Carga a CSV
        df.to_csv(DATA_PROCESSED, index=False, encoding='utf-8')
        logger.info(f"CSV procesado guardado en: {DATA_PROCESSED}")

        # 2. Carga a SQL Server
        conn_str = DBConfig.get_connection_string()
        engine = create_engine(conn_str)

        # Definir tipos de datos explicitos para SQL mejora performance y seguridad
        dtype_mapping = {
            'brand': types.VARCHAR(50),
            'model': types.VARCHAR(100),
            'currency': types.VARCHAR(20),
            'fuel_type': types.VARCHAR(30),
            'gear': types.VARCHAR(30),
            'body_type': types.VARCHAR(50),
            'price_segment': types.VARCHAR(50),
            'km_category': types.VARCHAR(50)
        }

        # 'replace' borrara la tabla y la creara de nuevo. 
        df.to_sql('fact_cars', con=engine, if_exists='replace', index=False, schema='dbo', dtype=dtype_mapping)
        
        logger.info("Carga a SQL Server (tabla: fact_cars) exitosa.")

    except Exception as e:
        logger.error(f"Error en Carga: {e}")
        raise