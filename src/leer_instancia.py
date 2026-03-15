class Leer_Instancia:
    def leer_instancia():
        profits = []
        weights = []
        ARCHIVO_INSTANCIA = "data/instancia_mochila.txt"
        with open(ARCHIVO_INSTANCIA, 'r') as file:
            cantidad = int(next(file).strip())
            for i in range(cantidad):
                _, profit, weight = map(float, next(file).split())
                profits.append(profit)
                weights.append(weight)
            capacidad = int(next(file).strip())
        return cantidad, profits, weights, capacidad
