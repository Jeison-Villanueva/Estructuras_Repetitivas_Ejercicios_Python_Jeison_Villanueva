menos_50 = 0
entre_50_69 = 0
entre_70_79 = 0
mas_80 = 0

for _ in range(23):
    calificacion = float(input("Ingresa la calificación del estudiante: "))

    if calificacion < 50:
        menos_50 += 1
    elif 50 <= calificacion < 70:
        entre_50_69 += 1
    elif 70 <= calificacion < 80:
        entre_70_79 += 1
    else:
        mas_80 += 1

print(f"Menos de 50: {menos_50}")
print(f"Entre 50 y 69: {entre_50_69}")
print(f"Entre 70 y 79: {entre_70_79}")
print(f"Más de 80: {mas_80}")
