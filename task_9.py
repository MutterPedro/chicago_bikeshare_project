from task_3 import column_to_list


def run(data_list):
    # TAREFA 9
    # Você não deve usar funções prontas parTODO isso, como max() e min().
    trip_duration_list = [int(x) for x in column_to_list(data_list, 2)]
    trip_duration_list.sort()
    min_trip = trip_duration_list[0]
    max_trip = trip_duration_list[-1]
    mean_trip = sum(trip_duration_list) / len(trip_duration_list)
    median_trip = 0.
    if len(trip_duration_list) % 2 == 0:
        index = len(trip_duration_list) / 2
        median_trip = (trip_duration_list[index] + trip_duration_list[index - 1]) / 2
    else:
        median_trip = trip_duration_list[int(len(trip_duration_list) / 2)]

    print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
    print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
    assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
    assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
    assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
    # -----------------------------------------------------
