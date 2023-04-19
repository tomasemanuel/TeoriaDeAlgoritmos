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

a = [[1,3,5],[4,5,6],[5,8,9],[8,9,10],[1,3,5],[4,5,6],[5,8,9],[8,9,10]]

print(k_merge_heap(a))