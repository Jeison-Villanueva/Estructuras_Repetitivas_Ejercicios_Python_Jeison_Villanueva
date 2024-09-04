suma_positivos = 0

for _ in range(10):
    numero = int(input("Ingresa un número negativo: "))
    if numero < 0:
        numero = abs(numero)
    suma_positivos += numero

print(f"La suma de los números convertidos a positivos es: {suma_positivos}")

