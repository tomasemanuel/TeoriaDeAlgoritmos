## Comenzamos por las pruebas de complejidad de Backtracking

# Test 1
def probarConElementosIguales():
    plt.xlabel('Cantidad de pesos')
    plt.ylabel('Tiempo de Ejecucion (segundos)')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de pesos ')
    dataset =[]
    cant = []
    tiempo = []
    for i in range(19):
        print(f"va por el item {i}")
        cant.append(i)

        dataset.append(0.5)
        start_time = datetime.datetime.now()
        backtrackingBinPacking(dataset, 1)
        end = datetime.datetime.now()
        elapsedTime = end - start_time
        tiempo.append(elapsedTime.total_seconds())
    plt.plot(cant, tiempo, color='blue')

# Test 2
def probarConElementosCompletos():
    plt.xlabel('Cantidad de pesos')
    plt.ylabel('Tiempo de Ejecucion (segundos)')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de pesos ')
    dataset =[]
    cant = []
    tiempo = []
    for i in range(700):
        print(f"va por el item {i}")
        cant.append(i)
        dataset.append(0.9)
        start_time = datetime.datetime.now()
        backtrackingBinPacking(dataset, 1)
        end = datetime.datetime.now()
        elapsedTime = end - start_time
        tiempo.append(elapsedTime.total_seconds())
    plt.plot(cant, tiempo, color='blue')

# Test 3
def probarConElementosComplemento():
    plt.xlabel('Cantidad de pesos')
    plt.ylabel('Tiempo de Ejecucion (segundos)')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de pesos ')
    dataset =[]
    cant = []
    tiempo = []
    for i in range(120):
        print(f"va por el item {i}")
        cant.append(i)
        dataset.append(0.9)
        dataset.append(0.1)
        start_time = datetime.datetime.now()
        backtrackingBinPacking(dataset, 1)
        end = datetime.datetime.now()
        elapsedTime = end - start_time
        tiempo.append(elapsedTime.total_seconds())
    plt.plot(cant, tiempo, color='blue')

# Test 4
def pruebaConDatasetGenerado():
    plt.xlabel('Cantidad de pesos')
    plt.ylabel('Tiempo de Ejecucion (segundos)')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de pesos ')
    tiempos  = []
    for j in range(7):  
        weights = []
        cant = []
        tiempo = []
        for i in range(55):
            print(f"va por el item {i} repe {j}")
            cant.append(i)
            weights.append(round(random.uniform(0, 1), 2))
            start_time = datetime.datetime.now()
            backtrackingBinPacking(weights, 1)
            end = datetime.datetime.now()
            elapsedTime = end - start_time;
            tiempo.append(elapsedTime.total_seconds())
        tiempos.append(tiempo)
    plt.plot(cant, tiempos[0], color='blue')
    plt.plot(cant, tiempos[1], color='red')
    plt.plot(cant, tiempos[2], color='green')
    plt.plot(cant, tiempos[3], color='yellow') 
    plt.plot(cant, tiempos[4], color='orange')
    plt.plot(cant, tiempos[5], color='purple')
    plt.plot(cant, tiempos[6], color='pink')

    plt.show() 

## Generacion de Sets para los tests

# Primer Set de Datos
def primerSet(funcionAproximada):
    minimo = 10
    capacidad = 1
    weights = [random.random() for _ in range(minimo)]
    additional_numbers = 40
    plt.xlabel('Cantidad de pesos')
    plt.ylabel('Ratio entre la respuesta Optima con la Aproximada')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de pesos ')
    soluciones = []
    cant = []
    for i in range(additional_numbers):
        cant.append(i+minimo)
        print(f"VA POR EL NUMERO {i+5} ")
        weights.append(round(random.uniform(0, 0.5), 2))
        solOptima = backtrackingBinPacking(weights,capacidad)
        solAproximadaNextFit = funcionAproximada(weights,capacidad)
        soluciones.append(solAproximadaNextFit/solOptima)
    print(soluciones)
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    color_cycle = itertools.cycle(colors)
    limited_colors = list(itertools.islice(color_cycle, len(cant)))
    plt.bar(cant, soluciones,color=limited_colors )

# Segundo Set de Datos
def segundoSet(rango,funcionAproximada):
    capacidad = 1
    soluciones = []
    iteraciones = []
    plt.xlabel('Cantidad de iteraciones')
    plt.ylabel('Ratio entre la respuesta Optima con la Aproximada')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de Pesos ')
    for i in range(1,rango):
        print(f"va por el item {i}")
        iteraciones.append(i)
        weights = [round(random.uniform(0, 0.5), 2) for _ in range(i)]
        solOptima = backtrackingBinPacking(weights,capacidad)
        solAproximadaNextFit = funcionAproximada(weights,capacidad)
        soluciones.append(solAproximadaNextFit/solOptima)
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    color_cycle = itertools.cycle(colors)
    limited_colors = list(itertools.islice(color_cycle, len(iteraciones)))
    plt.bar(iteraciones, soluciones,color=limited_colors )

# Tercer Set de Datos
def tercerSet(rango,longitud,funcionAproximada):
    capacidad = 1
    soluciones = []
    iteraciones = []
    plt.xlabel('Cantidad de iteraciones')
    plt.ylabel('Ratio entre la respuesta Optima con la Aproximada')
    plt.title('Ratio Optima y Aproximada vs la Cantidad de Pesos ')
    for i in range(1,rango):
        print(f"va por el item {i}")
        iteraciones.append(i)
        weights = [round(random.uniform(0, 0.5), 2) for _ in range(longitud)]
        solOptima = backtrackingBinPacking(weights,capacidad)
        solAproximadaNextFit = funcionAproximada(weights,capacidad)
        soluciones.append(solAproximadaNextFit/solOptima)
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    color_cycle = itertools.cycle(colors)
    limited_colors = list(itertools.islice(color_cycle, len(iteraciones)))
    plt.bar(iteraciones, soluciones,color=limited_colors )