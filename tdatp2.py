import sys
import time

def backtrackingBinPacking(weights, capacity):
    return backtrackingBinPackingAux(weights, capacity, [[weights[0]]], 1, None)
        
def backtrackingBinPackingAux(weights, capacity, bins, currentIndex, solucionMinima):
    if (solucionMinima and solucionMinima <= len(bins)): 
        return solucionMinima
    if (currentIndex == len(weights)):
        return len(bins)
    binsForOption1 = []
    for i in range(len(bins)): 
        if (weights[currentIndex] + sumBin(bins[i]) <= capacity): 
            binsIOption1= bins[i] + [weights[currentIndex]]
            binsOption1 = bins[:i] + [binsIOption1] + bins[i+1:]
            option1 = backtrackingBinPackingAux(weights, capacity, binsOption1, currentIndex + 1, solucionMinima) #llamado recursivo
            if (solucionMinima is None or option1< solucionMinima): 
                solucionMinima = option1
            binsForOption1.append(option1)
    binsOption2 = bins + [[weights[currentIndex]]]
    option2 = backtrackingBinPackingAux(weights, capacity, binsOption2 , currentIndex + 1,solucionMinima)
    if (solucionMinima is None or option2< solucionMinima):
        solucionMinima = option2
    if (len(binsForOption1) == 0):
        return option2
    option1 = min(binsForOption1)
    return min(min(option1, option2),solucionMinima)

def sumBin(bin):
    sum = 0
    for i in range(len(bin)):
        sum += bin[i]
    return sum

def next_fit(capacity, weights):
    bins = []
    bin_actual = []
    for item in weights:
        if sum(bin_actual) + item <= capacity:
            bin_actual.append(item)
        else:
            bins.append(bin_actual)
            bin_actual = [item]
    bins.append(bin_actual)
    return len(bins)

def first_fit(capacity, weights):
    bins = []
    for item in weights:
        for i in range(len(bins)): 
            if bins[i] + item <= capacity:
                bins[i] += item 
                break
        else:
            bins.append(item)
    return len(bins) 

def leer_archivo(archivo):
    with open(archivo, "r") as file:
        lineas = file.readlines()
        set = []
        for i in range(2, len(lineas)):
            set.append(float(lineas[i].strip()))
        return set

def main(): 
    argumentos = sys.argv

    if len(argumentos) != 3:
        print("La cantidad de argumentos es incorrecta")
        return
    
    set = leer_archivo(argumentos[2])
    inicio = time.time()

    if argumentos[1] == "E":
        bins = backtrackingBinPacking(set, 1)
        print("Solución Exacta: # ", bins)

    elif argumentos[1] == "A":
        bins = next_fit(1, set)
        print("Solución Aproximada: # ", bins)

    elif argumentos[1] == "A2":
        bins = first_fit(1, set)
        print("Solución Aproximada Alumnos: # ", bins)

    fin = time.time()

    tiempo_ejecucion = (fin - inicio) * 1000
    print("Tiempo de ejecución:", tiempo_ejecucion, "mseg")

main()