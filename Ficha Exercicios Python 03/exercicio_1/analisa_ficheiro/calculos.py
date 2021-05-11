def calcula_linhas(fileName):
    "Recebe o nome de um ficheiro e retorna o número de linhas do ficheiro."

    fileSplit = fileName.split(".", 2)
    if len(fileSplit) != 2 or fileSplit[1] != "txt":
        print("Input file format not supported.")
        return None

    try:
        count = 0

        #Como utilizamos o "with" não necessitamos de fechar o ficheiro
        with open(fileName, 'r') as file:
            while True:
                line = file.readline()
                if line == "":
                    break

                count += 1

        #print(count)
        return count

    except OSError:
        print("File not found.")

    return None

def calcula_carateres(fileName):
    "Calcula o número de caracteres de um ficheiro."

    fileSplit = fileName.split(".", 2)
    if len(fileSplit) != 2 or fileSplit[1] != "txt":
        print("Input file format not supported.")
        return None

    try:
        count = 0

        # Como utilizamos o "with" não necessitamos de fechar o ficheiro
        with open(fileName, 'r') as file:
            while True:
                line = file.readline()
                if line == "":
                    break

                count += len(line)

        #print(count)
        return count

    except OSError:
        print("File not found.")

    return None

def calcula_palavra_comprida(fileName):
    "Retorna a palavra mais comprida do ficheiro."

    fileSplit = fileName.split(".", 2)
    if len(fileSplit) != 2 or fileSplit[1] != "txt":
        print("Input file format not supported.")
        return None

    try:
        maxSize = 0
        maxWord = ""

        # Como utilizamos o "with" não necessitamos de fechar o ficheiro
        with open(fileName, 'r') as file:
            while True:
                line = file.readline()
                if line == "":
                    break

                lineSplit = line.split(" ")
                for word in lineSplit:
                    if len(word) > maxSize:
                        maxSize = len(word)
                        maxWord = word

        #print(maxSize)
        #print(maxWord)
        return maxWord

    except OSError:
        print("File not found.")

    return None

def calcula_ocorrencia_de_letras(fileName):
    "Cria um dicionário de todas as letras do ficheiro, indicando a quantidade de vezes que cada letra ocorre."

    fileSplit = fileName.split(".", 2)
    if len(fileSplit) != 2 or fileSplit[1] != "txt":
        print("Input file format not supported.")
        return None

    try:
        letterCountDict = dict()

        # Como utilizamos o "with" não necessitamos de fechar o ficheiro
        with open(fileName, 'r') as file:
            while True:
                line = file.readline()
                if line == "":
                    break

                for letter in line:
                    letter = letter.lower()
                    if letter == ' ':
                        continue

                    if letter in letterCountDict:
                        letterCountDict[letter] += 1
                    else:
                        letterCountDict[letter] = 0

        #print(letterCountDict)
        return letterCountDict

    except OSError:
        print("File not found.")

    return None