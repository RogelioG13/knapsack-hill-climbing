import time
import os
import statistics
import matplotlib.pyplot as plt
from random import randint

from leer_instancia import Leer_Instancia
from hill_climbing import Hill_Climbing


CARPETA_RESULTS = "results"


if not os.path.exists(CARPETA_RESULTS):
    os.makedirs(CARPETA_RESULTS)


cantidad, profits, weights, capacidad = Leer_Instancia.leer_instancia()


algoritmos = {
    "Hill Climbing": "hill_climbing",
    "Vecinos Aleatorios": "hill_climbing_vecinos_aleatorios"
}


resultados_alg = {}


for nombre, metodo in algoritmos.items():

    print(f"\n===== {nombre} =====")

    resultados = []
    tiempos = []

    inicio_metodo = time.time()

    for i in range(30):

        inicio = [randint(0,1) for _ in range(cantidad)]

        start = time.time()

        hc = Hill_Climbing(cantidad, profits, weights, capacidad, inicio)

        solucion, evaluacion = getattr(hc, metodo)()

        end = time.time()

        tiempo = end - start

        resultados.append(evaluacion)
        tiempos.append(tiempo)

        print(f"Ejecucion {i+1}: Evaluacion={evaluacion:.2f}  Tiempo={tiempo:.4f}")


    fin_metodo = time.time()
    tiempo_total = fin_metodo - inicio_metodo


    print("\nResumen")

    print(f"Mejor evaluacion: {max(resultados):.2f}")
    print(f"Peor evaluacion: {min(resultados):.2f}")
    print(f"Promedio evaluacion: {sum(resultados)/len(resultados):.2f}")
    print(f"Desviacion estandar evaluacion: {statistics.stdev(resultados):.2f}")

    print()

    print(f"Tiempo promedio: {sum(tiempos)/len(tiempos):.4f}")
    print(f"Tiempo minimo: {min(tiempos):.4f}")
    print(f"Tiempo maximo: {max(tiempos):.4f}")
    print(f"Desviacion estandar tiempo: {statistics.stdev(tiempos):.4f}")

    print(f"\nTiempo total metodo: {tiempo_total:.4f}")

    resultados_alg[nombre] = resultados


plt.boxplot(resultados_alg.values())
plt.xticks(range(1, len(resultados_alg)+1), resultados_alg.keys())
plt.title("Comparacion de algoritmos")
plt.ylabel("Evaluacion")

ruta = os.path.join(CARPETA_RESULTS, "boxplot_resultados.png")

plt.savefig(ruta)
