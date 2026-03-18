import random

class Hill_Climbing:
    """
    Clase que implementa el algoritmo Hill Climbing para resolver el 
    problema de la mochila 0/1 mediante búsqueda local.
    """
    def __init__(self, cantidad, profits, weights, capacidad, solucion_inicial):
        """
        Inicializa los parámetros del problema.
        
        Args:
            cantidad (int): Número total de objetos.
            profits (list): Lista de beneficios de cada objeto.
            weights (list): Lista de pesos de cada objeto.
            capacidad (int): Capacidad máxima de la mochila.
            solucion_inicial (list): Lista binaria representando el estado inicial.
        """
        self.cantidad = cantidad
        self.profits = profits
        self.weights = weights
        self.capacidad = capacidad
        self.solucion_inicial = solucion_inicial

    def generar_vecino(self, solucion, index):
        """
        Genera un vecino cambiando exactamente 1 bit (vecindario de flip). [cite: 70]
        """
        vecino = solucion.copy()
        # Cambia el estado del objeto en el índice dado (0 a 1 o 1 a 0)
        vecino[index] = 1 if vecino[index] == 0 else 0
        return vecino, vecino[index]
    
    def evaluar_solucion_inicial(self, solucion):
        """
        Calcula el beneficio y peso total inicial, aplicando la función de penalización.
        """
        profit = 0
        weight = 0
        for i in range(self.cantidad):
            if solucion[i]:
                profit += self.profits[i]
                weight += self.weights[i]
        
        # Función objetivo con penalización proporcional al exceso de peso [cite: 58, 59]
        exceso = max(0, weight - self.capacidad)
        evaluacion = profit - 50000 * exceso
        return evaluacion, profit, weight

    def evaluar_vecino(self, nuevo_valor, weight_actual, profit_actual, index):
        """
        Evalúa de forma incremental un cambio en la solución para ahorrar cómputo.
        """
        if nuevo_valor == 1:
            profit_vecino = profit_actual + self.profits[index]
            weight_vecino = weight_actual + self.weights[index]
        else:
            profit_vecino = profit_actual - self.profits[index]
            weight_vecino = weight_actual - self.weights[index]

        # Aplicación de la penalización sugerida [cite: 29, 32]
        exceso = max(0, weight_vecino - self.capacidad)
        evaluacion_vecino = profit_vecino - 50000 * exceso
        return evaluacion_vecino, profit_vecino, weight_vecino

    def hill_climbing(self):
        """
        Variante: Búsqueda del mejor vecino.
        Evalúa todos los vecinos y elige el de mayor costo penalizado. [cite: 62, 63]
        """
        solucion_actual = self.solucion_inicial
        evaluacion_actual, profit_actual, weight_actual = self.evaluar_solucion_inicial(solucion_actual)
        j = 0
        
        # Límite de 50 iteraciones para control de tiempo [cite: 67]
        while j < 50:
            mejor_vecino = None
            mejor_eval_vecino = evaluacion_actual
            mejor_profit_vecino = profit_actual
            mejor_weight_vecino = weight_actual

            # Exploración exhaustiva del vecindario de 1 bit
            for i in range(self.cantidad):
                vecino, nuevo_valor = self.generar_vecino(solucion_actual, i)
                evaluacion_vecino, profit_vecino, weight_vecino = self.evaluar_vecino(
                    nuevo_valor, weight_actual, profit_actual, i
                )

                # Criterio de mejora estricta
                if evaluacion_vecino > mejor_eval_vecino:
                    mejor_eval_vecino = evaluacion_vecino
                    mejor_vecino = vecino
                    mejor_profit_vecino = profit_vecino
                    mejor_weight_vecino = weight_vecino
            
            # Si ningún vecino mejora la solución actual, se ha alcanzado un óptimo local
            if mejor_vecino is None:
                break

            solucion_actual = mejor_vecino
            evaluacion_actual = mejor_eval_vecino
            profit_actual = mejor_profit_vecino
            weight_actual = mejor_weight_vecino
            j += 1

        return solucion_actual, evaluacion_actual
    
    def hill_climbing_vecinos_aleatorios(self):
        """
        Variante: Búsqueda aleatoria entre mejores vecinos.
        Elige aleatoriamente uno de los vecinos que mejoren la solución actual. [cite: 64, 65]
        """
        solucion_actual = self.solucion_inicial
        evaluacion_actual, profit_actual, weight_actual = self.evaluar_solucion_inicial(solucion_actual)
        j = 0
        
        while j < 50:
            buenos_vecinos = []

            # Identificación de todos los vecinos que aportan mejora
            for i in range(self.cantidad):
                vecino, nuevo_valor = self.generar_vecino(solucion_actual, i)
                evaluacion_vecino, profit_vecino, weight_vecino = self.evaluar_vecino(
                    nuevo_valor, weight_actual, profit_actual, i
                )
                
                if evaluacion_vecino > evaluacion_actual:
                    buenos_vecinos.append([vecino, evaluacion_vecino, profit_vecino, weight_vecino])
            
            if len(buenos_vecinos) == 0:
                break
                
            # Selección estocástica entre los candidatos que mejoran el costo
            vecino_elegido = random.choice(buenos_vecinos)
            solucion_actual = vecino_elegido[0]
            evaluacion_actual = vecino_elegido[1]
            profit_actual = vecino_elegido[2]
            weight_actual = vecino_elegido[3]
            j += 1

        return solucion_actual, evaluacion_actual