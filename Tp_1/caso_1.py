# El problema de K-merge es el siguiente: se tienen K arreglos ordenados, y se quiere quiere obtener un único arreglo, también
# ordenado, con todos los elementos de los arreglos originales (inclusive si hay repetidos). Por simplicidad para los diferentes
# análisis se puede suponer que todos los arreglos tienen exactamente h elementos (por ende, la cantidad total de elementos es
# n = K ∗ h).
# Para resolver este problema, es posible que hayan visto en Algoritmos y Programación II un algoritmo que resuelve este
# problema utilizando un Heap. Nos referiremos a este como el algoritmo que utiliza Heaps.
# La idea en este caso será plantear otra solución y analizarla. Se propone el siguiente algoritmo por división y conquista, con
# semejanzas a mergesort.
# 1. Caso base: cuando quede un único arreglo, simplemente devolver dicho arreglo.
# 2. En el caso general, dividir la cantidad de arreglos entre la primera mitad, y la segunda mitad, y luego invocar
# recursivamente para cada mitad de arreglos. Es decir, si tenemos cuatro arreglos, invocamos para los primeros 2, y
# luego para los segundos 2. Al terminar los llamados recursivos, tenemos dos arreglos ordenados. Estos deberán ser
# intercalados ordenadamente, tal cual se realiza en mergesort.
import random
import datetime
# from k_merge_heap import *
import heapq
import matplotlib.pyplot as plt
import numpy as np
import math

def k_merge(lista_arreglos):
    if len(lista_arreglos) == 1:
        return lista_arreglos[0]

    medio = len(lista_arreglos) // 2  #-> B =2
    izq = lista_arreglos[:medio]  # O(medio) -> a lo sumo es O((K*h)/2) -> O(K*h)
    der = lista_arreglos[medio:]  # O(fin - medio+1) ->  a lo sumo es O((K*h)/2) -> O(K*h)

    ## dos llamados recursivos -> A = 2
    izq = k_merge(izq) 
    der = k_merge(der)
    return merge(izq,der) # O(K*h)) -> n^C


def merge(left, right):
    res = []
    while left and right: 
        if left[0] <= right[0]:
            res.append(left.pop(0)) 
        else:                     
            res.append(right.pop(0))
    res = res + left + right
                           
    return res

def k_merge_catedra(lista_elementos):
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
def generarArregloConHElementos(h):
    arr = []
    for i in range(h):
        arr.append(random.randint(1, 300))
    arr.sort()
    return arr

def generarKArreglosConHElementosDiferentes(K,h0):
    arrays = []
    r = 1.05
    h = h0
    for i in range(K):
        h = math.ceil(h * r)
        arr = np.random.randint(1, 101, size=h)
        arrays.append(arr)
    return arrays

class Pruebas:
    def probarKArreglosConHElementos(self, k, func,h = 100):

        array = [generarArregloConHElementos(h) for i in range(k)]
        start_time = datetime.datetime.now()
        func(array)
        end = datetime.datetime.now()
        elapsedTime = end - start_time;
        return elapsedTime.total_seconds()

    def probarKArreglosConDistintosHElementos(self,k,func,h_inicial = 50):
        array = generarKArreglosConHElementosDiferentes(k,h_inicial)
        start_time = datetime.datetime.now()
        func(array)
        end = datetime.datetime.now()
        elapsedTime = end - start_time;
        return elapsedTime.total_seconds()

def probarFunc(func,func_generacion_arreglos,ks = [100]):
  times = [] 
  for arreglos in ks:
      time = func_generacion_arreglos(arreglos, func)
      times.append(time)

  return ks, times


plt.xlabel('Cantidad de  por arreglo')
plt.ylabel('Tiempo de ejecucion (segundos)')
plt.title('Tiempo de ejecucion vs Cantidad de elementos por arreglo')
pruebas = Pruebas()
#ks1, times1 = probarFunc(k_merge,pruebas.probarKArreglosConDistintosHElementos)

ks2, times2 = probarFunc(k_merge_catedra,pruebas.probarKArreglosConDistintosHElementos)

# plt.plot(ks1, times1, color='blue', label='k_merge')
plt.plot(ks2, times2, color='red', label='k_merge_catedra')

plt.legend()
plt.show() 