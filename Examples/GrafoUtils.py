from collections import defaultdict    

def parse(clase, ruta_archivo):
    archivo = open(ruta_archivo)
    grafo = clase(int(archivo.readline())) 
    for _ in xrange(int(archivo.readline())):
        grafo.eje(*map(int, archivo.readline().split()))
    return grafo



class Digrafo(object):
    # Inicializador
	def __init__(self, vertices):
		self.V = vertices
		self.grafo = defaultdict(lambda:([],[])) #Diccionario default para almacenar el grafo como tuplas de dos listas
    # Funcion para agregar un elemento al grafo
	def eje(self, u, v):
	    self.grafo[u][0].append(v)
	    self.grafo[v][1].append(u)

	def vertices(self):
 		return self.V

	def vecinos(self, u):
	    for v in self.grafo[u][0]:
	        yield v
    
	def vecinos_entrantes(self, u):
	    for v in self.grafo[u][1]:
	        yield v
            
class Grafo(Digrafo):
    def eje(self, u, v):
    	Digrafo.eje(self, u, v)
    	Digrafo.eje(self, v, u)

class DigrafoConPeso(Digrafo):
	def __init__(self, vertices):
		super(DigrafoConPeso, self).__init__(vertices)
		self.pesos = defaultdict(lambda :float("inf"))

	def eje(self, u, v, peso):
		self.pesos[(u, v)] = peso
		super(DigrafoConPeso, self).eje(u,v)

	def peso(self, u, v):
		return pesos[(u,v)]

def generarGrafo(n):
	from random import seed, randint
	seed()
	tope = 10**3
	grafo = DigrafoConPeso(n)
	for i in xrange(n):
		for j in xrange(n):
			if i != j:
				grafo.eje(i, j, randint(1, tope))
	return grafo