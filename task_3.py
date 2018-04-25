def column_to_list(data, index):
    """
    Função para pegar um certo atributo dos dados.
    Argumentos:
      data: lista de dados.
      index: indice do atributo desejado.
    Retorna:
      Uma lista dos atributos desejados.
    """
    return [d[index] for d in data]


def run(data_list):
    # TAREFA 3

    # Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
    print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
    print(column_to_list(data_list, -2)[:20])

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
    assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
    assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
        1] == "Male", "TAREFA 3: A lista não coincide."
    # -----------------------------------------------------
