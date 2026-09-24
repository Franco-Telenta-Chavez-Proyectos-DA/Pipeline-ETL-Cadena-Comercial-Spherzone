import pandas as pd
import numpy as np


def generate_sales_header(data):
    # 1. Determinar historico base de ventas
    monthly_base = calculate_monthly_baseline(data)

    # 2. Estima crecimiento histórico
    growth = calculate_historical_growth(data)

    # 3. Estima variabilidad mensual
    variability = calculate_monthly_variability(data)

    # 4. Generar ventas diarias acorde a los patrones históricos
    daily_sales = simulate_daily_sales(
        monthly_base,
        growth,
        variability
    )

    # 5. Crear registros sintéticos de transacciones
    return build_sales_records(data, daily_sales)
