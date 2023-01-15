#Título Programa: PRACTICA 5: Algoritmo Evolutivo
#Fecha: 13-Enero-2023
#Autor: Renteria Arriaga Josue

import numpy as np
import matplotlib.pyplot as pit
from tkinter import * # Librería para crear el tablero gráfico.

np.random.seed(2)
k = 4

# Inicializamos nuestas matrices de aprendizaje.
Reinas = np.random.randint(0,8,(k,8))
Reinas_inicial = Reinas
cont_heuristica = 0

# Funcion que saca la heuristica de una lista o np.
def heuristica (reinas):
    h = 0
    # De forma Horizontal.
    for i in range(0,8):
        for j in range(i+1, 8):
            if (reinas[i] == reinas[j]):
                h += 1

    # De forma Diagonal.
    for i in range(0, 7):
        for j in range(i+1, 8):
            if(abs(i-j) == abs(reinas[i] - reinas[j])):
                h += 1
    
    return (28-h)

# Funcion que hace el cruce de las diferentes (listas o np).
# Recordar que solo agarra las 3 mejores listas o np (Con su mejor heuristica).
def cruza (Reinas, anterior, seleccionados, rechazados):
    # Cambio de las primeras 2.
    a,b,c = anterior[seleccionados[1], 0:3]
    x,y,z = anterior[seleccionados[0], 0:3]
    Reinas[seleccionados[0], 0:3] = a,b,c 
    Reinas[seleccionados[1], 0:3] = x,y,z

    # Cambio de las siguientes 2.
    a,b,c = anterior[seleccionados[2], 0:3]
    x,y,z = anterior[rechazados[0], 0:3]
    Reinas[rechazados[0], 0:3] = a,b,c 
    Reinas[seleccionados[2], 0:3] = x,y,z

    return Reinas

# Funcion que hace la mutacion en nuestra en laS 3 LISTAS O NP
def mutuacion (Reinas):
    # Hacemos la mutacion.
    Reinas[np.random.randint(0,4), np.random.randint(0,8)] = np.random.randint(0,8)
    Reinas[np.random.randint(0,4), np.random.randint(0,8)] = np.random.randint(0,8)
    Reinas[np.random.randint(0,4), np.random.randint(0,8)] = np.random.randint(0,8)

    return Reinas

# Funcion que busca la lista con la mejor Heuristica (28).
def buscar_heuristica(Reinas, k, problema_resuelto):
    cont_heuristica = 0
    for i in range(0, k):
        cont_heuristica = int(heuristica(Reinas[i]))

        # Condicion para dahr la mejor lista o opcion.
        if cont_heuristica == 28:
            problema_resuelto = Reinas[i]

            return cont_heuristica, problema_resuelto
    
    return cont_heuristica, problema_resuelto

# Funcion que convierte un renglon de un np a una lista.
def lista_del_renglon(Reinas, numero, problema_resuelto):
    problema_resuelto = Reinas[numero]

    return problema_resuelto

# Funcion que devuelve una lista con los elementos no repetidos en 2 listas.
def no_repetidos(lista1, lista2):
    lista_repetidos = list(set(lista1) - set(lista2))

    return lista_repetidos

# Funcion que cuenta las veces que se repite un numero en una lista.
def repetidos(lista, numero):
    repeticiones = 0
    
    # Ciclo que busca los numeros repetidos.
    for n in lista:
        if n == numero:
            repeticiones += 1

    return repeticiones

# Funcion que elimina los numeros repetidos de cada renglon de la Lista Reinas.
def numeros_repetidos(Reinas, k):
    # Inicializacion de los elementos necesarios.
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    lista_repetidos = []
    problema_resuelto = []
    repeticiones = 0

    # Ciclo para hacer los cambios.
    for i in range(0, k):
        # Llamamos a la funcion que nos convierte un renglon de un np en una lista.
        problema_resuelto = lista_del_renglon(Reinas, i, problema_resuelto)
        for j in range(len(problema_resuelto)):
            # Llamamos a la funciones de numeros repetidos y no repetidos.
            repeticiones = repetidos(problema_resuelto, problema_resuelto[j])
            lista_repetidos = no_repetidos(numeros, problema_resuelto)

            # Condicion para cambiar un elemento que se repite mas de 2 veces.
            if repeticiones > 1:
                problema_resuelto[j] = lista_repetidos[0]

        # Actualizamos el renglon que se modifico.
        Reinas[i] = problema_resuelto

    return Reinas

