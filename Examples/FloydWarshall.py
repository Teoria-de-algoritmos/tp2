from GrafoUtils import Digrafo


class FloydWarshall:

    def __init__(self, grafo):
        self.grafo = grafo
        self.dist = [[grafo.peso(i,j) for j in xrange(grafo.vertices())] for i in xrange(grafo.vertices())]
        for k in xrange(grafo.vertices()):
             for i in xrange(grafo.vertices()):
                for j in xrange(grafo.vertices()):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k]+ self.dist[k][j])

    def distancia(self, u, v):
        return self.dist[u][v]