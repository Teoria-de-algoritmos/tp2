from bisect import insort

class Dijkstra:

	def __init__(self, grafo):
		self.grafo = grafo
		self.distancias = [[grafo.peso(i,j) for j in xrange(grafo.vertices())] for i in xrange(grafo.vertices())]

		for i in xrange(grafo.vertices()):
			self.distancias[i][i] = 0
			for j in xrange(grafo.vertices()):
				cola.append((self.distancias[i][j], j))
			cola.sort()
			while cola:
				actual = cola.pop(0)
				for siguiente in xrange(self.grafo.vertices()):
					nuevaDistancia = self.distancias[i][actual] + self.distancias[actual][siguiente]
					if nuevaDistancia < self.distancias[i][siguiente]:
						cola.remove((distancia[i][siguiente], siguiente))
						self.distancias[i][siguiente] = nuevaDistancia
						insort(cola, (nuevaDistancia, siguiente))
	
	def distancia(self, u, v):
		return self.distancias[u][v]