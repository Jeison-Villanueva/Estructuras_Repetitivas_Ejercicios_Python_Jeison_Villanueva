hombres = mujeres = suma_hombres = suma_mujeres = 0

n = int(input("Ingresa el número total de alumnos: "))

for _ in range(n):
    sexo = input("Ingresa el sexo (H/M): ").upper()
    edad = int(input("Ingresa la edad: "))
    
    if sexo == 'H':
        hombres += 1
        suma_hombres += edad
    elif sexo == 'M':
        mujeres += 1
        suma_mujeres += edad

if hombres > 0:
    print(f"Promedio de edad de hombres: {suma_hombres / hombres}")
if mujeres > 0:
    print(f"Promedio de edad de mujeres: {suma_mujeres / mujeres}")
print(f"Promedio de edad total: {(suma_hombres + suma_mujeres) / n}")
