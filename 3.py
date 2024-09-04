calificaciones = []

for _ in range(20):
    calificacion = float(input("Ingresa la calificación: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
max_calificacion = max(calificaciones)
min_calificacion = min(calificaciones)

print(f"Promedio: {promedio}")
print(f"Calificación más alta: {max_calificacion}")
print(f"Calificación más baja: {min_calificacion}")

