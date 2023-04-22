# Queremos pasar mercadería de contrabando de Genovia a Krakozhia. La mercadería viene en paquetes que no podemos abrir.
# Cada paquete i trae Xi unidades de un determinado tipo de producto j. Podríamos llegar a tener varios paquetes del mismo
# tipo de producto j, incluso con diferente cantidad de unidades. También podemos tener diferentes paquetes de diferentes
# productos. Es decir, cada paquete (in-abrible) es de una cantidad específica de un tipo específico, y en total para un tipo
# específico j tenemos la suma de Xi unidades, para todos los i que sean de ese tipo.
# Para nuestro ejemplo, supongamos que tenemos un paquete que trae 8 cajetillas de cigarrillos sabor arándano. Otro paquete
# trae 5 cajetillas de lo mismos cigarrillos. Otro paquete puede traer 5 botellitas de 100ml de vodka radioactivo, etc. . .
# 1Ejemplo: https://www.reddit.com/r/LadyGaga/comments/ku1ed5/oreos_in_germany/

# 1

# Al pasar por la aduana, el corrupto funcionario puede indicarnos que “por acá no pasan sin dejarme al menos 6 cajetillas de
# cigarrillos de arándano”.
# Ante la imposibilidad de abrir y/o separar los paquetes, es claro que en dicho caso nos conviene dejar el paquete de 8 (no
# podemos abrirlo para sacar 6 de allí. . . sino la movida sería muy evidente). Si el oficial hubiera dicho que hay que dejar
# al menos 10 cajetillas, habría sido necesario dejar ambos paquetes para un total de 13 unidades de dicho producto. Si este
# hubiera dicho que le dejemos una cajetilla de cigarrillos y una botellita de vodka, tendríamos que dejar el paquete de 5
# botellitas de vodka y el paquete de 5 cajetillas de cigarrillos.

import random


class paquete:     
    def __init__(self, nombre, unidades):         
        self.nombre = nombre        
        self.unidades = unidades

def mayor_es_menor_que_soborno(dict_con_nombre_productos,soborno,incautado,incautado_total):
    if soborno.nombre not in incautado:
            incautado[soborno.nombre] = []    
    primer_unidad = dict_con_nombre_productos[soborno.nombre][0]   
    incautado[soborno.nombre].append(primer_unidad)
    incautado_total += primer_unidad
    dict_con_nombre_productos[soborno.nombre].pop(0)
    return rec_sobornos(dict_con_nombre_productos, soborno,incautado,incautado_total) # 


def rec_sobornos(dict_con_nombre_productos, soborno, incautado,incautado_total = 0):
    print(dict_con_nombre_productos)
    print(f" \nsoborno: {soborno.unidades}; {soborno.nombre}\n")
    print(f"soborno devuelto : {incautado}")
    if dict_con_nombre_productos[soborno.nombre][0] + incautado_total < soborno.unidades:    ##Caso el mayor de la lista es menor al soborno
        return mayor_es_menor_que_soborno(dict_con_nombre_productos,soborno,incautado,incautado_total) 
    # unidad_max = 0
    # for unidades in dict_con_nombre_productos[soborno.nombre]:  #O(n) Igualmente se puede mejorar haciendo una busqueda binaria, mejorando a un O(log n)!!
    #     if soborno.unidades <= unidades + incautado_total:     
    #         unidad_max = unidades
    #     if soborno.unidades > unidades + incautado_total:
    #         break 
    units = dict_con_nombre_productos[soborno.nombre]   #Busqueda binaria (O(log n) siendo n la cantidad de unidades de cada producto
    inicio = 0
    fin = len(units) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if soborno.unidades <= units[medio] + incautado_total:
            fin = medio - 1
        else:
            inicio = medio + 1
    unidad_max = units[fin]
    if soborno.nombre not in incautado:
        incautado[soborno.nombre] = []
    incautado[soborno.nombre].append(unidad_max) ## O(1)
    incautado_total += unidad_max
    return incautado

def alg_greedy(productos,sobornos): 
    dict_con_nombre_productos = {}
    for producto in productos: # O(n * k) n = cantidad de productos    Siempre la cantidad de sobornos es menor que la cantidad de productos
        for soborno in sobornos:  # O(k) k = cantidad de sobornos
            if producto.nombre == soborno.nombre:
                if producto.nombre not in dict_con_nombre_productos: 
                    dict_con_nombre_productos[producto.nombre] = []
                dict_con_nombre_productos[producto.nombre].append(producto.unidades)  #O(1)
                break
    for nombre in dict_con_nombre_productos:
        dict_con_nombre_productos[nombre].sort(reverse=True) ## O(k log n) siendo k la cantidad de sobornos y n la cantidad de cada tipo
    incautado = {}
    for soborno in sobornos: # (O(k) k = cantidad de sobornos)
        rec_sobornos(dict_con_nombre_productos, soborno, incautado) #O(n)
    return incautado                                                # O(n * k) + O(k log n) + O(k*n) = O(n * k) + O(k log n)
productos = []
for i in range(10):
    productos.append(paquete("coca", random.randint(1, 15)))

unidades = [11, 9, 7, 5,4, 2] # soborno = 14 cigarrillos  -> deberia dar 7+5+2 -> 11+4

for unidad in unidades:
    productos.append(paquete("cigarrillos", unidad))

incautado = alg_greedy(productos, [paquete("cigarrillos", 26), paquete("coca", 18)])
print(f"lo incautado es {incautado}")
