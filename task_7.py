import matplotlib.pyplot as plt
from task_3 import column_to_list


def run(data_list):
    # TAREFA 7
    print("\nTAREFA 7: Verifique o gráfico!")
    user_types = column_to_list(data_list, -3)
    types = ["Subscriber", "Customer"]
    subscribers = 0
    customers = 0

    for user_type in user_types:
        if user_type == "Subscriber":
            subscribers += 1
        elif user_type == "Customer":
            customers += 1

    y_pos = list(range(len(types)))
    plt.bar(y_pos, [subscribers, customers])
    plt.ylabel('Quantidade')
    plt.xlabel('Tipo')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Tipo de Usuário')
    plt.show(block=True)
