print("\033[7;32;43m=-")
print("CALCULO DO SEU IMC")
print("\033[7;32;43m=-")

nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua  altura?"))
imc = peso / altura **2 
print("O seu imc é {}".format(imc))
if peso > 30 and 35 and 40:
    print("Obesidade")
else:
    print("Está normal")
if peso < 25 and 18.5 and 17.5:
    print("Magro")
else:
    print("Está normal")
if peso >= 20 and 25:
    print("Normal")
else:
    print("Está normal")
