from analisa_ficheiro import calculos
from analisa_ficheiro import acessorio
import json

def main():
    "Extrai informação do ficheiro de texto e põe-na no ficheiro no formato json."

    txtFileName = acessorio.pede_nome()
    jsonFileName = acessorio.gera_nome(txtFileName)

    numberOfLetters = calculos.calcula_carateres(txtFileName)
    letterDictionary = calculos.calcula_ocorrencia_de_letras(txtFileName)
    largestWord = calculos.calcula_palavra_comprida(txtFileName)
    numberOfLines = calculos.calcula_linhas(txtFileName)

    data = {
        "File Name": txtFileName,
        "Number of Lines": numberOfLines,
        "Number of Letters": numberOfLetters,
        "Largest Word": largestWord,
        "Dictionary": letterDictionary
    }

    #Makes the file even if it doesnt exist
    with open(jsonFileName, 'w') as file:
        data = json.dumps(data)
        file.write(data)

if __name__ == "__main__":
    main()