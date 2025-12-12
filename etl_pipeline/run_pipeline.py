from etl_pipeline.extract import extract_data
from etl_pipeline.clean import clean_data
from etl_pipeline.validate import validate_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data
from etl_pipeline.config import logger
import time

def run():
    start_time = time.time()
    logger.info(">>> INICIANDO PIPELINE DE DATOS 'ARGENTINA CARS' <<<")
    
    try:
        # Paso 1: Extract
        df_raw = extract_data()
        
        # Paso 2: Clean
        df_clean = clean_data(df_raw)
        
        # Paso 3: Validate
        if validate_data(df_clean):
            # Paso 4: Transform
            df_transformed = transform_data(df_clean)
            
            # Paso 5: Load
            load_data(df_transformed)
            
            logger.info(f">>> PIPELINE FINALIZADO EXITOSAMENTE en {round(time.time() - start_time, 2)} segundos <<<")
        else:
            logger.error("El pipeline se detuvo por fallas en la validacióon.")
            
    except Exception as e:
        logger.critical(f"EL PIPELINE FALLO: {e}")

if __name__ == "__main__":
    run()