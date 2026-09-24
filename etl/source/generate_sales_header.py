import pandas as pd
import numpy as np


def generar_ventas_cabecera(datos):
    # 1. Establecer la base histórica mensual
    base_mensual = calcular_base_mensual(datos)

    # 2. Estimar el crecimiento histórico
    crecimiento = calcular_crecimiento_historico(datos)

    # 3. Estimar la variabilidad mensual
    variabilidad = calcular_variabilidad_mensual(datos)

    # 4. Simular el volumen diario de ventas
    ventas_diarias = simular_ventas_diarias(
        base_mensual,
        crecimiento,
        variabilidad
    )

    # 5. Construir los registros de ventas sintéticos
    ventas = construir_registros_ventas(
        datos,
        ventas_diarias
    )

    return ventas
