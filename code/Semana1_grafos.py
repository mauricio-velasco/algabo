# Implementación de grafos como listas de adyacencia
from copy import deepcopy
from collections import deque
import math

class Grafo:
    def __init__(self, num_vertices, dirigido = True):
        #inicializa declarando un arreglo de vertices 
        self.vertices = range(num_vertices)
        # y el objeto adj_edges que tiene por keys los vertices y por values conjuntos
        # si el vertice i tiene valor {j,k,t} quiere decir que (i,j), (i,k) e (i,t) son aristas
        self.adj_edges = {vertex : set() for vertex in self.vertices}
        self.dirigido = dirigido

    def nueva_arista(self, i, j):
        self.adj_edges[i].add(j) #add(j)  en sets significa unir {j}
        if not self.dirigido:
            self.adj_edges[j].add(i) #add(j)  en sets significa unir {j}
            
    def mostrar_adj_list(self):
        for key in self.adj_edges:
            print(f"node {key} : {self.adj_edges[key]}")

    # Ahora vamos a ver como es BFS en un grafo. La clave es usar un queue, 
    # una estructura de datos que importamos arriba de collections

    # Hay varias cosas que podriamos preguntar, por ejemplo como producir una lista 
    # de los nodos a los que podemos llegar desde s y más precisamente la distancia mínima

    def distancias_desde(self, source_vertex):
        Q = deque([source_vertex])
        explorados = set()
        explorados.add(source_vertex)
        distancias = {vertex: math.inf for vertex in self.vertices} 
        distancias[source_vertex] = 0
        while Q:
            v = Q.pop()
            for w in self.adj_edges[v]:
                if w not in explorados:
                    distancias[w] = distancias[v]+1
                    explorados.add(w)
                    Q.appendleft(w)
        return distancias

if __name__=="main":
    G = Grafo(4, dirigido = False)
    G.nueva_arista(0,1)
    G.nueva_arista(1,2)
    G.nueva_arista(2,3)
    G.nueva_arista(3,0)
    H=deepcopy(G)

    G = Grafo(4, dirigido = True)
    G.nueva_arista(0,1)
    G.nueva_arista(1,2)
    G.nueva_arista(2,3)
    G.nueva_arista(3,0)
    G.mostrar_adj_list()
    H.mostrar_adj_list()
    
    distancias = H.distancias_desde(0)