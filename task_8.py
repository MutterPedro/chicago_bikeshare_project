from task_5 import count_gender


def run(data_list):
    # TAREFA 8
    male, female = count_gender(data_list)
    print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
    print("male + female == len(data_list):", male + female == len(data_list))
    answer = "Porque alguns itens não possuem gênero."
    print("resposta:", answer)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
    # -----------------------------------------------------
