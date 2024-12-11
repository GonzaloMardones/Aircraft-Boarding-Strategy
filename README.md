# Simulación de Estrategias de Embarque de Aeronaves 🚀

¡Bienvenido! Este proyecto es una simulación diseñada para explorar y optimizar las estrategias de abordaje de pasajeros en aeronaves. Si alguna vez te has preguntado por qué algunas aerolíneas eligen ciertos métodos de embarque y cómo afectan al tiempo total, este proyecto tiene las respuestas. 🛫

## ¿Qué hace este proyecto? 🤔

Este programa simula el proceso de abordaje de pasajeros en un avión, modelando las interacciones entre ellos y evaluando cómo diferentes estrategias afectan los "eventos de bloqueo" (cuando un pasajero obstaculiza el movimiento de otro). Al realizar múltiples simulaciones, el código permite visualizar y analizar patrones, ofreciendo ideas para mejorar la eficiencia del abordaje.

## ¿Por qué es importante? ✈️

En la industria de la aviación, reducir el tiempo de embarque no solo mejora la experiencia de los pasajeros, sino que también ahorra dinero a las aerolíneas. Este proyecto busca responder preguntas clave, como:
- ¿Qué patrones de abordaje minimizan las interferencias entre pasajeros?
- ¿Cómo se puede ajustar el proceso para reducir el tiempo de giro (turnaround time)?
- ¿Qué impacto tienen las estrategias actuales en la eficiencia general?

Con este proyecto, puedes experimentar con diferentes configuraciones y estrategias para encontrar soluciones óptimas.

## Características principales ⚙️

- **Generación aleatoria de pasajeros:** Crea listas de pasajeros con asignación aleatoria de filas y asientos (ventana, medio y pasillo).
- **Simulación de abordaje:** Modela el proceso de abordar, identificando interferencias comunes entre pasajeros.
- **Visualización gráfica:** Incluye gráficos que muestran la distribución de eventos de bloqueo para analizar patrones y resultados.
- **Flexible y extensible:** Puedes ajustar fácilmente el número de filas, asientos y grupos de abordaje para explorar diferentes escenarios.

## ¿Cómo funciona? 🧩

1. **Generar pasajeros:** Se crea una lista de pasajeros asignados aleatoriamente a asientos específicos (ventana, medio, pasillo).
2. **Asignar grupos:** Los pasajeros se dividen en grupos de abordaje, imitando estrategias comunes en aerolíneas.
3. **Simular abordaje:** Se modelan los eventos de bloqueo cuando pasajeros del pasillo obstaculizan a otros, calculando el impacto.
4. **Visualizar resultados:** Los datos se analizan y se grafican para identificar patrones y optimizar estrategias.

## Requisitos 📋

Para ejecutar este proyecto, necesitas:
- **Python 3.8+**
- Bibliotecas:
  - `numpy`
  - `matplotlib`

### Instalación de bibliotecas
Ejecuta este comando en tu terminal para instalar las dependencias necesarias:

```bash
pip install numpy matplotlib

