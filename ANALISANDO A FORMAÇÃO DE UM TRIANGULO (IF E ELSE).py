print("-="*20)
print("\033[7;32;43mm Analisador de triangulos")
print("-="*20)
r1 = float(input("Primeiro segmento"))
r2 = float(input("Segundo segmento"))
r3 = float(input("Terceiro segmento"))
if r1 < r2 +r3 and r2 < r1 + r3 and r3< r1+r3:
    print("Os segmentos podem formar um tringulo")
else:
    print("Os segmentos não podem formar um triangulo")
    