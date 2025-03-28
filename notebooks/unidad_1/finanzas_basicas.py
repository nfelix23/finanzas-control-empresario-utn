import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def valor_futuro(va, tasa, periodos):
    """
    Calcula el valor futuro de una inversión
    
    Parámetros:
    va (float): Valor actual o inversión inicial
    tasa (float): Tasa de interés (en decimales, ej: 0.10 para 10%)
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor futuro
    """
    return va * (1 + tasa) ** periodos

def valor_actual(vf, tasa, periodos):
    """
    Calcula el valor actual de un monto futuro
    
    Parámetros:
    vf (float): Valor futuro
    tasa (float): Tasa de interés (en decimales)
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor actual
    """
    return vf / (1 + tasa) ** periodos

def va_anualidad_ordinaria(pago, tasa, periodos):
    """
    Calcula el valor actual de una anualidad ordinaria
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor actual de la anualidad
    """
    return pago * (1 - (1 + tasa) ** -periodos) / tasa

def va_anualidad_adelantada(pago, tasa, periodos):
    """
    Calcula el valor actual de una anualidad adelantada
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor actual de la anualidad
    """
    return va_anualidad_ordinaria(pago, tasa, periodos) * (1 + tasa)

def va_anualidad_diferida(pago, tasa, periodos, periodos_gracia):
    """
    Calcula el valor actual de una anualidad diferida
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    periodos (int): Número de períodos de la anualidad
    periodos_gracia (int): Número de períodos de gracia antes del primer pago
    
    Retorna:
    float: Valor actual de la anualidad diferida
    """
    va = va_anualidad_ordinaria(pago, tasa, periodos)
    return va / (1 + tasa) ** periodos_gracia

def va_perpetuidad(pago, tasa):
    """
    Calcula el valor actual de una perpetuidad
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    
    Retorna:
    float: Valor actual de la perpetuidad
    """
    return pago / tasa

def vf_anualidad_ordinaria(pago, tasa, periodos):
    """
    Calcula el valor futuro de una anualidad ordinaria
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor futuro de la anualidad
    """
    return pago * ((1 + tasa) ** periodos - 1) / tasa

def vf_anualidad_adelantada(pago, tasa, periodos):
    """
    Calcula el valor futuro de una anualidad adelantada
    
    Parámetros:
    pago (float): Pago periódico
    tasa (float): Tasa de interés por período
    periodos (int): Número de períodos
    
    Retorna:
    float: Valor futuro de la anualidad adelantada
    """
    return vf_anualidad_ordinaria(pago, tasa, periodos) * (1 + tasa)

def tna_a_tea(tna, capitalizaciones_por_anio):
    """
    Convierte Tasa Nominal Anual a Tasa Efectiva Anual
    
    Parámetros:
    tna (float): Tasa Nominal Anual (en decimales)
    capitalizaciones_por_anio (int): Número de capitalizaciones por año
    
    Retorna:
    float: Tasa Efectiva Anual
    """
    return (1 + tna/capitalizaciones_por_anio) ** capitalizaciones_por_anio - 1

def tea_a_tna(tea, capitalizaciones_por_anio):
    """
    Convierte Tasa Efectiva Anual a Tasa Nominal Anual
    
    Parámetros:
    tea (float): Tasa Efectiva Anual (en decimales)
    capitalizaciones_por_anio (int): Número de capitalizaciones por año
    
    Retorna:
    float: Tasa Nominal Anual
    """
    return capitalizaciones_por_anio * ((1 + tea) ** (1/capitalizaciones_por_anio) - 1)

def tasa_real(tasa_nominal, inflacion):
    """
    Calcula la tasa real usando la fórmula de Fisher
    
    Parámetros:
    tasa_nominal (float): Tasa nominal (en decimales)
    inflacion (float): Tasa de inflación (en decimales)
    
    Retorna:
    float: Tasa real
    """
    return (1 + tasa_nominal) / (1 + inflacion) - 1

def convertir_tasa_efectiva(tasa_efectiva, periodo_origen, periodo_destino):
    """
    Convierte una tasa efectiva de un período a otro
    
    Parámetros:
    tasa_efectiva (float): Tasa efectiva para el período de origen
    periodo_origen (int): Número de períodos de origen en un año (ej: 1 para anual, 12 para mensual)
    periodo_destino (int): Número de períodos de destino en un año
    
    Retorna:
    float: Tasa efectiva para el período de destino
    """
    # Primero convertir a tasa efectiva anual
    tea = (1 + tasa_efectiva) ** periodo_origen - 1
    
    # Luego convertir de TEA a tasa efectiva del período destino
    return (1 + tea) ** (1 / periodo_destino) - 1

def graficar_crecimiento(va, tasa_anual, meses):
    """
    Grafica el crecimiento de una inversión a lo largo del tiempo
    
    Parámetros:
    va (float): Valor actual o inversión inicial
    tasa_anual (float): Tasa anual (en decimales)
    meses (int): Duración en meses
    
    Retorna:
    matplotlib.pyplot: Objeto de gráfico
    """
    tasa_mensual = (1 + tasa_anual) ** (1/12) - 1
    periodos = np.arange(meses + 1)
    valores = [valor_futuro(va, tasa_mensual, p) for p in periodos]
    
    plt.figure(figsize=(10, 6))
    plt.plot(periodos, valores, 'b-', label='Valor de la inversión')
    plt.title('Crecimiento de la Inversión a lo largo del tiempo')
    plt.xlabel('Meses')
    plt.ylabel('Valor ($)')
    plt.grid(True)
    plt.legend()
    return plt
