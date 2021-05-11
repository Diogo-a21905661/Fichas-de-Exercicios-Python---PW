class Automovel(): #Definição de classe

    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo


    def setCap(self, cap_dep):
        "Permite mudar o valor da capacidade do carro."
        self.cap_dep = cap_dep


    def setQuant(self, quant_comb):
        "Permite mudar o valor da quantidade de combustivel."
        if quant_comb > self.cap_dep:
            return -1

        self.quant_comb = quant_comb
        return 0


    def setConsumo(self, consumo):
        "Permite mudar o valor do consumo."
        self.consumo = consumo


    def combustivel(self):
        "Retorna a quantidade de combustivel no depósito."
        return self.quant_comb


    def capacidade(self):
        "Retorna a capacidade do automóvel."
        return self.cap_dep


    def cons(self):
        "Retorna o consumo do automóvel."
        return self.consumo


    def autonomia(self):
        "Devolve o número de Km que é possivel percorrer com o combustivel no depósito."
        return int(self.quant_comb / self.consumo * 100)


    def abastece(self, n_litros):
        "Aumenta em ´n_litros' o combustivel no depósito e retorna a sua autonomia."

        if n_litros + self.quant_comb > self.cap_dep:
            print("O abastecimento foi acima da capacidade do Automóvel!")
            return -1
        else:
            self.quant_comb += n_litros

        return self.autonomia()


    def percorre(self, n_km):
        "Percorre 'n_km' Km, desde que a quantidade de combustivel no depósito o permita."

        if (n_km * self.consumo) / 100 > self.quant_comb:
            print("Não temos o combustivel suficiente para efetuar esse trajecto.")
            return -1
        else:
            self.quant_comb -= (n_km * self.consumo) / 100

        return self.autonomia()


def menu():
    print("---------------------Menu Automóvel---------------------")
    print("'Check' - Verifica todas as variáveis aos mesmo tempo.\n")
    print("-----------------(Criação do Automóvel)-----------------")
    print("1. Mudança da Capacidade do Depósito.")
    print("2. Mudança da Quantidade de Combustivel Atual.")
    print("3. Mudança do Consumo.")
    print("--------------(Visualização do Automóvel)---------------")
    print("4. Visualização da Capacidade do Depósito.")
    print("5. Visualização da Quantidade de Combustivel Atual.")
    print("6. Visualização do Consumo.")
    print("-----------------(Execução de Funções)------------------")
    print("7. Autonomia do Automóvel.")
    print("8. Abastecimento do Automóvel.")
    print("9. Percorrer Kms com o Automóvel.")
    print("\n---------------------Menu Automóvel---------------------")


def checkCarMade(carro):
    "Vê se o carro já foi criado."
    if carro.combustivel() == 0 or carro.capacidade() == 0 or carro.cons() == 0:
        return -1

    return 1


def getValue():
    value = input("Introduza o valor que quer utilizar:\n")
    value = int(value)

    return value


def checkChoices(choice, carro):
    if choice == 1:
        value = getValue()

        carro.setCap(value)

    elif choice == 2:
        value = getValue()

        if carro.setQuant(value) == -1:
            print("Quantidade de Combustivel inserida vai acima da capacidade do Carro.")

    elif choice == 3:
        value = getValue()

        carro.setConsumo(value)

    elif choice == 4:
        print("Capacidade == " + str(carro.capacidade()))

    elif choice == 5:
        print("Quantidade == " + str(carro.combustivel()))

    elif choice == 6:
        print("Consumo == " + str(carro.cons()))

    elif choice == 7:
        if checkCarMade(carro) == -1:
            return -1

        print("Calculo da Autonomia == " + str(carro.autonomia()))

    elif choice == 8:
        if checkCarMade(carro) == -1:
            return -1

        value = getValue()

        carro.abastece(value)
        print("Combustivel no Momento == " + str(carro.combustivel()))

    elif choice == 9:
        if checkCarMade(carro) == -1:
            return -1

        value = getValue()

        carro.percorre(value)
        print("Combustivel no Momento == " + str(carro.combustivel()))

    return 1


def main():
    carro = Automovel(0, 0, 0)
    print("Bem vindo à criação e gestão de um Automóvel, através de um menu.\n")

    while True:
        menu()

        choice = input("\nPor favor introduza uma escolha: (escreva 'exit' para sair)\n")
        if choice == "exit":
            break

        elif choice == "Check":
            print("\n")
            print("Capacidade == " + str(carro.capacidade()))
            print("Quantidade == " + str(carro.combustivel()))
            print("Consumo == " + str(carro.cons()))
            print("\n")
            continue

        elif not choice.isnumeric():
            print("Value given was not valid, please try again.")
            continue

        choice = int(choice)
        if choice < 1 or choice > 9:
            print("Please insert a valid choice.\n")
            continue

        if checkChoices(choice, carro) == -1:
            print("Carro ainda não foi criado.")

    print("\n\n")
    print("Muito obrigado por utilizar o nosso programa.")


if  __name__ == "__main__":
    main()