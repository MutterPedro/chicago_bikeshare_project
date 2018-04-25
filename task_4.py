def run(data_list):
    # TAREFA 4
    male = 0
    female = 0
    for data in data_list:
        if data[-2] == "Male":
            male += 1
        elif data[-2] == "Female":
            female += 1

    # Verificando o resultado
    print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
    print("Masculinos: ", male, "\nFemininos: ", female)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
    # -----------------------------------------------------
