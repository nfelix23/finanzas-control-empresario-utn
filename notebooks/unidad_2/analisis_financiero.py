"""
Módulo de Análisis Financiero - UTN La Plata
Finanzas y Control Empresario

Este módulo contiene funciones para el cálculo automático de ratios financieros
y análisis de estados financieros.

Autor: Prof. Nicolás Félix
Fecha: Julio 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnalizadorFinanciero:
    """
    Clase principal para el análisis financiero automatizado
    """
    
    def __init__(self):
        self.empresa = None
        self.periodo = None
        self.estados_financieros = {}
        
    def cargar_estados_financieros(self, balance: pd.DataFrame, 
                                 estado_resultados: pd.DataFrame,
                                 empresa: str = None, periodo: str = None):
        """
        Carga los estados financieros para análisis
        
        Parameters:
        -----------
        balance : pd.DataFrame
            Estado de Situación Patrimonial
        estado_resultados : pd.DataFrame  
            Estado de Resultados
        empresa : str
            Nombre de la empresa
        periodo : str
            Período de análisis
        """
        self.estados_financieros['balance'] = balance
        self.estados_financieros['resultados'] = estado_resultados
        self.empresa = empresa
        self.periodo = periodo
        print(f"Estados financieros cargados para {empresa} - Período {periodo}")

def calcular_ratios_liquidez(activo_corriente: float, 
                           pasivo_corriente: float,
                           inventarios: float = 0,
                           efectivo: float = 0,
                           inversiones_temporales: float = 0) -> Dict[str, float]:
    """
    Calcula los ratios de liquidez fundamentales
    
    Parameters:
    -----------
    activo_corriente : float
        Total del activo corriente
    pasivo_corriente : float
        Total del pasivo corriente
    inventarios : float
        Inventarios (para ratio ácido)
    efectivo : float
        Efectivo y equivalentes
    inversiones_temporales : float
        Inversiones de corto plazo
        
    Returns:
    --------
    Dict[str, float]
        Diccionario con los ratios calculados
    """
    
    if pasivo_corriente == 0:
        raise ValueError("El pasivo corriente no puede ser cero")
    
    ratios = {}
    
    # Ratio de liquidez corriente
    ratios['liquidez_corriente'] = activo_corriente / pasivo_corriente
    
    # Ratio de liquidez ácida (prueba ácida)
    activo_liquido = activo_corriente - inventarios
    ratios['liquidez_acida'] = activo_liquido / pasivo_corriente
    
    # Ratio de liquidez absoluta (inmediata)
    disponible = efectivo + inversiones_temporales
    ratios['liquidez_absoluta'] = disponible / pasivo_corriente
    
    return ratios

def calcular_ratios_actividad(ventas: float,
                            costo_ventas: float,
                            cuentas_por_cobrar: float,
                            inventarios: float,
                            cuentas_por_pagar: float,
                            activo_total: float,
                            activo_fijo: float,
                            dias_año: int = 365) -> Dict[str, float]:
    """
    Calcula los ratios de actividad o eficiencia
    
    Parameters:
    -----------
    ventas : float
        Ventas netas anuales
    costo_ventas : float
        Costo de mercaderías vendidas
    cuentas_por_cobrar : float
        Promedio de cuentas por cobrar
    inventarios : float
        Inventario promedio
    cuentas_por_pagar : float
        Promedio de cuentas por pagar
    activo_total : float
        Total de activos
    activo_fijo : float
        Activos fijos netos
    dias_año : int
        Días del año (365 por defecto)
        
    Returns:
    --------
    Dict[str, float]
        Diccionario con los ratios calculados
    """
    
    ratios = {}
    
    # Rotación de cuentas por cobrar
    if cuentas_por_cobrar > 0:
        ratios['rotacion_cxc'] = ventas / cuentas_por_cobrar
        ratios['dias_cobro'] = dias_año / ratios['rotacion_cxc']
    else:
        ratios['rotacion_cxc'] = np.inf
        ratios['dias_cobro'] = 0
    
    # Rotación de inventarios
    if inventarios > 0 and costo_ventas > 0:
        ratios['rotacion_inventarios'] = costo_ventas / inventarios
        ratios['dias_inventario'] = dias_año / ratios['rotacion_inventarios']
    else:
        ratios['rotacion_inventarios'] = np.inf if inventarios == 0 else 0
        ratios['dias_inventario'] = 0
    
    # Rotación de cuentas por pagar
    if cuentas_por_pagar > 0 and costo_ventas > 0:
        ratios['rotacion_cxp'] = costo_ventas / cuentas_por_pagar
        ratios['dias_pago'] = dias_año / ratios['rotacion_cxp']
    else:
        ratios['rotacion_cxp'] = np.inf if cuentas_por_pagar == 0 else 0
        ratios['dias_pago'] = 0
    
    # Ciclo de conversión del efectivo
    ratios['ciclo_efectivo'] = (ratios['dias_cobro'] + 
                               ratios['dias_inventario'] - 
                               ratios['dias_pago'])
    
    # Rotación de activos
    if activo_total > 0:
        ratios['rotacion_activo_total'] = ventas / activo_total
    else:
        ratios['rotacion_activo_total'] = 0
        
    if activo_fijo > 0:
        ratios['rotacion_activo_fijo'] = ventas / activo_fijo
    else:
        ratios['rotacion_activo_fijo'] = np.inf if ventas > 0 else 0
    
    return ratios

def calcular_ratios_endeudamiento(activo_total: float,
                                pasivo_total: float,
                                patrimonio_neto: float,
                                pasivo_corriente: float,
                                pasivo_no_corriente: float,
                                gastos_financieros: float,
                                resultado_operativo: float) -> Dict[str, float]:
    """
    Calcula los ratios de endeudamiento y estructura financiera
    
    Parameters:
    -----------
    activo_total : float
        Total de activos
    pasivo_total : float
        Total de pasivos
    patrimonio_neto : float
        Patrimonio neto
    pasivo_corriente : float
        Pasivo corriente
    pasivo_no_corriente : float
        Pasivo no corriente
    gastos_financieros : float
        Intereses y gastos financieros
    resultado_operativo : float
        Resultado operativo (EBIT)
        
    Returns:
    --------
    Dict[str, float]
        Diccionario con los ratios calculados
    """
    
    ratios = {}
    
    # Ratio de endeudamiento total
    if activo_total > 0:
        ratios['endeudamiento_total'] = pasivo_total / activo_total
        ratios['autonomia'] = patrimonio_neto / activo_total
    else:
        ratios['endeudamiento_total'] = 0
        ratios['autonomia'] = 0
    
    # Apalancamiento financiero
    if patrimonio_neto > 0:
        ratios['apalancamiento'] = pasivo_total / patrimonio_neto
        ratios['multiplicador_capital'] = activo_total / patrimonio_neto
    else:
        ratios['apalancamiento'] = np.inf
        ratios['multiplicador_capital'] = np.inf
    
    # Estructura del pasivo
    if pasivo_total > 0:
        ratios['pasivo_corriente_sobre_total'] = pasivo_corriente / pasivo_total
        ratios['pasivo_no_corriente_sobre_total'] = pasivo_no_corriente / pasivo_total
    else:
        ratios['pasivo_corriente_sobre_total'] = 0
        ratios['pasivo_no_corriente_sobre_total'] = 0
    
    # Cobertura de intereses
    if gastos_financieros > 0:
        ratios['cobertura_intereses'] = resultado_operativo / gastos_financieros
    else:
        ratios['cobertura_intereses'] = np.inf if resultado_operativo > 0 else 0
    
    return ratios

def calcular_ratios_rentabilidad(resultado_neto: float,
                                resultado_operativo: float,
                                ventas: float,
                                activo_total: float,
                                patrimonio_neto: float,
                                activo_operativo: float = None) -> Dict[str, float]:
    """
    Calcula los ratios de rentabilidad
    
    Parameters:
    -----------
    resultado_neto : float
        Resultado neto del ejercicio
    resultado_operativo : float
        Resultado operativo (EBIT)
    ventas : float
        Ventas netas
    activo_total : float
        Total de activos
    patrimonio_neto : float
        Patrimonio neto promedio
    activo_operativo : float, optional
        Activos operativos (si no se proporciona, se usa activo_total)
        
    Returns:
    --------
    Dict[str, float]
        Diccionario con los ratios calculados
    """
    
    ratios = {}
    
    # Márgenes de rentabilidad
    if ventas > 0:
        ratios['margen_neto'] = resultado_neto / ventas
        ratios['margen_operativo'] = resultado_operativo / ventas
    else:
        ratios['margen_neto'] = 0
        ratios['margen_operativo'] = 0
    
    # Rentabilidad sobre activos (ROA)
    if activo_total > 0:
        ratios['roa'] = resultado_neto / activo_total
        ratios['roi_operativo'] = resultado_operativo / activo_total
    else:
        ratios['roa'] = 0
        ratios['roi_operativo'] = 0
    
    # Rentabilidad sobre patrimonio (ROE)
    if patrimonio_neto > 0:
        ratios['roe'] = resultado_neto / patrimonio_neto
    else:
        ratios['roe'] = np.inf if resultado_neto > 0 else 0
    
    # ROI sobre activos operativos
    if activo_operativo and activo_operativo > 0:
        ratios['roi_activo_operativo'] = resultado_operativo / activo_operativo
    elif activo_total > 0:
        ratios['roi_activo_operativo'] = resultado_operativo / activo_total
    else:
        ratios['roi_activo_operativo'] = 0
    
    return ratios

def analisis_dupont(resultado_neto: float,
                   ventas: float,
                   activo_total: float,
                   patrimonio_neto: float) -> Dict[str, float]:
    """
    Realiza el análisis DuPont del ROE
    
    ROE = Margen Neto × Rotación de Activos × Multiplicador de Capital
    
    Parameters:
    -----------
    resultado_neto : float
        Resultado neto del ejercicio
    ventas : float
        Ventas netas
    activo_total : float
        Total de activos
    patrimonio_neto : float
        Patrimonio neto
        
    Returns:
    --------
    Dict[str, float]
        Componentes del análisis DuPont
    """
    
    dupont = {}
    
    # Componentes del DuPont
    if ventas > 0:
        dupont['margen_neto'] = resultado_neto / ventas
    else:
        dupont['margen_neto'] = 0
        
    if activo_total > 0:
        dupont['rotacion_activos'] = ventas / activo_total
    else:
        dupont['rotacion_activos'] = 0
        
    if patrimonio_neto > 0:
        dupont['multiplicador_capital'] = activo_total / patrimonio_neto
        dupont['roe'] = resultado_neto / patrimonio_neto
    else:
        dupont['multiplicador_capital'] = np.inf
        dupont['roe'] = np.inf if resultado_neto > 0 else 0
    
    # Verificación del producto
    dupont['roe_calculado'] = (dupont['margen_neto'] * 
                              dupont['rotacion_activos'] * 
                              dupont['multiplicador_capital'])
    
    return dupont

def z_score_altman(capital_trabajo: float,
                  utilidades_retenidas: float,
                  resultado_operativo: float,
                  valor_mercado_capital: float,
                  ventas: float,
                  activo_total: float,
                  pasivo_total: float,
                  modelo: str = 'original') -> Dict[str, float]:
    """
    Calcula el Z-Score de Altman para predicción de quiebras
    
    Parameters:
    -----------
    capital_trabajo : float
        Capital de trabajo (Activo Corriente - Pasivo Corriente)
    utilidades_retenidas : float
        Utilidades retenidas acumuladas
    resultado_operativo : float
        Resultado operativo (EBIT)
    valor_mercado_capital : float
        Valor de mercado del capital (para modelo original)
        Para modelo revisado, usar valor en libros del patrimonio
    ventas : float
        Ventas netas
    activo_total : float
        Total de activos
    pasivo_total : float
        Total de pasivos
    modelo : str
        'original', 'revisado' o 'emergentes'
        
    Returns:
    --------
    Dict[str, float]
        Z-Score y clasificación de riesgo
    """
    
    resultado = {}
    
    # Variables del modelo
    x1 = capital_trabajo / activo_total
    x2 = utilidades_retenidas / activo_total
    x3 = resultado_operativo / activo_total
    x4 = valor_mercado_capital / pasivo_total
    x5 = ventas / activo_total
    
    # Selección del modelo
    if modelo == 'original':
        # Modelo original (1968) - empresas cotizantes
        z_score = 1.2*x1 + 1.4*x2 + 3.3*x3 + 0.6*x4 + 1.0*x5
        zona_segura = 2.99
        zona_gris_inf = 1.81
        
    elif modelo == 'revisado':
        # Modelo revisado (1983) - empresas no cotizantes
        x4_revisado = valor_mercado_capital / pasivo_total  # Valor libro del patrimonio
        z_score = 0.717*x1 + 0.847*x2 + 3.107*x3 + 0.420*x4_revisado + 0.998*x5
        zona_segura = 2.90
        zona_gris_inf = 1.23
        
    elif modelo == 'emergentes':
        # Modelo para mercados emergentes (Z''-Score)
        z_score = 3.25 + 6.56*x1 + 3.26*x2 + 6.72*x3 + 1.05*x4
        zona_segura = 5.85
        zona_gris_inf = 4.15
        
    else:
        raise ValueError("Modelo debe ser 'original', 'revisado' o 'emergentes'")
    
    # Clasificación de riesgo
    if z_score >= zona_segura:
        clasificacion = "Zona Segura - Bajo riesgo de quiebra"
        riesgo = "Bajo"
    elif z_score >= zona_gris_inf:
        clasificacion = "Zona Gris - Riesgo moderado"
        riesgo = "Moderado"
    else:
        clasificacion = "Zona de Peligro - Alto riesgo de quiebra"
        riesgo = "Alto"
    
    resultado = {
        'z_score': z_score,
        'modelo': modelo,
        'clasificacion': clasificacion,
        'nivel_riesgo': riesgo,
        'x1_capital_trabajo': x1,
        'x2_utilidades_retenidas': x2,
        'x3_rentabilidad': x3,
        'x4_estructura_capital': x4,
        'x5_rotacion_ventas': x5
    }
    
    return resultado

def crear_dashboard_ratios(ratios_dict: Dict[str, Dict[str, float]], 
                          empresa: str = "Empresa",
                          figsize: Tuple[int, int] = (15, 12)) -> None:
    """
    Crea un dashboard visual con los principales ratios financieros
    
    Parameters:
    -----------
    ratios_dict : Dict[str, Dict[str, float]]
        Diccionario con categorías de ratios y sus valores
    empresa : str
        Nombre de la empresa
    figsize : Tuple[int, int]
        Tamaño de la figura
    """
    
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(f'Dashboard Financiero - {empresa}', fontsize=16, fontweight='bold')
    
    # Ratios de Liquidez
    if 'liquidez' in ratios_dict:
        liquidez = ratios_dict['liquidez']
        categorias = list(liquidez.keys())
        valores = list(liquidez.values())
        
        axes[0,0].bar(categorias, valores, color=['skyblue', 'lightgreen', 'coral'])
        axes[0,0].set_title('Ratios de Liquidez')
        axes[0,0].set_ylabel('Ratio')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Línea de referencia
        axes[0,0].axhline(y=1.0, color='red', linestyle='--', alpha=0.7, label='Mínimo recomendado')
        axes[0,0].legend()
    
    # Ratios de Rentabilidad
    if 'rentabilidad' in ratios_dict:
        rentabilidad = ratios_dict['rentabilidad']
        
        # Convertir a porcentajes
        labels = []
        valores = []
        for key, value in rentabilidad.items():
            if 'margen' in key.lower() or 'ro' in key.lower():
                labels.append(key.upper())
                valores.append(value * 100)  # Convertir a porcentaje
        
        axes[0,1].bar(labels, valores, color=['gold', 'orange', 'darkturquoise'])
        axes[0,1].set_title('Ratios de Rentabilidad (%)')
        axes[0,1].set_ylabel('Porcentaje')
        axes[0,1].tick_params(axis='x', rotation=45)
    
    # Ratios de Actividad (Rotaciones)
    if 'actividad' in ratios_dict:
        actividad = ratios_dict['actividad']
        
        # Seleccionar solo ratios de rotación
        rotaciones = {k: v for k, v in actividad.items() if 'rotacion' in k}
        
        if rotaciones:
            labels = list(rotaciones.keys())
            valores = list(rotaciones.values())
            
            axes[1,0].bar(labels, valores, color=['mediumpurple', 'plum', 'thistle'])
            axes[1,0].set_title('Ratios de Actividad (Rotaciones)')
            axes[1,0].set_ylabel('Veces por año')
            axes[1,0].tick_params(axis='x', rotation=45)
    
    # Estructura de Endeudamiento
    if 'endeudamiento' in ratios_dict:
        endeud = ratios_dict['endeudamiento']
        
        # Crear gráfico de torta para estructura
        if 'endeudamiento_total' in endeud and 'autonomia' in endeud:
            labels = ['Financiamiento Externo', 'Financiamiento Propio']
            sizes = [endeud['endeudamiento_total'], endeud['autonomia']]
            colors = ['lightcoral', 'lightblue']
            
            axes[1,1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            axes[1,1].set_title('Estructura de Financiamiento')
    
    plt.tight_layout()
    plt.show()

def interpretar_ratios(ratios: Dict[str, float], categoria: str) -> List[str]:
    """
    Proporciona interpretaciones automáticas de los ratios calculados
    
    Parameters:
    -----------
    ratios : Dict[str, float]
        Ratios calculados
    categoria : str
        Categoría de ratios ('liquidez', 'actividad', 'endeudamiento', 'rentabilidad')
        
    Returns:
    --------
    List[str]
        Lista de interpretaciones
    """
    
    interpretaciones = []
    
    if categoria == 'liquidez':
        if 'liquidez_corriente' in ratios:
            lc = ratios['liquidez_corriente']
            if lc >= 2.0:
                interpretaciones.append(f"Liquidez corriente excelente ({lc:.2f}). La empresa puede cubrir {lc:.1f} veces sus obligaciones de corto plazo.")
            elif lc >= 1.5:
                interpretaciones.append(f"Liquidez corriente buena ({lc:.2f}). Situación financiera estable a corto plazo.")
            elif lc >= 1.0:
                interpretaciones.append(f"Liquidez corriente aceptable ({lc:.2f}). Monitorear evolución de capital de trabajo.")
            else:
                interpretaciones.append(f"Liquidez corriente baja ({lc:.2f}). Posibles dificultades para cubrir obligaciones inmediatas.")
    
    elif categoria == 'rentabilidad':
        if 'roe' in ratios:
            roe = ratios['roe'] * 100
            if roe >= 15:
                interpretaciones.append(f"ROE excelente ({roe:.1f}%). Muy buena rentabilidad para los accionistas.")
            elif roe >= 10:
                interpretaciones.append(f"ROE bueno ({roe:.1f}%). Rentabilidad satisfactoria del patrimonio.")
            elif roe >= 5:
                interpretaciones.append(f"ROE moderado ({roe:.1f}%). Oportunidades de mejora en rentabilidad.")
            else:
                interpretaciones.append(f"ROE bajo ({roe:.1f}%). Necesario revisar estrategia de rentabilidad.")
    
    elif categoria == 'endeudamiento':
        if 'endeudamiento_total' in ratios:
            et = ratios['endeudamiento_total'] * 100
            if et <= 30:
                interpretaciones.append(f"Endeudamiento conservador ({et:.1f}%). Baja dependencia de financiamiento externo.")
            elif et <= 50:
                interpretaciones.append(f"Endeudamiento moderado ({et:.1f}%). Estructura financiera equilibrada.")
            elif et <= 70:
                interpretaciones.append(f"Endeudamiento alto ({et:.1f}%). Monitorear capacidad de pago.")
            else:
                interpretaciones.append(f"Endeudamiento muy alto ({et:.1f}%). Riesgo financiero elevado.")
    
    return interpretaciones

# Función de utilidad para formatear números
def formatear_numero(numero: float, decimales: int = 2, porcentaje: bool = False) -> str:
    """
    Formatea números para presentación
    
    Parameters:
    -----------
    numero : float
        Número a formatear
    decimales : int
        Cantidad de decimales
    porcentaje : bool
        Si True, multiplica por 100 y agrega %
        
    Returns:
    --------
    str
        Número formateado
    """
    if pd.isna(numero) or numero == np.inf:
        return "N/A"
    
    if porcentaje:
        return f"{numero * 100:.{decimales}f}%"
    else:
        return f"{numero:.{decimales}f}"

# Constantes para benchmarks de la industria argentina
BENCHMARKS_INDUSTRIA = {
    'liquidez_corriente': {'minimo': 1.0, 'bueno': 1.5, 'excelente': 2.0},
    'liquidez_acida': {'minimo': 0.8, 'bueno': 1.0, 'excelente': 1.2},
    'endeudamiento_total': {'bajo': 0.3, 'moderado': 0.5, 'alto': 0.7},
    'roe': {'bajo': 0.05, 'bueno': 0.10, 'excelente': 0.15},
    'roa': {'bajo': 0.03, 'bueno': 0.06, 'excelente': 0.10},
    'margen_neto': {'bajo': 0.03, 'bueno': 0.05, 'excelente': 0.10}
}

if __name__ == "__main__":
    print("Módulo de Análisis Financiero - UTN La Plata")
    print("Versión 1.0 - Julio 2025")
    print("\nFunciones disponibles:")
    print("- calcular_ratios_liquidez()")
    print("- calcular_ratios_actividad()")
    print("- calcular_ratios_endeudamiento()")
    print("- calcular_ratios_rentabilidad()")
    print("- analisis_dupont()")
    print("- z_score_altman()")
    print("- crear_dashboard_ratios()")
    print("- interpretar_ratios()")
