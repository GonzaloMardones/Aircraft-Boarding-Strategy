import numpy as np
import matplotlib.pyplot as plt 

# Configuración inicial
NUM_ROWS = 30  # Número de filas en el avión
SEATS_PER_ROW = 3  # Asientos por lado (ventana, medio, pasillo)
BOARDING_GROUPS = 3  # Número de grupos de abordaje

# Simulación de pasajeros y sus asientos
def generate_passengers(num_rows, seats_per_row):
    seats = ["W", "M", "A"]  # Ventana, Medio, Pasillo
    passengers = [(row, seat) for row in range(1, num_rows + 1) for seat in seats]
    np.random.shuffle(passengers)
    return passengers

# Asignar pasajeros a grupos de abordaje
def assign_boarding_groups(passengers, num_groups):
    return np.array_split(passengers, num_groups)

# Simulación del abordaje
def simulate_boarding(boarding_groups):
    seated_passengers = set()
    blocking_events = 0

    for group in boarding_groups:
        for row, seat in group:
            if seat == "M": 
                if (row, "A") not in seated_passengers:
                    blocking_events += 1
            seated_passengers.add((row, seat))

    return blocking_events

# Simulación completa
def run_simulation(num_simulations, num_rows, seats_per_row, num_groups):
    blocking_events = np.zeros(num_simulations)
    
    for i in range(num_simulations):
        passengers = generate_passengers(num_rows, seats_per_row)
        boarding_groups = assign_boarding_groups(passengers, num_groups)
        blocking_events[i] = simulate_boarding(boarding_groups)

    return blocking_events

# Función para representar gráficamente los resultados
def plot_results(blocking_events):
    # Histograma de eventos de bloqueo
    plt.figure(figsize=(10, 6))
    plt.hist(blocking_events, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Distribución de Eventos de Bloqueo en el Embarque', fontsize=14)
    plt.xlabel('Número de Eventos de Bloqueo', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Configuración de parámetros y ejecución
NUM_SIMULATIONS = 1000
blocking_events = run_simulation(NUM_SIMULATIONS, NUM_ROWS, SEATS_PER_ROW, BOARDING_GROUPS)

# Promedio de eventos de bloqueo
average_blocking_events = np.mean(blocking_events)
print(f"Promedio de eventos de bloqueo por abordaje: {average_blocking_events:.2f}")

# Visualización de resultados
plot_results(blocking_events)
