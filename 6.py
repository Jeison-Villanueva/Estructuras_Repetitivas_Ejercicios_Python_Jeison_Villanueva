n = int(input("Ingresa el número total de personas en el salón: "))
hombres = 0
mujeres = 0

for _ in range(n):
    sexo = input("Ingresa el sexo (H/M): ").upper()
    if sexo == 'H':
        hombres += 1
    elif sexo == 'M':
        mujeres += 1

print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")


