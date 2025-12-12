import pandas as pd
from etl_pipeline.config import logger, DATA_RAW

def extract_data() -> pd.DataFrame:
    try:
        logger.info("Iniciando fase de Extraccion...")
        if not DATA_RAW.exists():
            raise FileNotFoundError(f"No se encontro el archivo en {DATA_RAW}")
        
        df = pd.read_csv(DATA_RAW)
        logger.info(f"Extraccion exitosa. Filas leidas: {len(df)}")
        return df
    except Exception as e:
        logger.error(f"Error en Extraccion: {e}")
        raise