import pandas as pd


def refinar_ventas_detalle(datos, referencias):
    # 1. Validar la calidad de los datos
    reporte_calidad = generar_reporte_calidad(
        datos,
        referencias
    )

    # 2. Eliminar registros duplicados
    datos_refinados = eliminar_duplicados(datos)

    # 3. Validar campos obligatorios
    datos_refinados = validar_campos_obligatorios(
        datos_refinados
    )

    # 4. Normalizar cantidades y valores monetarios
    datos_refinados = normalizar_valores(
        datos_refinados
    )

    # 5. Validar integridad referencial
    datos_refinados = validar_integridad_referencial(
        datos_refinados,
        referencias
    )

    return datos_refinados, reporte_calidad
