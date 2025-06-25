salario = float(input("qual o seu salario?"))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
    print("Seu salario com aumento de 15% ficou em",salario)
else:
    salario = salario + (salario * 10 / 100)
    print("Seu salario com aumento de 10% ficou em",salario)
