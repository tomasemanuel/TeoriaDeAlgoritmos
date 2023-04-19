# Consigna
## 1. 
### Determinar, utilizando el Teorema Maestro, cuál sería la complejidad del algoritmo propuesto.
## 2. 
### Describir el algoritmo que utiliza heaps, y determinar su complejidad.
## 3. 
### Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas para cada uno se condicen con la realidad.
## 4. 
### En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla).
### En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).
## 5. 
### Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.
#

## Resolucion
### 1

Por teorema maestro:
    
    Siendo K = Cantidad de arreglos ordenados
    Siendo H = Cant elementos de cada arreglo
    siendo n = k*h, la cantidad de elementos totales    
    T(n) = aT(n/b) + f(n)
    Donde: a = 2, b = 2, f(n) = O(n), C = 1

Para determinar la complejidad:

    n^logb(a) -> n^log2(2) -> n^1

Por lo tanto:

    n == f(n) == n

Como f(n) y n^logb(a) son asintoticamente iguales:

    T(n) = O(n^logb a ∗ log n) = O(n^1 ∗ log n) = O(n * log n)

La complejidad computacional del algoritmo propuesto por division y conquista es:

    T(n) = O(f(n)) = O(n * log n)

### 2 
El algoritmo propuesto utiliza un heap para encolar y desencolar los elementos que se encuentran en todos los arreglos. En primer lugar, encolamos el primer elemento de cada arreglo. Una vez que encolamos el primer elemento (como todos los arreglos estan ordenados, es el mas pequeño), iniciamos una iteracion hasta que el heap que utilizamos se encuentre vacio. El procedimiento es simple, desencolamos una vez el numero del heap, y vemos cual es el siguiente en el arreglo que provino ese numero, y lo encolamos al heap. Esto es analogo (desencolar del heap y ver cual es el siguiente del numero que provino ese numero) hasta que no tenemos mas numeros en un arreglo, por lo que no encolamos mas nada de este arreglo y seguimos desencolando del heap. Una vez que la posicion de todos los arreglos se encuentre en el final, desencolamos elementos restantes del heap y los añadimos al arreglo resultado. Dicho arreglo resultado se encontrara completamente ordenado.

Complejidad:
Al encolar los primeros elementos de todos los arreglos, como el encolamiento en un heap es log(k), siendo k los arreglos totales. Luego, el desencolar y encolar solamente es log k, ya que como mucho tenemos k elementos en el heap, pero como lo tenemos que hacer hasta que cada uno de los arreglos se encuentre vacio, osea un total de k*h, porque cada arreglo tiene h elementos, quedaria en total O(k*h*log(k)), ya que despreciamos el O(log(k)) del encolamiento del principio. 

import heapq

    def k_merge_heap(lista_elementos):
        heap = []
        res = []
        for i in range(len(lista_elementos)):
            heapq.heappush(heap,(lista_elementos[i][0],i,0))

        while heap: 
            minimo,indice_arreglo,indice_numero = heapq.heappop(heap) 
            res.append(minimo)
            if (indice_numero < len(lista_elementos[indice_arreglo])-1):
                nueva_posicion = indice_numero + 1
                heapq.heappush(heap,(lista_elementos[indice_arreglo][nueva_posicion],indice_arreglo,nueva_posicion))
        return res


        

        
    