# Unidad 1: Fundamentos y Valor del Dinero en el Tiempo

Esta unidad aborda los conceptos fundamentales de las finanzas y del valor temporal del dinero, pilares esenciales para el análisis financiero y la toma de decisiones económicas en el ámbito empresarial.

## Objetivos de Aprendizaje

- Comprender el concepto del valor temporal del dinero y su importancia en el análisis financiero
- Aprender a calcular valores presentes y futuros de flujos de efectivo
- Dominar la conversión entre diferentes tipos de tasas de interés
- Comprender el efecto de la inflación en los rendimientos financieros
- Aplicar el concepto de anualidades y perpetuidades a problemas financieros reales

## Notebooks

Estos son los materiales disponibles para la Unidad 1:

### 1.1 Conceptos Básicos Financieros
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.1_conceptos_basicos_financieros.ipynb)

- Introducción a las finanzas y su importancia
- Fundamentos del valor temporal del dinero
- Factores que afectan al valor del dinero (costo de oportunidad, inflación, riesgo, preferencia temporal)
- Aplicaciones en el contexto económico argentino

### 1.2 Valor Actual y Futuro
#### Parte 1: Fundamentos
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.2_valor_actual_y_futuro_parte1.ipynb)

- Valor futuro de una suma única
- Valor presente de una suma única
- Implementación con Python
- Visualización del crecimiento mediante interés compuesto

#### Parte 2: Aplicaciones
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.2_valor_actual_y_futuro_parte2.ipynb)

- Efecto de la tasa de interés y el tiempo
- Análisis del valor actual de flujos futuros
- La Regla del 72: Calculando el tiempo de duplicación
- Visualizaciones y análisis de sensibilidad

#### Parte 3: Evaluación de Alternativas
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.2_valor_actual_y_futuro_parte3.ipynb)

- Evaluación de alternativas de inversión
- Cálculo del Valor Actual Neto (VAN)
- Análisis de sensibilidad a la tasa de descuento
- Tasa de indiferencia y TIR
- Impacto de la inflación en la evaluación de proyectos

### 1.3 Tasas de Interés
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.3_tasas_de_interes.ipynb)

- Tipos de tasas de interés (nominal, efectiva)
- Conversiones entre tasas
- Efecto de la frecuencia de capitalización
- Tasas reales y el impacto de la inflación
- Análisis de instrumentos financieros en diferentes escenarios

### 1.4 Anualidades y Perpetuidades
#### Parte 1: Fundamentos
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.4_anualidades_parte1.ipynb)

- Concepto de anualidades y perpetuidades
- Tipos de anualidades (ordinarias, adelantadas, diferidas)
- Cálculo del valor actual y futuro de anualidades
- Visualización de flujos de efectivo

#### Parte 2: Aplicación a Préstamos
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.4_anualidades_parte2.ipynb)

- Cálculo de cuotas de préstamos
- Tablas de amortización
- Comparación de sistemas de amortización (francés vs alemán)
- Impacto de la inflación en préstamos

#### Parte 3: Perpetuidades y Casos Especiales
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nfelix23/finanzas-control-empresario-utn/blob/main/notebooks/unidad_1/1.4_anualidades_parte3.ipynb)

- Perpetuidades y su valoración
- Perpetuidades con crecimiento (Modelo de Gordon)
- Anualidades con crecimiento
- Aplicaciones a valuación de propiedades y acciones

## Módulos de Utilidades

El módulo `finanzas_basicas.py` contiene funciones reutilizables para cálculos financieros que pueden importarse en cualquier notebook:

```python
# Ejemplo de uso
from finanzas_basicas import valor_futuro, valor_actual, tasa_real

# Calcular el valor futuro de $10,000 al 5% anual por 3 años
vf = valor_futuro(10000, 0.05, 3)
```

## Material Complementario

### Lecturas Recomendadas
- Dumrauf, G. L. (2013). *Finanzas Corporativas: Un enfoque latinoamericano*. 3ra Edición. Capítulos 1-3.
- Ross, S., Westerfield, R., & Jordan, B. (2018). *Fundamentos de Finanzas Corporativas*. 11va Edición. Capítulos 4-6.

### Recursos Online
- [Banco Central de la República Argentina](https://www.bcra.gob.ar/) - Datos actualizados sobre tasas de interés
- [INDEC](https://www.indec.gob.ar/) - Información sobre inflación y otros indicadores económicos

## Ejercicios Prácticos

Cada notebook incluye ejercicios propuestos al final para reforzar los conceptos aprendidos. Se recomienda resolverlos antes de avanzar a la siguiente unidad.