# Unidad 3: Valuación de Activos

Esta unidad aborda las metodologías fundamentales para la valuación de diferentes instrumentos financieros, con énfasis en bonos, acciones y derivados básicos. Los estudiantes aprenderán tanto los fundamentos teóricos como su implementación práctica en Python.

## Objetivos de Aprendizaje

- Dominar las técnicas de valuación de bonos y análisis de riesgo de tasa de interés
- Comprender los modelos de valuación de acciones y sus aplicaciones
- Aplicar conceptos de duración, convexidad y sensibilidad
- Implementar modelos de valuación utilizando Python
- Analizar instrumentos del mercado financiero argentino

## Notebooks

### 3.1 Valuación de Bonos
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_3/3.1_valuacion_bonos.ipynb)

**Contenido teórico:**
- Conceptos fundamentales de bonos y su funcionamiento
- Fórmulas de valuación para diferentes tipos de bonos
- Relación precio-rendimiento y factores determinantes

**Implementación práctica:**
- Funciones Python para cálculo de precios y rendimientos
- Cálculo del Rendimiento al Vencimiento (YTM)
- Análisis de bonos con diferentes características

**Medidas de riesgo:**
- Duración de Macaulay: tiempo promedio ponderado de flujos
- Duración Modificada: sensibilidad del precio ante cambios en tasas
- Convexidad: curvatura de la relación precio-rendimiento
- Aplicaciones para gestión de riesgo de tasa de interés

**Contexto argentino:**
- Análisis de LECAP, BONCER y BONAR
- Impacto de la inflación en la valuación
- Instrumentos ajustables por inflación
- Escenarios de volatilidad de tasas

### 3.2 Valuación de Acciones
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_3/3.2_valuacion_acciones.ipynb)

*En desarrollo*

**Contenido planificado:**
- Modelo de Descuento de Dividendos (DDM)
- Modelo de Gordon (crecimiento constante)
- Modelos de crecimiento por etapas
- Valuación por múltiplos (P/E, P/B, EV/EBITDA)
- Análisis de acciones argentinas

### 3.3 Introducción a Derivados
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_3/3.3_introduccion_derivados.ipynb)

*En desarrollo*

**Contenido planificado:**
- Forwards y Futuros: características y pricing
- Opciones: Call y Put, paridad put-call
- Modelo de Black-Scholes básico
- Aplicaciones de cobertura

## Módulos de Utilidades

### `valuacion_bonos.py`
Módulo completo para análisis de bonos que incluye:

```python
# Importar el módulo
from valuacion_bonos import Bono, precio_bono, rendimiento_al_vencimiento

# Crear un bono
mi_bono = Bono(valor_nominal=1000, tasa_cupon=0.08, años_vencimiento=5, frecuencia=2)

# Calcular precio
precio = mi_bono.precio(rendimiento=0.10)

# Analizar riesgo
duracion = mi_bono.duracion_modificada(0.10)
convexidad = mi_bono.convexidad(0.10)
```

**Funciones principales:**
- `precio_bono()`: Valuación básica de bonos
- `rendimiento_al_vencimiento()`: Cálculo de YTM
- `duracion_macaulay()`, `duracion_modificada()`: Medidas de duración
- `convexidad()`: Cálculo de convexidad
- `estimar_cambio_precio()`: Estimación usando duración y convexidad
- `analizar_sensibilidad_cartera()`: Análisis de carteras de bonos

### `valuacion_acciones.py` *(En desarrollo)*
Módulo para valuación de acciones con modelos DDM, Gordon y múltiplos.

### `derivados_basicos.py` *(En desarrollo)*
Módulo para pricing básico de opciones y futuros.

## Casos Prácticos

### Caso 1: Gestión de Cartera de Bonos
Análisis de una cartera diversificada considerando:
- Optimización duración-rendimiento
- Inmunización ante cambios de tasas
- Estrategias de ladder y barbell

### Caso 2: Valuación de Empresa Argentina
Aplicación de múltiples metodologías:
- DCF con diferentes escenarios
- Múltiplos comparables
- Ajustes por riesgo país

