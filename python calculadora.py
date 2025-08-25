def calculadora():
    while True:
        tipo_operacao = input('''Digite o tipo da sua operação:
"1 - Soma"
"2 - Subtração" 
"3 - Multiplicação" 
"4 - Divisão"
"0 - Sair"
''')

        if tipo_operacao == '0':
            print("Encerrando a calculadora...")
            break

        num1 = float(input("Digite seu primeiro número:"))
        num2 = float(input("Digite seu segundo número:"))

        if tipo_operacao == '1':
            resultado = num1 + num2
            print(resultado)
        elif tipo_operacao == '2':
            resultado = num1 - num2
            print(resultado)
        elif tipo_operacao == '3':
            resultado = num1 * num2
            print(resultado)
        elif tipo_operacao == '4':
            if num2 == 0:
                print("Erro: não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(resultado)
        else:
            print("Operação inválida!")

        print(f"O resultado da sua operação é: {resultado}")
calculadora()