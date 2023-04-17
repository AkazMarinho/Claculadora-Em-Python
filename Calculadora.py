import os

sair = "n"
while(sair == "n"):
    os.system("cls")

    print("------- calculadora em Python -------\n\n")
    num1 = int(input("Insira o primeiro valor a ser calculado: "))
    num2 = int(input("Insira o segundo valor a ser calculado: "))
    res = 0

    op = input("Insira a operação: ")

    print("\n")
    if op == "+":
        res = num1 + num2
        print("A soma dos dois numeros é: " + str(res))
    elif op == "-":
        res = num1 - num2
        print("A subtração dos dois numeros é: " + str(res))
    elif op == "*":
        res = num1 * num2
        print("A multiplicação dos dois numeros é: " + str(res))
    elif op == "/":
        res = num1 / num2
        print("A divisão dos dois numeros é: " + str(res))
    else:
        print("Operação inválida")


    checagem =  input("\nDeseja sair(s/n ): ")

    if(checagem == "s"):
        sair = "s"
        
    elif (checagem != "s" and checagem != "n"):
        print("Comando incorreto")

print("Fim do programa")
       