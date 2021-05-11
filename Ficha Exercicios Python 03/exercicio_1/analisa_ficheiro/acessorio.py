import json

def pede_nome():
    "Pede e retorna o nome de um ficheiro \".txt\" existente."

    while True:
        fileName = input("Por favor introduza um ficheiro de texto.\n")

        fileSplit = fileName.split(".", 2)
        if len(fileSplit) != 2 or fileSplit[1] != "txt":
            print("Input file format not supported.")
            continue

        try:
            #Como utilizamos o "with" não necessitamos de fechar o ficheiro
            with open(fileName, 'r') as file:
                return fileName

        except OSError:
            print("File not found.")

def gera_nome(fileName):
    "Recebe o nome de um ficheiro e cria um ficheiro onde irá guardar os resultados da analise do ficheiro (em formato json)."

    fileSplit = fileName.split(".", 2)
    if len(fileSplit) != 2 or fileSplit[1] != "txt":
        print("Wrong argument was inserted.")
        return None

    newFileName = fileSplit[0] + ".json"
    return newFileName