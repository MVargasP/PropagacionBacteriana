import numpy as np

def calculate_population(bacteria_strain,initial_state, days):
    #Obtengo la cantidad de estados que tendra esta bacteria 
    number_of_states =  bacteria_strain.life_expectancy + 1
    bacteria_in_state = [0] * number_of_states
    state_adult = bacteria_strain.life_expectancy - bacteria_strain.maturation_period
    # Cuente las bacterias iniciales en cada estado.
    for state in initial_state:
        bacteria_in_state[state] += 1

    for _ in range(days):
        # Calcular el recién nacido y la cantidad que se restablece a 3.
        new_born = bacteria_in_state[0]
        reset_to_three = bacteria_in_state[0]

        # Cambia los estados.
        #bacteria_in_state[0:4] = bacteria_in_state[1:5]
        bacteria_in_state[0:bacteria_strain.life_expectancy] = bacteria_in_state[1:bacteria_strain.life_expectancy + 1]
        # Actualice el estado 3 y 4.
        bacteria_in_state[state_adult] += reset_to_three
        bacteria_in_state[bacteria_strain.life_expectancy] = new_born * bacteria_strain.reproduction_rate

    return sum(bacteria_in_state)





##################################################################################################################
##################################################################################################################
##################################################################################################################
# OTHER TEST NO WORKING 

def calculate_population1(initial_state, days):
    # Convierte el estado inicial en una lista de bacterias, cada una representada por su contador interno
    bacteria = initial_state.copy()
    # Para cada día en el rango de días especificado  [2, 3, 3, 1, 2]
    for _ in range(days):
        new_bacteria = []  # Inicializa una nueva lista para almacenar las nuevas bacterias que se produzcan

        # Para cada bacteria en la lista de bacterias
        for i in range(len(bacteria)):
            # Si el contador de una bacteria llega a 0, se reproduce y se reinicia su contador a 3.
            if bacteria[i] == 0:
                bacteria[i] = 3
                # Dos nuevas bacterias nacen con un contador de 4
                new_bacteria.extend([4, 4])
            else:
                # Si no, disminuye el contador para cada bacteria
                bacteria[i] -= 1

        # Añade las nuevas bacterias a la población
        bacteria.extend(new_bacteria)

    # Devuelve la longitud de la lista de bacterias, que es igual a la población total
    return len(bacteria)

def calculate_population2(initial_state, days):
    bacteria = np.array(initial_state)

    for _ in range(days):
        bacteria = bacteria - 1

        fertile_indices = np.where(bacteria == -1)[0]
        bacteria[fertile_indices] = 3

        if len(fertile_indices) > 0:
            offspring = np.full((2*len(fertile_indices),), 4)
            bacteria = np.append(bacteria, offspring)

    return len(bacteria)

def calculate_populationv3(initial_state, days):
    #Inicialice una lista para almacenar el recuento de bacterias en cada estado.
    bacteria_in_state = [0, 0, 0, 0, 0]

    # Cuente las bacterias iniciales en cada estado.
    for state in initial_state:
        bacteria_in_state[state] += 1

    for _ in range(days):
        # Calcular el recién nacido y la cantidad que se restablece a 3.
        new_born = bacteria_in_state[0]
        reset_to_three = bacteria_in_state[0]

        # Cambia los estados.
        bacteria_in_state[0:4] = bacteria_in_state[1:5]

        # Actualice el estado 3 y 4.
        bacteria_in_state[3] += reset_to_three
        bacteria_in_state[4] = new_born * 2

    return sum(bacteria_in_state)
 







