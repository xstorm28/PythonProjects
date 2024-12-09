import numpy as np

#Creación del array de calificaciones
calificaciones = np.array([
    [80, 94, 70],  # Estudiante 1, Parcial 1,2,3
    [78, 60, 80],  # Estudiante 2, Parcial 1,2,3
    [92, 85, 99],  # Estudiante 3, Parcial 1,2,3
    [70, 82, 80],  # Estudiante 4, Parcial 1,2,3
    [70, 92, 97]   # Estudiante 5, Parcial 1,2,3
])
#Promedio Final grupo
promedio_final_grupo = np.mean(calificaciones)

#Calificación final más alta del grupo.
promedio_individual = np.mean(calificaciones, axis=1)
calificacion_mas_alta_final = np.max(promedio_individual)

#Calificación final más baja del grupo.
calificacion_mas_baja_final = np.min(promedio_individual)

#Calificación más alta del primer parcial.
calificacion_mas_alta_parcial1 = np.max(calificaciones[:, 0])

#Calificación más baja del segundo parcial.
calificacion_mas_baja_parcial2 = np.min(calificaciones[:, 1])
#Impresión
print("Resumen Estadístico de Calificaciones".center(50, "="))
print(f"Promedio final del grupo: {promedio_final_grupo:.2f}")
print(f"Calificación final más alta del grupo: {calificacion_mas_alta_final:.2f}")
print(f"Calificación final más baja del grupo: {calificacion_mas_baja_final:.2f}")
print(f"Calificación más alta del primer parcial: {calificacion_mas_alta_parcial1}")
print(f"Calificación más baja del segundo parcial: {calificacion_mas_baja_parcial2}")
print("=".center(50, "="))

