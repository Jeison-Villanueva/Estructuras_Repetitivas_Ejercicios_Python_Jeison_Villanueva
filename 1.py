positivos = 0
negativos = 0
neutros = 0

for _ in range(20):
    numero = int(input("Ingresa un número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")