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

def rec_sobornos(dict_con_nombre_productos, soborno, cantidad_a_dejar):
    print(dict_con_nombre_productos)
    print(f" \nsoborno: {soborno.unidades}; {soborno.nombre}\n")
    print(f"soborno devuelto : {cantidad_a_dejar}")
    cantidad = 0
    if soborno.nombre in cantidad_a_dejar:
        cantidad = sum(cantidad_a_dejar[soborno.nombre])
    if dict_con_nombre_productos[soborno.nombre][0] + cantidad < soborno.unidades: 
        if soborno.nombre not in cantidad_a_dejar:
            cantidad_a_dejar[soborno.nombre] = []    
        primer_unidad = dict_con_nombre_productos[soborno.nombre][0]   
        cantidad_a_dejar[soborno.nombre].append(primer_unidad)
        dict_con_nombre_productos[soborno.nombre].pop(0)
        return rec_sobornos(dict_con_nombre_productos, soborno,cantidad_a_dejar )# -> #producto = [9, 7, 5,4,3, 1]
    unidad_max = 0
    soborno_contrajado = 0
    if soborno.nombre in cantidad_a_dejar:
        soborno_contrajado = sum(cantidad_a_dejar[soborno.nombre])
    for unidades in dict_con_nombre_productos[soborno.nombre]:  #(cigarrillos) -> [9,7,5,4,3,1] 
        if soborno.unidades <= unidades + soborno_contrajado:     
            unidad_max = unidades ## unidades_max = 2
        if soborno.unidades > unidades + soborno_contrajado:
            break
    if soborno.nombre not in cantidad_a_dejar:
        cantidad_a_dejar[soborno.nombre] = []
    cantidad_a_dejar[soborno.nombre].append(unidad_max)
    return cantidad_a_dejar

def alg_greedy(productos,sobornos):     ##  paquetes cigarrillos de 3 y 9 y 15 unidades, soborno 6 -> paquete de 9 unidades
    dict_con_nombre_productos = {}
    productos.sort(key=lambda x: x.unidades, reverse=True)  # O(n logn)
    for producto in productos:   #O(n)
        if producto.nombre not in dict_con_nombre_productos: 
            dict_con_nombre_productos[producto.nombre] = []
        dict_con_nombre_productos[producto.nombre].append(producto.unidades)
    soborno_devuelto = {}
    for soborno in sobornos:
        rec_sobornos(dict_con_nombre_productos, soborno, soborno_devuelto) ## -> productos = {cigarrillos: [15, 9, 3], coca: [15, 7, 5, 3, 1]}
    return soborno_devuelto                                                ## soborno = paquete("cigarrillos", 6)
                                                                            ## soborno devuelto = {}


productos = []
for i in range(10):
    productos.append(paquete("coca", random.randint(1, 15)))
for i in range(15):
    productos.append(paquete("vodka", random.randint(1, 20)))
for i in range(5):
    productos.append(paquete("sprite", random.randint(1, 15)))

unidades = [11, 9, 7, 5,4, 2] ## soborno = 14 cigarrillos  -> deberia dar 7+5+2 -> 11+4

for unidad in unidades:
    productos.append(paquete("cigarrillos", unidad))

incautado = alg_greedy(productos, [paquete("cigarrillos", 8),paquete("coca",20)])
print(f"lo incautado es {incautado}")
