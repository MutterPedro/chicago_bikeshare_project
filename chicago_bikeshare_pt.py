# coding: utf-8
from sys import argv
import file_reader
import task_0
import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
import task_8
import task_9
import task_10
import task_11


data_list = file_reader.read(argv[1] or "chicago.csv")
task_0.run(data_list)

data_list = task_1.run(data_list)
input("Aperte Enter para continuar...")

task_2.run(data_list)
input("Aperte Enter para continuar...")

task_3.run(data_list)
input("Aperte Enter para continuar...")

task_4.run(data_list)
input("Aperte Enter para continuar...")

task_5.run(data_list)
input("Aperte Enter para continuar...")

task_6.run(data_list)
input("Aperte Enter para continuar...")

task_7.run(data_list)
input("Aperte Enter para continuar...")

task_8.run(data_list)
input("Aperte Enter para continuar...")

task_9.run(data_list)
input("Aperte Enter para continuar...")

task_10.run(data_list)
input("Aperte Enter para continuar...")

# TAREFA 11 Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída,
# e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#   """ Função de exemplo com
#   anotações. Argumentos: param1: O primeiro parâmetro. param2: O segundo parâmetro. Retorna: Uma lista de valores x.
#
#   """
input("Aperte Enter para continuar...")

task_11.run(data_list)
input("Fim do programa. Aperte Enter para sair...")
