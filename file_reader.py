import csv


def read(filename):
    # Vamos ler os dados como uma lista
    print("Lendo o documento...")
    with open(filename, "r") as file_read:
        reader = csv.reader(file_read)
        data_list = list(reader)
    print("Ok!")
    return data_list
