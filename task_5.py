def count_gender(data_list):
    """
    Função para contar a quantidade de cada genero em uma lista de dados.
    Argumentos:
      data_list: Lista de dados.
    Retorna:
      Uma lista das quantidades do genero masculino e feminino respectivamente.
    """
    male = 0
    female = 0
    for data in data_list:
        if data[-2] == "Male":
            male += 1
        elif data[-2] == "Female":
            female += 1
    return [male, female]


def run(data_list):
    # TAREFA 5
    # Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

    print("\nTAREFA 5: Imprimindo o resultado de count_gender")
    print(count_gender(data_list))

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
    assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
    assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
        1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
    # -----------------------------------------------------
