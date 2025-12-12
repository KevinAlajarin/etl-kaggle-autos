import pandas as pd
import numpy as np
from etl_pipeline.config import logger

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza la limpieza de datos siguiendo el checklist de calidad.
    """
    try:
        logger.info("Iniciando fase de Limpieza...")
        
        # Copia para evitar SettingWithCopyWarning
        df_clean = df.copy()

        # CHECKLIST 1: Eliminar duplicados
        initial_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        logger.info(f"Duplicados eliminados: {initial_rows - len(df_clean)}")

        # CHECKLIST 2: Estandarización de Nombres de Columnas
        # Limpiamos espacios y pasamos a minúsculas
        df_clean.columns = [col.lower().strip().replace(' ', '_') for col in df_clean.columns]
        
        # --- DEBUG: Imprimir columnas para ver qué está llegando ---
        logger.info(f"Columnas detectadas tras normalización: {df_clean.columns.tolist()}")
        
        # --- FIX: Renombrar variaciones a la norma (American English) ---
        rename_map = {
            'kilometer': 'kilometers',
            'kilometres': 'kilometers',  # <--- AQUÍ ESTÁ EL ARREGLO
            'km': 'kilometers'
        }
        df_clean = df_clean.rename(columns=rename_map)

        # CHECKLIST 3: Tratamiento de Moneda (CRÍTICO)
        df_clean = df_clean.dropna(subset=['money'])
        
        def clean_price(val):
            if isinstance(val, str):
                return float(val.replace('.', '').replace(',', '').replace('$', ''))
            return val

        df_clean['price_numeric'] = df_clean['money'].apply(clean_price)

        # CHECKLIST 4: Normalización de Texto
        text_cols = ['brand', 'model', 'fuel_type', 'gear', 'body_type', 'color']
        for col in text_cols:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].str.strip().str.title()
            else:
                logger.warning(f"La columna de texto '{col}' no se encontró en el dataset.")

        # CHECKLIST 5: Manejo de Nulos
        df_clean[text_cols] = df_clean[text_cols].fillna('Desconocido')
        
        # Finalizando estructura
        # Eliminamos la columna original 'money' y nos quedamos con price_numeric
        df_clean = df_clean.drop(columns=['money'])
        df_clean = df_clean.rename(columns={'price_numeric': 'price'})

        logger.info("Limpieza finalizada.")
        return df_clean

    except Exception as e:
        logger.error(f"Error en Limpieza: {e}")
        raise