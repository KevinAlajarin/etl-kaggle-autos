import pandas as pd
import datetime
from etl_pipeline.config import logger

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("Iniciando fase de Transformacion...")
        df_trans = df.copy()
        
        current_year = datetime.datetime.now().year

        # 1. Antiguedad del vehiculo (Car Age)
        df_trans['car_age'] = current_year - df_trans['year']
        
        # 2. Segmentacion de Precio (Price Range)
        # Calculamos percentiles solo sobre la base en dolares para que tenga sentido,
        # o hacemos un binning genérico. Haremos uno simplificado.
        
        def get_price_segment(row):
            price = row['price']
            currency = row['currency']
            
            # Logica simple para segmentar (ajustar umbrales según mercado real)
            # Asumimos umbrales en USD.
            if currency == 'Dolares':
                if price < 10000: return 'Economico (<10k USD)'
                elif price < 25000: return 'Gama Media (10k-25k USD)'
                elif price < 50000: return 'Gama Alta (25k-50k USD)'
                else: return 'Lujo (>50k USD)'
            else:
                return 'Cotizacion en Pesos (Verificar)'

        df_trans['price_segment'] = df_trans.apply(get_price_segment, axis=1)

        # 3. Clasificacion de Kilometraje
        bins = [0, 20000, 80000, 150000, 1000000]
        labels = ['Nuevo (<20k)', 'Uso Medio (20-80k)', 'Muy Usado (80-150k)', 'Alto Kilometraje (>150k)']
        df_trans['km_category'] = pd.cut(df_trans['kilometers'], bins=bins, labels=labels, right=False)

        # 4. ID Unico para base de datos (si no existe)
        df_trans['sku_id'] = df_trans.index + 1000  # ID sintetico

        logger.info("Transformación finalizada.")
        return df_trans

    except Exception as e:
        logger.error(f"Error en Transformación: {e}")
        raise