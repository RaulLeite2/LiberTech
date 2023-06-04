import random

def calcular(a, b):
    c = random.randint(a, b)
    resultado = a + b
    if resultado == 10:
        print("A soma de A e B é 10")
        print(f"O número aleatório gerado entre {a} e {b} é {c}")
    return resultado
