def run(data_list):
    input("Aperte Enter para continuar...")
    # TAREFA 1
    print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
    for i in range(20):
        print(data_list[i])
    # Vamos mudar o data_list para remover o cabeçalho dele.
    data_list = data_list[1:]
    return data_list