# Funcion de todo el proceso para hacer los cambios.
def Proceso(Reinas):
    lista = []
    arreglo = np.zeros(k)

    # Creamos un arreglo con las diferentes heuristicas.
    for i in range(0, k):
        arreglo[i] = heuristica(Reinas[i])

    # Ordenamos de mayor a menor la lista de las heuristicas. 
    ordenando = sorted(arreglo)

    # Inicializacion de listas de aceptar y rechazar.
    seleccionados = []
    rechazados = []

    # Mostramos los mayores Fi.
    for i in range(0, k):
        if(heuristica(Reinas[i]) ==  ordenando[k - 1]):
            print("Mayor fi:", i, Reinas[i], heuristica(Reinas[i]))
            seleccionados.append(i)

    # Mostramos los mayores Fi.
    for i in range(0, k):
        if(heuristica(Reinas[i]) >= ordenando[k - 3] and heuristica(Reinas[i]) < ordenando[k - 1]):
            print("Mayor fi:", i, Reinas[i], heuristica(Reinas[i]))
            seleccionados.append(i)

    # Metemos el valor o valores rechazados.
    for i in range(0, k):
        if (heuristica(Reinas[i]) == ordenando[0]):
            rechazados.append(i)

    # Hacemos el proceso de los valores rechazados. 
    anterior = Reinas
    a,b,c,d,e,f,g,h = Reinas[seleccionados[0]]
    print("\nRechazados: ", rechazados[0])
    Reinas[rechazados[0]] = a,b,c,d,e,f,g,h

    # Hacemos el proceso de la Cruza.
    print("\nCruza")
    Reinas = cruza(Reinas, anterior, seleccionados, rechazados)
    print(Reinas)

    # Hacemos el proceso de la Mutacion.
    print("\nMutacion")
    Reinas = mutuacion(Reinas)
    print(Reinas)

    # Mostramos los elementos si eliminamos valores repetidos.
    print("\nEliminar los numeros repetidos: ")
    Reinas = numeros_repetidos(Reinas, k)
    print(Reinas)

    # Poceso para imprimir las nuevas Heuristicas.
    print("\nNuevas Heuristicas: ")
    for i in range(0,k):
        print(i, heuristica(Reinas[i]))
    print("\n")
    return Reinas

#----- INICIO DE NUESTROS PROCESOS -----
problema_resuelto = []
i = 0

# Repeticiones de el proceso y encontrar la mejor Heuristica.
while (cont_heuristica != 28):
    i += 1
    # Encabezado y mostrado de la poblacion inicial de ese proceso.
    print("\n\n--------------------------------")
    print("Poblacion inicial\n", Reinas)
    print("\nNo de Proceso: ", i)

    # Llamamos la funcion proceso que muestra la mutacion, Cruce, etc..
    Reinas = Proceso(Reinas)
    
    # """

    # """

    # Observamos la heuristica.
    cont_heuristica, problema_resuelto = buscar_heuristica(Reinas, k, problema_resuelto)

# Mostramos el Mejor tablero con h = 28
print("\n\t°°°°°°°° El mejor Tablero °°°°°°°°\n")
print("La heuristica es: ", cont_heuristica)
print("La lista es: ", problema_resuelto)
print("No. de Procesos: ", i, "\n")


# Funciones
# -------------------------------------------------------------------------------------------------------------------
# Graficar el tablero (Creación de la Ventana para el Tablero Inicial). 
root = Tk()
root.title("Tablero Final (Heuristica de 28)")
Grid.rowconfigure(root, 0, weight=10)
Grid.columnconfigure(root, 0, weight=10)
root.geometry("500x500")

# Creamos y configuramos un Frame.
frame = Frame(root)
frame.grid(row = 0, column = 0, sticky = N+S+E+W)
indice = 0

#Creamos un 8x8 (filas y columnas).
for filas in range(8):
    Grid.rowconfigure(frame, filas, weight = 10)
    for columnas in range(8):
        Grid.columnconfigure(frame, columnas, weight = 10)

        # Coloreamos los Botones que tengan un 1 en el arreglo.
        if columnas == problema_resuelto[filas]:
            btn = Button(frame, bg = "blue") # Creación de los botones en el Frame (Los que tengan a la reina).
        else:
            btn = Button(frame) # Creación de los botones en el Frame (los que quedan). 
        btn.grid(row = filas, column = columnas, sticky = N+S+E+W)  

# Loop de la Ventana.
root.mainloop()