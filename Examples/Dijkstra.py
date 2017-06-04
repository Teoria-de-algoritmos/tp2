from bisect import insort

class Dijkstra:

	def __init__(self, grafo):
		self.grafo = grafo
		self.distancias = [[grafo.peso(i,j) for j in xrange(grafo.vertices())] for i in xrange(grafo.vertices())]

		for i in xrange(grafo.vertices()):
			self.distancias[i][i] = 0
			cola = sorted([(self.distancias[i][j], j) for j in xrange(grafo.vertices())])
			while cola:
				actual = cola.pop(0)[1]
				for siguiente in xrange(self.grafo.vertices()):
					nuevaDistancia = self.distancias[i][actual] + self.distancias[actual][siguiente]
					if nuevaDistancia < self.distancias[i][siguiente]:
						cola.remove((self.distancias[i][siguiente], siguiente))
						self.distancias[i][siguiente] = nuevaDistancia
						insort(cola, (nuevaDistancia, siguiente))
	
	def distancia(self, u, v):
		return self.distancias[u][v]
