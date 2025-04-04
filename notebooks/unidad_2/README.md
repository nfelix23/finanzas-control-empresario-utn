# Unidad 2: Análisis de Estados Financieros

Esta unidad aborda las técnicas y metodologías para analizar e interpretar la información contable-financiera de las empresas, con enfoque en el contexto empresarial argentino.

## Objetivos de Aprendizaje

- Comprender la estructura y componentes de los estados financieros
- Aplicar técnicas de análisis horizontal y vertical para evaluar tendencias
- Calcular e interpretar ratios financieros clave
- Desarrollar modelos para la predicción de riesgo financiero y quiebras
- Evaluar la salud financiera de empresas argentinas mediante casos prácticos

## Notebooks

### 2.1 Introducción a los Estados Financieros
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.1_introduccion_estados_financieros.ipynb)

- Estructura y componentes del Balance General
- Estado de Resultados y su interpretación
- Estado de Flujo de Efectivo
- Particularidades de la normativa contable argentina

### 2.2 Análisis Horizontal y Vertical
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.2_analisis_horizontal_vertical.ipynb)

- Metodología del análisis horizontal: evaluación de tendencias
- Técnicas de análisis vertical y su interpretación
- Implementación con Python y pandas
- Visualización de tendencias financieras

### 2.3 Ratios Financieros
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.3_ratios_financieros.ipynb)

- Indicadores de liquidez (corriente, prueba ácida, capital de trabajo)
- Indicadores de actividad (rotación de inventarios, plazos de cobro y pago)
- Indicadores de solvencia y endeudamiento
- Indicadores de rentabilidad (ROE, ROA, margen bruto/operativo/neto)
- Implementación de funciones en Python para su cálculo automatizado

### 2.4 Análisis Integrado y Modelo DuPont
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.4_analisis_integrado_modelo_dupont.ipynb)

- Descomposición del ROE mediante el enfoque DuPont
- Interpretación de los componentes del modelo
- Análisis de sensibilidad para mejora de indicadores
- Implementación en Python y visualización

### 2.5 Predicción de Quiebras y Riesgo Financiero
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.5_prediccion_quiebras.ipynb)

- Modelo Z-Score de Altman
- Adaptaciones para mercados emergentes (Z''-Score)
- Implementación de modelos predictivos con Python
- Aplicación a casos de empresas argentinas

## Módulos de Utilidades

El módulo `analisis_financiero.py` contiene funciones reutilizables para el análisis financiero:

```python
# Ejemplo de uso
from analisis_financiero import calcular_ratios, analisis_dupont

# Calcular los ratios financieros para una empresa
ratios = calcular_ratios(balance, resultados)
```

## Material Complementario

### Lecturas Recomendadas
- Dumrauf, G. L. (2013). *Finanzas Corporativas: Un enfoque latinoamericano*. 3ra Edición. Capítulos 8-9.
- Palepu, K. G., & Healy, P. M. (2013). *Business Analysis and Valuation Using Financial Statements*. Capítulos 3-5.

### Recursos Online
- [Comisión Nacional de Valores (CNV)](https://www.cnv.gov.ar/) - Estados financieros de empresas que cotizan en bolsa
- [Bolsa de Comercio de Buenos Aires](https://www.bcba.sba.com.ar/) - Información financiera de empresas argentinas

## Ejercicios Prácticos

Cada notebook incluye ejercicios prácticos utilizando datos reales de empresas argentinas para aplicar los conceptos aprendidos en situaciones del mundo real.
