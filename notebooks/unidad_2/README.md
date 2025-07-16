# Unidad 2: Análisis de Estados Financieros

Esta unidad aborda el análisis e interpretación de la información contable-financiera de las empresas, herramienta fundamental para la toma de decisiones empresariales y la evaluación del desempeño organizacional.

## 🎯 Objetivos de Aprendizaje

- Comprender la estructura y componentes de los estados financieros básicos
- Dominar el cálculo e interpretación de ratios financieros fundamentales
- Aplicar técnicas de análisis horizontal, vertical y comparativo
- Evaluar la salud financiera y riesgo de quiebra empresarial
- Implementar análisis financiero automatizado con Python

## 📚 Marco Teórico

### Estados Financieros Básicos

Los estados financieros son informes que presentan la situación económica y financiera de una empresa en un momento determinado o durante un período específico. En Argentina, se rigen por las Normas Internacionales de Información Financiera (NIIF) y las normas de la Federación Argentina de Consejos Profesionales de Ciencias Económicas (FACPCE).

#### Estados Principales:
1. **Estado de Situación Patrimonial (Balance)**: Fotografía financiera en un momento dado
2. **Estado de Resultados**: Rentabilidad durante un período
3. **Estado de Flujo de Efectivo**: Movimientos de efectivo
4. **Estado de Evolución del Patrimonio Neto**: Cambios en el capital

### Análisis de Ratios Financieros

Los ratios son herramientas que permiten comparar y evaluar el desempeño financiero mediante relaciones matemáticas entre diferentes partidas de los estados financieros.

#### Categorías Principales:
- **Liquidez**: Capacidad de pago a corto plazo
- **Actividad**: Eficiencia en el uso de activos
- **Endeudamiento**: Estructura de financiamiento
- **Rentabilidad**: Capacidad de generar beneficios

## 📖 Notebooks Disponibles

### 2.1 Lectura e Interpretación de Estados Financieros
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.1_lectura_estados_financieros.ipynb)

- Estructura del Estado de Situación Patrimonial
- Componentes del Estado de Resultados
- Normas contables argentinas (NIIF-FACPCE)
- Lectura automatizada de estados financieros con pandas

### 2.2 Ratios de Liquidez y Actividad
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.2_ratios_liquidez_actividad.ipynb)

- Ratios de liquidez corriente, ácida y absoluta
- Rotación de inventarios, cuentas por cobrar y por pagar
- Ciclo de conversión del efectivo
- Análisis de capital de trabajo

### 2.3 Ratios de Endeudamiento y Rentabilidad
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.3_ratios_endeudamiento_rentabilidad.ipynb)

- Estructura de endeudamiento y apalancamiento
- ROE, ROA, ROI: Medidas de rentabilidad
- Márgenes de ganancia y eficiencia operativa
- Análisis de cobertura de intereses

### 2.4 Modelo DuPont
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.4_analisis_dupont.ipynb)

- Descomposición del ROE (Rentabilidad del Patrimonio)
- Análisis de palancas: financiera, operativa y total
- Identificación de drivers de rentabilidad
- Estrategias de mejora del desempeño financiero

### 2.5 Análisis Temporal y Comparativo
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.5_analisis_temporal_comparativo.ipynb)

- Análisis horizontal (evolución temporal)
- Análisis vertical (estructura porcentual)
- Benchmarking sectorial
- Análisis de tendencias con visualizaciones

### 2.6 Predicción de Quiebras - Modelo Altman
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_2/2.6_prediccion_quiebras_altman.ipynb)

- Z-Score de Altman original y adaptaciones
- Z''-Score para mercados emergentes
- Modelos predictivos de dificultades financieras
- Aplicación a empresas argentinas cotizantes

## 🔧 Módulo de Utilidades

### analisis_financiero.py
Módulo Python con funciones reutilizables para automatizar cálculos financieros:

```python
from analisis_financiero import (
    calcular_ratios_liquidez,
    calcular_ratios_actividad,
    calcular_ratios_endeudamiento,
    calcular_ratios_rentabilidad,
    analisis_dupont,
    z_score_altman
)

# Ejemplo de uso
ratios = calcular_ratios_liquidez(activo_corriente, pasivo_corriente, inventarios, efectivo)
```

## 📊 Casos de Estudio

Los notebooks incluyen análisis prácticos de empresas argentinas como:
- **YPF S.A.** (Energía)
- **Banco Macro** (Servicios Financieros)
- **Pampa Energía** (Utilities)
- **Telecom Argentina** (Telecomunicaciones)
- **Arcor** (Alimentos)

## 📚 Material Complementario

### Lecturas Recomendadas
- Dumrauf, G. L. (2013). *Finanzas Corporativas: Un enfoque latinoamericano*. 3ra Edición. Capítulos 8-10.
- Palepu, K. G., & Healy, P. M. (2013). *Business Analysis and Valuation Using Financial Statements*. Capítulos 3-6.
- García Fronti, I. (2017). *Análisis de Estados Financieros*. Editorial Errepar. Buenos Aires.

### Recursos Online Argentina
- [Comisión Nacional de Valores (CNV)](https://www.cnv.gov.ar/) - Estados financieros de empresas cotizantes
- [Bolsas y Mercados Argentinos (BYMA)](https://www.byma.com.ar/) - Información bursátil
- [BCRA - Banco Central](https://www.bcra.gob.ar/) - Información del sistema financiero
- [FACPCE](https://www.facpce.org.ar/) - Normas contables profesionales

## 🎯 Metodología de Estudio

1. **Teoría** (30%): Conceptos fundamentales y marcos teóricos
2. **Práctica Python** (40%): Implementación computacional
3. **Casos Reales** (30%): Aplicación a empresas argentinas

## ⚡ Conocimientos Previos

- Unidad 1: Valor temporal del dinero
- Conceptos básicos de contabilidad
- Programación Python básica (pandas, matplotlib)

## 🔗 Conexiones con Otras Unidades

- **Unidad 3**: Valuación de activos utilizará ratios como inputs
- **Unidad 6**: Valuación de empresas aplicará análisis financiero
- **Unidad 7**: Project Finance incorporará análisis de viabilidad financiera
