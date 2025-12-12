import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno
load_dotenv()

# Rutas Base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = BASE_DIR / "data" / "raw" / "argentina_cars.csv"
DATA_PROCESSED = BASE_DIR / "data" / "processed" / "cars_cleaned.csv"

# Configuracion de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("etl_pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ETL_Core")

# Configuracion de DB 
class DBConfig:
    CONNECTION_STRING = os.getenv("DATABASE_URI")
    
    @classmethod
    def get_connection_string(cls):
        if not cls.CONNECTION_STRING:
            raise ValueError("La variable DATABASE_URI no esta definida en el archivo .env")
        return cls.CONNECTION_STRING