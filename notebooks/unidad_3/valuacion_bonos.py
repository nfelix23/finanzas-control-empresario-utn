"""
Módulo de Valuación de Bonos
Universidad Tecnológica Nacional - Facultad Regional La Plata
Finanzas y Control Empresario - Ingeniería Industrial

Este módulo contiene funciones para la valuación y análisis de bonos,
incluyendo cálculos de precio, rendimiento, duración y convexidad.

Autor: Prof. Esp. en Finanzas Cuantitativas
Fecha: 2025
"""

import numpy as np
import pandas as pd
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings('ignore')


class Bono:
    """
    Clase para representar y analizar bonos.
    
    Atributos:
    ----------
    valor_nominal : float
        Valor nominal del bono
    tasa_cupon : float
        Tasa de cupón anual (como decimal)
    años_vencimiento : int
        Años hasta el vencimiento
    frecuencia : int
        Frecuencia de pagos por año (1=anual, 2=semestral, etc.)
    """
    
    def __init__(self, valor_nominal, tasa_cupon, años_vencimiento, frecuencia=1):
        self.valor_nominal = valor_nominal
        self.tasa_cupon = tasa_cupon
        self.años_vencimiento = años_vencimiento
        self.frecuencia = frecuencia
        
    def precio(self, rendimiento):
        """Calcula el precio del bono dado un rendimiento."""
        return precio_bono(self.valor_nominal, self.tasa_cupon, 
                          self.años_vencimiento, rendimiento, self.frecuencia)
    
    def ytm(self, precio_mercado):
        """Calcula el rendimiento al vencimiento dado un precio de mercado."""
        return rendimiento_al_vencimiento(precio_mercado, self.valor_nominal,
                                        self.tasa_cupon, self.años_vencimiento, 
                                        self.frecuencia)
    
    def duracion_macaulay(self, rendimiento):
        """Calcula la duración de Macaulay."""
        return duracion_macaulay(self.valor_nominal, self.tasa_cupon,
                                self.años_vencimiento, rendimiento, self.frecuencia)
    
    def duracion_modificada(self, rendimiento):
        """Calcula la duración modificada."""
        return duracion_modificada(self.valor_nominal, self.tasa_cupon,
                                  self.años_vencimiento, rendimiento, self.frecuencia)
    
    def convexidad(self, rendimiento):
        """Calcula la convexidad."""
        return convexidad(self.valor_nominal, self.tasa_cupon,
                         self.años_vencimiento, rendimiento, self.frecuencia)


def precio_bono(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia=1):
    """
    Calcula el precio de un bono con cupones periódicos.
    
    Parámetros:
    -----------
    valor_nominal : float
        Valor nominal del bono (principal)
    tasa_cupon : float
        Tasa de cupón anual (como decimal, ej: 0.05 para 5%)
    periodos : int
        Número de años hasta el vencimiento
    rendimiento : float
        Rendimiento requerido (como decimal)
    frecuencia : int, default=1
        Frecuencia de pagos por año (1=anual, 2=semestral, 4=trimestral)
    
    Retorna:
    --------
    float
        Precio del bono
    
    Ejemplo:
    --------
    >>> precio_bono(1000, 0.08, 5, 0.10)
    924.18
    """
    if periodos <= 0:
        raise ValueError("Los períodos deben ser positivos")
    if rendimiento < 0:
        raise ValueError("El rendimiento no puede ser negativo")
    if frecuencia <= 0:
        raise ValueError("La frecuencia debe ser positiva")
    
    # Ajustar parámetros por frecuencia
    cupon_periodo = (tasa_cupon * valor_nominal) / frecuencia
    rendimiento_periodo = rendimiento / frecuencia
    num_periodos = periodos * frecuencia
    
    # Calcular valor presente de cupones
    if rendimiento_periodo == 0:
        vp_cupones = cupon_periodo * num_periodos
    else:
        # Fórmula de anualidad
        vp_cupones = cupon_periodo * (1 - (1 + rendimiento_periodo)**(-num_periodos)) / rendimiento_periodo
    
    # Calcular valor presente del principal
    vp_principal = valor_nominal / (1 + rendimiento_periodo)**num_periodos
    
    return vp_cupones + vp_principal


