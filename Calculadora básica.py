print(" ------------ Bem vindo a calculadora ------------")
a = float(input("Digite o primeiro numero: "))
b = str(input("Qual a expressão númerica a ser usada: "))
c = float(input("Qual o segundo número: "))

def calculdora():

    if b == "+":
        return float(a) + float(c)
    elif b == "-":
        return float(a) - float(c)    
    elif b == "*":        
        return float(a) * float(c)
    elif b == "/":
        return float(a) / float(c)    
    else:
        return "Opção inválida" 
    

print(calculdora())
print(" ------------ Fim da Calculadora ------------")