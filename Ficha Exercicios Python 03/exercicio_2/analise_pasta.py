import os
import csv
from matplotlib import pyplot as plt


def pede_pasta():
    "Pede ao utilizador para inserir um caminho para uma pasta."

    #Ask for an input, in the format of a path, and only accept one that exists
    while True:
        path = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta:\n")

        if os.path.exists(path):
            break

        print("Given Path was not found.")

    #print(path)
    return path


def faz_calculos(path):
    "Contabiliza a quantidade de ficheiros e o volume total ocupado em kBytes."

    #Path given in arguments was not found
    if not os.path.exists(path):
        print("Given Path was not found.")
        return None

    dic_info = dict()
    list_info = os.listdir(path)
    for file in list_info:
        #Get the size in kBytes
        size = os.path.getsize(path + '\\' + file)

        #Split for the file type ([0] is file name)
        fileSplit = file.split(".", 2)
        fileType = fileSplit[1]

        #Add the size and the volume based on the file type, and if they exist already
        if fileType in dic_info:
            dic_info[fileType]['volume'] += size
            dic_info[fileType]['quantidade'] += 1
        else:
            dic_info[fileType] = dict()
            dic_info[fileType]['volume'] = size
            dic_info[fileType]['quantidade'] = 1

    #print(dic_info)
    return dic_info


def guarda_resultados(path, dic_info):
    "Guarda informação num ficheiro CSV e indica na consola o nome do ficheiro com resultados."

    # Path given in arguments was not found
    if not os.path.exists(path):
        print("Given info was not made.")
        return None

    # Info given in arguments was not made
    if dic_info == None:
        print("Given info was not made.")
        return None

    #Get directory name
    dirSplit = path.split("\\")
    dirName = dirSplit[-1]
    fileName = dirName + ".csv"
    #print(dirName)

    #Open and make .csv file, and write initial line into it
    with open(fileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Extensao","Quantidade","Tamanho[kByte]"])

        #Write info depending on dictionary given in arguments
        for type,info in dic_info.items():
            writer.writerow([type, info['quantidade'], info['volume']])

    print(f"Os resultados foram guardados no ficheiro '{fileName}'.")
    return


def faz_grafico_queijos(dic_info):
    "Representa os resultados numa pie chart."

    #Decide o estilo utilizado pelo pie chart
    plt.style.use("fivethirtyeight")

    #Get info out of dictionary
    typeData = list()
    amountData = list()
    for type, info in dic_info.items():
        typeData.append(type)
        amountData.append(info['quantidade'])

    #Create and show the pie chart
    plt.pie(amountData, labels=typeData, startangle=90, autopct='%1.1f%%')
    plt.title("Quantity of Types Found")
    plt.tight_layout()
    plt.show()
    return


def faz_grafico_barras(dic_info):
    "Representa os resultados num gráfico de barras."

    #Decide o estilo utilizado pelo pie chart
    plt.style.use("fivethirtyeight")

    #Get info out of dictionary
    typeData = list()
    amountData = list()
    for type, info in dic_info.items():
        typeData.append(type)
        amountData.append(info['volume'])

    #print(typeData)
    #print(amountData)

    #Create and show the bar graph
    plt.bar(typeData, amountData)
    plt.title("Amount of bytes per File Type")
    plt.show()
    return