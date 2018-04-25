import matplotlib.pyplot as plt
from task_3 import column_to_list
from task_5 import count_gender


def most_popular_gender(data_list):
    """
    Função para encontrar o gênero mais popular.
    Argumentos:
      data_list: Lista de dados.
    Retorna:
      Uma string do gênero mais popular ou igual.
    """
    male, female = count_gender(data_list)
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


def run(data_list):
    # TAREFA 6
    # esperamos ver "masculino", "feminino", ou "igual" como resposta.

    print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
    print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(
        most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
    assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    # Se tudo está rodando como esperado, verifique este gráfico!
    gender_list = column_to_list(data_list, -2)
    types = ["Male", "Female"]
    quantity = count_gender(data_list)
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantidade')
    plt.xlabel('Gênero')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Gênero')
    plt.show(block=True)
