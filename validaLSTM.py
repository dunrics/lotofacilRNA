#FUNCIONAL#
#Esse código abre o arquivo 'output.csv' e analise se os jogos previstos estão 'OK' ou 'Inválidos' 
#seguindo como critério os requisitos abaixo:
#Ao somar os números previstos, a somatória deve estar entre 171 e 220 (média de somatória de sorteios passados)
#Caso a previsão tenha números iguais ou igual a '0'
import csv

def sum_numbers(line):
    numbers = line[1:-1].split()
    numbers = [int(num) for num in numbers]
    total = sum(numbers)
    return total

def check_validity(numbers):
    if 0 in numbers or len(set(numbers)) != len(numbers):
        return False
    return True

def process_file(filename):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Volta para o início do arquivo para sobrescrever os resultados

        for line in lines:
            line = line.strip()
            if line.startswith("Resultado"):
                file.write(line + "\n")
                continue  # Pula para a próxima iteração do loop

            numbers = line[1:-1].split()
            numbers = [int(num) for num in numbers]

            if not check_validity(numbers):
                file.write(f"{line} = {sum(numbers)} --> Jogo Inválido\n")
            else:
                total = sum_numbers(line)
                file.write(f"{line} = {total} --> OK!\n")

        file.truncate()  # Remove qualquer conteúdo restante no arquivo

# Nome do arquivo CSV a ser processado
filename = 'C:\\Users\\Vandinho\\Documents\\Loteria_Projekt_V2\\Dados_Output\\outputRNA.csv'

# Chama a função para processar o arquivo
process_file(filename)
