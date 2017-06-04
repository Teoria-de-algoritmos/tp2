

class BellmanFord: 

    def __init__(self,grafo):
        self.grafo = grafo
        self.distancias = []
	    for src in xrange(self.grafo.vertices()):	 
	        dist = [float("Inf")] * self.grafo.vertices()
	        dist[src] = 0
	        for _ in xrange(self.grafo.vertices() - 1):
	            for u in xrange(self.grafo.vertices()):
	            	for v in xrange(self.grafo.vertices()):
				w = grafo.peso(u,v)
		                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
		                        dist[v] = dist[u] + w
	        for u in xrange(self.grafo.vertices()):
		        for v in xrange(self.grafo.vertices()):
		        	w = self.grafo.peso(u,v)
	               		if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					print "El grafo contiene un ciclo de peso negativo"
					return
	        self.distancias.append(dist) 

	 def distancia(self, u, v):
	 	return self.distancias[u][v]