def rendimiento_al_vencimiento(precio_mercado, valor_nominal, tasa_cupon, periodos, frecuencia=1):
    """
    Calcula el rendimiento al vencimiento (YTM) de un bono.
    Utiliza método numérico para encontrar la tasa que iguala el precio calculado al precio de mercado.
    
    Parámetros:
    -----------
    precio_mercado : float
        Precio actual del bono en el mercado
    valor_nominal : float
        Valor nominal del bono
    tasa_cupon : float
        Tasa de cupón anual
    periodos : int
        Años hasta el vencimiento
    frecuencia : int
        Frecuencia de pagos por año
    
    Retorna:
    --------
    float
        Rendimiento al vencimiento anualizado
    
    Ejemplo:
    --------
    >>> rendimiento_al_vencimiento(950, 1000, 0.08, 5)
    0.0906
    """
    def ecuacion_precio(ytm):
        return precio_bono(valor_nominal, tasa_cupon, periodos, ytm, frecuencia) - precio_mercado
    
    try:
        # Estimación inicial del YTM basada en la fórmula aproximada
        ytm_inicial = (tasa_cupon * valor_nominal + (valor_nominal - precio_mercado) / periodos) / \
                     ((valor_nominal + precio_mercado) / 2)
        
        # Resolver la ecuación numéricamente
        ytm = fsolve(ecuacion_precio, ytm_inicial)[0]
        
        # Verificar que la solución es válida
        if ytm < 0:
            raise ValueError("YTM negativo encontrado")
            
        return ytm
    except Exception as e:
        print(f"Error calculando YTM: {e}")
        return None


def duracion_macaulay(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia=1):
    """
    Calcula la duración de Macaulay de un bono.
    
    La duración de Macaulay es el tiempo promedio ponderado hasta recibir los flujos de efectivo.
    
    Parámetros:
    -----------
    valor_nominal : float
        Valor nominal del bono
    tasa_cupon : float
        Tasa de cupón anual
    periodos : int
        Años hasta el vencimiento
    rendimiento : float
        Rendimiento del bono
    frecuencia : int
        Frecuencia de pagos por año
    
    Retorna:
    --------
    float
        Duración de Macaulay en años
    """
    cupon_periodo = (tasa_cupon * valor_nominal) / frecuencia
    rendimiento_periodo = rendimiento / frecuencia
    num_periodos = periodos * frecuencia
    
    precio = precio_bono(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia)
    
    suma_ponderada = 0
    
    # Calcular la suma ponderada de los tiempos de los flujos
    for t in range(1, num_periodos + 1):
        if t < num_periodos:
            flujo = cupon_periodo
        else:
            flujo = cupon_periodo + valor_nominal  # Último período incluye principal
        
        vp_flujo = flujo / (1 + rendimiento_periodo)**t
        suma_ponderada += (t / frecuencia) * vp_flujo  # Convertir períodos a años
    
    return suma_ponderada / precio


def duracion_modificada(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia=1):
    """
    Calcula la duración modificada de un bono.
    
    La duración modificada mide la sensibilidad del precio del bono 
    ante cambios en el rendimiento.
    
    Parámetros:
    -----------
    valor_nominal : float
        Valor nominal del bono
    tasa_cupon : float
        Tasa de cupón anual
    periodos : int
        Años hasta el vencimiento
    rendimiento : float
        Rendimiento del bono
    frecuencia : int
        Frecuencia de pagos por año
    
    Retorna:
    --------
    float
        Duración modificada
    """
    d_mac = duracion_macaulay(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia)
    return d_mac / (1 + rendimiento/frecuencia)


def convexidad(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia=1):
    """
    Calcula la convexidad de un bono.
    
    La convexidad mide la curvatura de la relación precio-rendimiento,
    proporcionando una mejor aproximación de los cambios de precio.
    
    Parámetros:
    -----------
    valor_nominal : float
        Valor nominal del bono
    tasa_cupon : float
        Tasa de cupón anual
    periodos : int
        Años hasta el vencimiento
    rendimiento : float
        Rendimiento del bono
    frecuencia : int
        Frecuencia de pagos por año
    
    Retorna:
    --------
    float
        Convexidad del bono
    """
    cupon_periodo = (tasa_cupon * valor_nominal) / frecuencia
    rendimiento_periodo = rendimiento / frecuencia
    num_periodos = periodos * frecuencia
    
    precio = precio_bono(valor_nominal, tasa_cupon, periodos, rendimiento, frecuencia)
    
    suma_convexidad = 0
    
    for t in range(1, num_periodos + 1):
        if t < num_periodos:
            flujo = cupon_periodo
        else:
            flujo = cupon_periodo + valor_nominal
        
        suma_convexidad += (flujo * t * (t + 1)) / (1 + rendimiento_periodo)**(t + 2)
    
    return suma_convexidad / (precio * frecuencia**2)


# Ejemplo de uso y testing
if __name__ == "__main__":
    print("=== TESTING MÓDULO VALUACIÓN DE BONOS ===")
    
    # Test básico
    precio = precio_bono(1000, 0.08, 5, 0.10)
    print(f"Precio bono básico: ${precio:.2f}")
    
    # Test YTM
    ytm = rendimiento_al_vencimiento(950, 1000, 0.08, 5)
    print(f"YTM: {ytm:.4f} ({ytm*100:.2f}%)")
    
    # Test clase Bono
    mi_bono = Bono(1000, 0.08, 5, 2)  # Semestral
    precio_obj = mi_bono.precio(0.10)
    duracion = mi_bono.duracion_modificada(0.10)
    print(f"Precio (clase): ${precio_obj:.2f}")
    print(f"Duración modificada: {duracion:.4f}")
    
    print("\n✅ Todos los tests completados exitosamente")
