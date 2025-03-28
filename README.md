# Finanzas y Control Empresario - UTN La Plata

Repositorio oficial para la materia Finanzas y Control Empresario de la carrera de Ingeniería Industrial de la Universidad Tecnológica Nacional, Facultad Regional La Plata.

## Acerca de la materia

Esta materia está diseñada para desarrollar habilidades analíticas en finanzas cuantitativas aplicadas a la gestión empresarial, utilizando Python como herramienta computacional. El enfoque es teórico-práctico, con aplicaciones específicas al contexto empresarial argentino.

## Contenido del repositorio

El repositorio está organizado por unidades temáticas, siguiendo el programa oficial de la materia:

### 1. [Fundamentos y Valor del Dinero en el Tiempo](./notebooks/unidad_1)
- Conceptos básicos financieros
- Valor actual y futuro
- Tasas de interés (nominal, efectiva, TNA, TEA)
- Inflación y tasas reales
- Anualidades y perpetuidades

### 2. [Análisis de Estados Financieros](./notebooks/unidad_2)
- Interpretación y análisis de la información contable
- Ratios financieros
- Análisis horizontal y vertical
- Predicción de quiebras

### 3. [Valuación de Activos](./notebooks/unidad_3)
- Metodologías para valorar bonos
- Valuación de acciones
- Derivados financieros básicos

### 4. [Riesgo y Rendimiento](./notebooks/unidad_4)
- Teoría de carteras
- Diversificación y medidas de riesgo
- Modelo CAPM y APT

### 5. [Análisis Técnico y Backtesting](./notebooks/unidad_5)
- Indicadores técnicos
- Estrategias de trading
- Backtesting y optimización

### 6. [Valuación de Empresas](./notebooks/unidad_6)
- Métodos de valoración empresarial
- Flujos de fondos descontados
- Múltiplos comparables

### 7. [Project Finance](./notebooks/unidad_7)
- Evaluación de proyectos
- Financiamiento estructurado
- Análisis de sensibilidad

### 8. [Análisis de Riesgo y Simulación](./notebooks/unidad_8)
- Modelos estocásticos
- Simulación Monte Carlo
- Value at Risk (VaR)

## Cómo usar este repositorio

### Opción 1: Google Colab (recomendado para principiantes)
Cada notebook tiene un enlace [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)] que permite abrirlo directamente en Google Colab sin necesidad de instalar nada en tu computadora.

### Opción 2: Ejecutar localmente

#### Requisitos

Para ejecutar los notebooks en tu computadora necesitarás:

```
python >= 3.8
jupyter >= 1.0.0
numpy >= 1.20.0
pandas >= 1.3.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
scipy >= 1.7.0
yfinance >= 0.1.70
```

Puedes instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

#### Pasos para ejecutar localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/nfelix23/finanzas-control-empresario-utn.git
   cd finanzas-control-empresario-utn
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicia Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Navega a la carpeta de la unidad que deseas estudiar y abre el notebook correspondiente.

## Metodología de enseñanza

- **Teoría**: Cada unidad comienza con una introducción teórica de los conceptos fundamentales.
- **Implementación**: Se muestran implementaciones en Python de los modelos y cálculos financieros.
- **Ejemplos**: Casos prácticos con datos reales o simulados del mercado argentino.
- **Ejercicios**: Problemas propuestos para resolver y poner en práctica lo aprendido.

## Contribuciones

Los estudiantes pueden contribuir a este repositorio mediante pull requests, reportando errores o sugiriendo mejoras a través de issues.