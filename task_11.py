from task_3 import column_to_list


def count_items(column_list):
    """
    Função para contar a quantidade itens em uma lista de dados.
    Argumentos:
      data_list: Lista de dados.
    Retorna:
      Uma tupla contendo os types dos items e quantidades dos itens respectivamente.
    """
    dictionary = {}
    for data in column_list:
        if not dictionary.get(data):
            dictionary[data] = 0
        dictionary[data] += 1
    return list(dictionary.keys()), list(dictionary.values())


def run(data_list):
    # TAREFA 12 - Desafio! (Opcional)
    # para que nós possamos usar essa função com outra categoria de dados.
    print("Você vai encarar o desafio? (yes ou no)")

    answer = "yes"

    if answer == "yes":
        # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
        column_list = column_to_list(data_list, -2)
        types, counts = count_items(column_list)
        print("\nTAREFA 11: Imprimindo resultados para count_items()")
        print("Tipos:", types, "Counts:", counts)
        assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
        assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
        # -----------------------------------------------------
