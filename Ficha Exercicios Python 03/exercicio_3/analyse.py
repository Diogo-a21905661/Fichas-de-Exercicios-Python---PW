import os

def calcula_tamanho_pasta(pasta):
    "Recebe o nome de uma pasta e calcula o tamanho total em MBytes dos ficheiros nela contidos."

    #print(pasta)
    #Utiliza o os.walk para encontrar o diretorio e, quando encontra, calcula o tamanho
    for root, dirs, files in os.walk('C:\\Users'):
        #print(files)

        if pasta in dirs:
            sizeFound = 0
            #print(pasta)

            #Go through file and add onto size of files
            for file in os.listdir(root + "\\" + pasta):
                sizeFound += os.path.getsize(root + "\\" + pasta + "\\" + file)

            return sizeFound

    return -1


def main():
    while True:
        dirName = input("Please write which directory you wish to search for. (Writing 'exit' will quit the program)\n")
        if dirName == "exit":
            break

        sizeFound = calcula_tamanho_pasta(dirName)
        if (sizeFound == -1):
            print("Directory was not found, please try again.")
        else:
            print(f"Directory was found, and its size was {sizeFound}.")

    print("Thank you for choosing our program.")


if __name__ == "__main__":
    main()