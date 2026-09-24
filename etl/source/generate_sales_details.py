import pandas as pd


def generar_ventas_detalle(cabeceras, detalles_referencia):
    # 1. Identificar las ventas generadas recientemente
    nuevas_ventas = identificar_nuevas_ventas(cabeceras)

    # 2. Seleccionar registros representativos de detalle
    detalles_muestra = seleccionar_detalles_referencia(
        detalles_referencia
    )

    # 3. Asociar la información de detalle con las nuevas ventas
    ventas_detalle = asociar_detalles(
        nuevas_ventas,
        detalles_muestra
    )

    # 4. Validar que los identificadores generados no estén duplicados
    validar_ids_unicos(ventas_detalle)

    return ventas_detalle