### Caso 3: Cobertura con Derivados
Diseño de estrategias de cobertura:
- Protección de carteras de bonos
- Cobertura de riesgo cambiario
- Especulación controlada

## Herramientas y Librerías

**Librerías principales:**
```python
import numpy as np           # Cálculos numéricos
import pandas as pd          # Manejo de datos
import matplotlib.pyplot as plt  # Visualizaciones
import seaborn as sns        # Gráficos estadísticos
from scipy.optimize import fsolve  # Optimización numérica
import yfinance as yf        # Datos financieros
```

**Fuentes de datos recomendadas:**
- Yahoo Finance (yfinance) para datos internacionales
- Banco Central de la República Argentina (BCRA)
- Comisión Nacional de Valores (CNV)
- Bolsa de Comercio de Buenos Aires

## Ejercicios y Evaluación

### Ejercicios de Aplicación
Cada notebook incluye ejercicios progresivos:
1. **Básicos**: Cálculos directos con fórmulas
2. **Intermedios**: Análisis de sensibilidad y escenarios
3. **Avanzados**: Optimización de carteras y estrategias

### Proyecto Integrador
**Valuación completa de una empresa argentina:**
- Análisis fundamental de estados financieros
- Proyección de flujos de fondos
- Aplicación de múltiples métodos de valuación
- Análisis de sensibilidad y escenarios
- Recomendación de inversión fundamentada

## Material Complementario

### Lecturas Recomendadas
- **Dumrauf, G. L. (2013).** *Finanzas Corporativas: Un enfoque latinoamericano*. 3ra Edición. Capítulos 10-15.
- **Ross, S., Westerfield, R., & Jordan, B. (2018).** *Fundamentos de Finanzas Corporativas*. 11va Edición. Capítulos 7-9.
- **Damodaran, A. (2012).** *Investment Valuation: Tools and Techniques*. 3ra Edición.

### Recursos Online
- [BCRA - Información de Mercados](https://www.bcra.gob.ar/)
- [CNV - Estados Financieros](https://www.cnv.gov.ar/)
- [IAMC - Mercado de Capitales](https://www.iamc.sba.com.ar/)
- [Professor Damodaran's Pages](http://pages.stern.nyu.edu/~adamodar/)

### Papers y Artículos Académicos
- "Duration and Convexity: The Price Volatility of Bonds" - CFA Institute
- "Dividend Discount Models" - Financial Analysts Journal
- "The Theory and Practice of Corporate Finance" - Journal of Applied Corporate Finance

## Conexiones con Otras Unidades

**Prerrequisitos:**
- Unidad 1: Valor temporal del dinero y tasas de interés
- Unidad 2: Análisis de estados financieros

**Preparación para:**
- Unidad 4: Riesgo y rendimiento (aplicación a carteras)
- Unidad 6: Valuación de empresas (integración de conceptos)
- Unidad 8: Simulación Monte Carlo (modelos estocásticos)

## Competencias Desarrolladas

### Técnicas
- Implementación de modelos de valuación en Python
- Análisis de sensibilidad y escenarios
- Interpretación de medidas de riesgo financiero
- Uso de datos financieros en tiempo real

### Analíticas
- Evaluación crítica de diferentes metodologías
- Identificación de fortalezas y limitaciones de cada modelo
- Adaptación de modelos al context argentino
- Toma de decisiones bajo incertidumbre

### Comunicacionales
- Presentación clara de resultados de valuación
- Justificación de supuestos y metodologías
- Elaboración de reportes profesionales
- Comunicación de riesgos a audiencias no técnicas

---

## Próximos Desarrollos

La Unidad 3 se completará con:
1. **3.2 Valuación de Acciones** (próximo desarrollo)
2. **3.3 Introducción a Derivados** 
3. **Casos integrados** con datos reales del mercado argentino
4. **Herramientas interactivas** para análisis de sensibilidad

---

*Unidad desarrollada para la cátedra de Finanzas y Control Empresario*  
*Universidad Tecnológica Nacional - Facultad Regional La Plata*  
*Carrera: Ingeniería Industrial*