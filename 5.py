niños = 0
jóvenes = 0
adultos = 0
ancianos = 0
total_niños = total_jóvenes = total_adultos = total_ancianos = 0

for _ in range(50):
    edad = int(input("Ingresa la edad: "))
    peso = float(input("Ingresa el peso: "))

    if 0 <= edad <= 12:
        niños += 1
        total_niños += peso
    elif 13 <= edad <= 29:
        jóvenes += 1
        total_jóvenes += peso
    elif 30 <= edad <= 59:
        adultos += 1
        total_adultos += peso
    else:
        ancianos += 1
        total_ancianos += peso

if niños > 0:
    print(f"Promedio de peso de niños: {total_niños / niños}")
if jóvenes > 0:
    print(f"Promedio de peso de jóvenes: {total_jóvenes / jóvenes}")
if adultos > 0:
    print(f"Promedio de peso de adultos: {total_adultos / adultos}")
if ancianos > 0:
    print(f"Promedio de peso de ancianos: {total_ancianos / ancianos}")
