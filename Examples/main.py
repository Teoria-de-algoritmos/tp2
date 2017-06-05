# Ejemplo
from timeit import default_timer as timer
from BellmanFord import BellmanFord
from Dijkstra import Dijkstra
from FloydWarshall import FloydWarshall
from GrafoUtils import generarGrafo


quant = input("Ingrese la cantidad de monedas: ")
u = input("Ingrese u: ")
v = input("Ingrese v: ")
G = generarGrafo(quant)

print("Vertices: "+str(G.vertices()))

start = timer()
D = Dijkstra(G)
end = timer()


print("Dijkstra: "+str((end - start)*1000)+" mseg")

start = timer()
B = BellmanFord(G)
end = timer()

print("BellmanFord: "+str((end - start)*1000)+" mseg")

start = timer()
F = FloydWarshall(G)
end = timer()

print("FloydWarshall: "+str((end - start)*1000)+" mseg")

print "Dijkstra distance: "+str(D.distancia(u,v))
print "BellmanFord distance: "+str(B.distancia(u,v))
print "FloydWarshall distance: "+str(F.distancia(u,v))
