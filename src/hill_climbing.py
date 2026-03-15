import random
class Hill_Climbing:
    def __init__(self, cantidad, profits, weights, capacidad, solucion_inicial):
        self.cantidad = cantidad
        self.profits = profits
        self.weights = weights
        self.capacidad = capacidad
        self.solucion_inicial = solucion_inicial

    def generar_vecino(self, solucion, index):
        vecino = solucion.copy()
        if vecino[index] == 0:
            vecino[index] = 1
        else:
            vecino[index] = 0
        return vecino, vecino[index]
    
    def evaluar_solucion_inicial(self, solucion):
        profit = 0
        weight = 0
        for i in range(self.cantidad):
            if solucion[i]:
                profit += self.profits[i]
                weight += self.weights[i]
        exceso = max(0, weight - self.capacidad)
        return profit - 50000 * exceso, profit, weight

    
    def evaluar_vecino(self, nuevo_valor, weight_actual, profit_actual, index):

        if nuevo_valor == 1:
            profit_vecino = profit_actual + self.profits[index]
            weight_vecino = weight_actual + self.weights[index]
        else:
            profit_vecino = profit_actual - self.profits[index]
            weight_vecino = weight_actual - self.weights[index]

        exceso = max(0, weight_vecino - self.capacidad)
        evaluacion_vecino = profit_vecino - 50000 * exceso
        return evaluacion_vecino, profit_vecino, weight_vecino

    def hill_climbing(self):
        solucion_actual = self.solucion_inicial
        evaluacion_actual, profit_actual, weight_actual = self.evaluar_solucion_inicial(solucion_actual)
        j = 0
        while j < 50:

            mejor_vecino = None
            mejor_eval_vecino = evaluacion_actual
            mejor_profit_vecino = profit_actual
            mejor_weight_vecino = weight_actual

            for i in range(self.cantidad):

                vecino, nuevo_valor = self.generar_vecino(solucion_actual, i)
                evaluacion_vecino, profit_vecino, weight_vecino = self.evaluar_vecino(nuevo_valor, weight_actual, profit_actual, i)

                if evaluacion_vecino > mejor_eval_vecino:
                    mejor_eval_vecino = evaluacion_vecino
                    mejor_vecino = vecino
                    mejor_profit_vecino = profit_vecino
                    mejor_weight_vecino = weight_vecino
            if mejor_vecino is None:
                break

            solucion_actual = mejor_vecino
            evaluacion_actual = mejor_eval_vecino
            profit_actual = mejor_profit_vecino
            weight_actual = mejor_weight_vecino

            j += 1

        return solucion_actual, evaluacion_actual
    
    def hill_climbing_vecinos_aleatorios(self):
        solucion_actual = self.solucion_inicial
        evaluacion_actual, profit_actual, weight_actual = self.evaluar_solucion_inicial(solucion_actual)
        j = 0
        buenos_vecinos = []
        while j < 50:

            buenos_vecinos = []

            for i in range(self.cantidad):
                vecino, nuevo_valor = self.generar_vecino(solucion_actual, i)
                evaluacion_vecino, profit_vecino, weight_vecino = self.evaluar_vecino(nuevo_valor, weight_actual, profit_actual, i)
                if evaluacion_vecino > evaluacion_actual:
                    buenos_vecinos.append([vecino, evaluacion_vecino, profit_vecino, weight_vecino])
            if len(buenos_vecinos) == 0:
                break
            vecino = random.choice(buenos_vecinos)
            solucion_actual = vecino[0]
            evaluacion_actual = vecino[1]
            profit_actual = vecino[2]
            weight_actual = vecino[3]

            j += 1

        return solucion_actual, evaluacion_actual