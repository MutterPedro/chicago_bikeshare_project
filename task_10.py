from task_3 import column_to_list


def run(data_list):
    # TAREFA 10
    start_stations = set(column_to_list(data_list, 3))

    print("\nTAREFA 10: Imprimindo as start stations:")
    print(len(start_stations))
    print(start_stations)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
    # -----------------------------------------------------
