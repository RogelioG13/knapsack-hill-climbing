import time
from random import randint
from leer_instancia import Leer_Instancia
from hill_climbing import Hill_Climbing

inicio_global = time.time()

cantidad, profits, weights, capacidad = Leer_Instancia.leer_instancia()

resultados = []
tiempos = []

mejor_global = float("-inf")
mejor_solucion = None

for i in range(30):

    inicio = [randint(0,1) for _ in range(cantidad)]

    start = time.time()
    solucion, evaluacion = Hill_Climbing(cantidad, profits, weights, capacidad, inicio).hill_climbing()
    end = time.time()

    tiempo = end - start

    resultados.append(evaluacion)
    tiempos.append(tiempo)

    print(f"Ejecucion {i+1}: Evaluacion={evaluacion}  Tiempo={tiempo:.4f}")

    if evaluacion > mejor_global:
        mejor_global = evaluacion
        mejor_solucion = solucion

fin_global = time.time()
total_global = fin_global - inicio_global

print(f"\nResumen")

print(f"Mejor evaluacion: {max(resultados)}")
print(f"Peor evaluacion: {min(resultados)}")
print(f"Promedio evaluacion: {sum(resultados)/len(resultados)}")

print(f"\nTiempo promedio: {sum(tiempos)/len(tiempos):.4f}")
print(f"Tiempo minimo: {min(tiempos):.4f}")
print(f"Tiempo maximo: {max(tiempos):.4f}")
print(f"Tiempo total: {total_global:.4f}")

print(f"\nMejor solucion encontrada:")
print(f"{mejor_solucion}")
