"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Practico grupal
Fecha: 08/11
Autores: Santino Bautista Carbonari, Leando Ochoa, Kiara Notaro, Jesus Caldera, Lucas Garcia Cespedes.

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORT
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def separadorAsterisco():
    """
    Imprime una línea de 50 asteriscos para separar visualmente las distintas secciones del programa.
    Parámetros:
        Ninguno.

    Retorno:
        Ninguno.
    """

    for i in range(60):
        print("*",end="")
    print()

def mostrar_valores(lista, titulo):
    """
    Muestra los números que se encuentren en la lista en una tabla de 10 columnas.

    Parámetros:
        - lista: lista de los números que se quieren mostrar.
        - titulo: texto que se muestra como título (en la tabla).

    Retorno:
        - No retorna valores.
    """
    
    separadorAsterisco()
    print(titulo)
    separadorAsterisco()


    print("A\tB\tC\tD\tE\tF\tG\tH\tI\tJ")

    print("=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======")

    print()


    cantidadenfila = 0

    for numero in lista:
        print(numero, end="\t")
        cantidadenfila = cantidadenfila + 1

        if cantidadenfila == 10:
            print()
            cantidadenfila = 0

    print()
    separadorAsterisco()

    
def eliminar_repetidos(lista):
    """
    Crea una nueva lista sin valores repetidos, conservando el orden de aparición de la lista "original".

    Parámetros:
        - lista_original: lista de números (que se van a revisar).

    Retorno:
        - Una lista nueva, contiene los valores sin repetir.
    """

    
    lista_2 = lista[:]       #lista_2 es una copia de la original
    lista_sin_repetidos = []
    num_eliminados = 0

    
    for numero in lista_2:
        repetido = False              #asumo que el num no esta repetido

        
        for num_guardado in lista_sin_repetidos:

            if numero == num_guardado:  
                repetido = True         #esta repetido => no lo agrega

        if repetido == False:
            lista_sin_repetidos.append(numero)

        else:
            num_eliminados = num_eliminados + 1

    print("Cantidad de valores eliminados:", num_eliminados)


    return lista_sin_repetidos


def punto_3(lista):
    """
    Realiza el punto 3: elimina los repetidos y muestra la lista resultante.

    Parámetros:
        - lista_original: lista de números generados en pto. 1.

    Retorno:
        - No retorna ningún valor.
    """
    if len(lista) == 0:
        print("Primero debe generar los valores.")
        return

    lista_sin_repetidos = eliminar_repetidos(lista)  

    mostrar_valores(lista_sin_repetidos, "VALORES DEL JUEGO DE DATOS (DATOS SIN REPETIDOS)")

def generarNumeros(lista):

    """
    Genera números aleatorios y los almacena en una lista.
    Si la lista ya contiene elementos, pregunta si se desea reemplazarla.
    
    Parametros:
    
        lista (list): Lista donde se almacenarán los números.

    Retorno:
        list: Lista con los números generados.
    
    
    """
    
    if len(lista) > 0:
        entradaCorrecta = False
        while not entradaCorrecta:
            respuesta = input("Lista detectada ¿desea remplazarla? (si = 1) (no = 0) ")
            if respuesta == "1": 
                lista.clear()
                entradaCorrecta = True
            elif respuesta == "0":
                return lista
            else:
                print("Introduciste un valor erroneo.")
    
    entradaCorrecta = False
    while not entradaCorrecta:
        cantidad = input("¿Cuántos números querés generar? ")
        if cantidad.isdigit(): 
            cantidad = int(cantidad)
            if cantidad >= 2:
                entradaCorrecta = True
            else:
                print("La cantidad debe ser mayor o igual a 2")    
        else:
            print("Solo puedes introducir digitos.")


    for i in range(0, cantidad):
        numero = random.randint(0, 99999)
        lista.append(numero)
    print (lista)

    return lista
        
def valoresTopN(lista):
    """
    Identifica y muestra los N valores mayores únicos de una lista.

    Parámetros:
        numeros: Lista de números enteros.

    Retorno:
        Ninguno.
    """

    if len(lista) == 0:
        print("Primero debe generar los valores.")
        return
    entradaValida = False

    while entradaValida == False:
        entrada = input("Ingrese la cantidad N de valores a mostrar: ")

        if entrada.isdigit():
            n = int(entrada)

            if n > 0:
                entradaValida = True
            else:
                print("N debe ser mayor que cero.")
        else:
            print("Debe ingresar un número entero positivo.")

    ranking = []

    while len(ranking) < n:
        mayor = None
        for numero in lista:
            if numero not in ranking:
                if mayor is None or numero > mayor:
                    mayor = numero
        if mayor is None:
            break

        ranking.append(mayor)

    separadorAsterisco()
    print("VALORES DEL JUEGO DE DATOS (DATOS TOP N)")
    separadorAsterisco()

    for i in range(len(ranking)):
        print(i + 1, ". ", ranking[i], sep="")

    separadorAsterisco()

    if len(ranking) < n:
        print("Se solicitaron", n, "valores, pero solo existen",
              len(ranking), "valores únicos disponibles.")

"""
                            PUNTOS 4 Y 5
"""

def validacionLetra(letrasValidas, caracter):
    """
    Comprueba si el carácter ingresado se encuentra dentro
    de una lista de caracteres permitidos.

    Parámetros:
        letrasValidas (list): Lista de caracteres aceptados.
        caracter (str): Carácter ingresado que será evaluado.

    Retorno:
        bool: True si el carácter es válido, False en caso contrario.
    """
    bucle = True
    validacion = False
    while bucle:
        if caracter not in letrasValidas:
            print("Caracter ingresado invalido.")
            bucle = False
            validacion = False
        else:
            bucle = False
            validacion = True
    return validacion

def pedir_numero(mensaje, minimo, maximo):
    """
    Solicita un numero entero por teclado y lo valida (tipo y rango)

    Parametros:
        mensaje (str): texto a mostrar al pedir el dato
        minimo (int): valor mínimo aceptado (inclusive)
        maximo (int): valor máximo aceptado (inclusive)

    Retorna:
        int: el número ingresado, ya validado
    """
    while True:
        texto = input(mensaje)
        if texto.isdigit():
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                return numero
            else:
                print("Error: el valor debe estar entre ", minimo, " y ", maximo)

    # ------- FILTRADO ---------

def filtrar(lista):
    
    """
        Filtra una lista de numeros segun el criterio seleccionado. Mayor, menor, en rango, pares o impares.
    
        Parametro:
            lista (list): lista de numeros
    
        Retorna:
            None
        """

    if len(lista) == 0:
        print("Primero debe generar los valores.")
        return
    
    letrasValidas = ["M", "m", "E", "e", "R", "r", "P", "p", "I", "i"]
    listaFiltrada = []
    
    valorErroneo = True
    while valorErroneo:
        criterio = input("Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]:")
        validacion = validacionLetra(letrasValidas, criterio)
        if validacion:
            valorErroneo = False

    if validacion:
        
        if (criterio == "M" or criterio == "m"):
            listaFiltrada = criterioMayor(lista)
            
        elif (criterio == "E" or criterio == "e"):
            listaFiltrada = criterioMenor(lista)
        
        elif criterio == "R" or criterio == "r":
            listaFiltrada = criterioRango(lista)
        
        elif criterio == "P" or criterio == "p":
            listaFiltrada = numerosPar(lista)
            
        else:
            listaFiltrada = numerosImpar(lista)
            
    mostrar_valores(listaFiltrada, "VALORES DEL JUEGO DE DATOS (DATOS FILTRADOS)")
            
def criterioMayor(lista):
    
    """
        Filtra una lista de numeros, solo guarda los numeros mayores al indicado.
        
        Parametro:
            lista (list): lista de numeros
        
        Retorna:
            listaFiltrada (list): lista de numeros filtrada
    """

    listaFiltrada = []
    
    umbral = pedir_numero("Ingrese el umbral: ", 0, 99999)
    
    for i in lista:
        if i > umbral:
            listaFiltrada.append(i)
                
    return listaFiltrada

def criterioMenor(lista):
    
    """
        Filtra una lista de numeros, solo guarda los numeros menores al indicado.
            
        Parametro:
            lista (list): lista de numeros
            
        Retorna:
            listaFiltrada (list): lista de numeros filtrada
        """
    
    listaFiltrada = []
    
    umbral = pedir_numero("Ingrese el umbral: ", 0, 99999)
    
    for i in lista:
        if i < umbral:
            listaFiltrada.append(i)
            
    return listaFiltrada

def criterioRango(lista):
    
    """
        Filtra una lista de numeros, solo guarda los numeros dentro del rango indicado.
            
        Parametro:
            lista (list): lista de numeros
            
        Retorna:
            listaFiltrada (list): lista de numeros filtrada
        """
    
    listaFiltrada = []
    
    minimo = pedir_numero("Ingrese el mínimo: ", 0, 99999)
    maximo = pedir_numero("Ingrese el maximo: ", minimo, 99999)
    
    for i in lista:
        if i <= maximo and i >= minimo:
            listaFiltrada.append(i)
            
    return listaFiltrada

def numerosPar(lista):
    """
    Filtra los números pares de una lista y los almacena
    en una nueva lista sin modificar la original.

    Parámetros:
        lista (list): Lista de números enteros que serán filtrados.

    Retorno:
        list: Nueva lista que contiene únicamente los números pares.
    """
    
    listaFiltrada = []
    
    for i in lista:
        if i % 2 == 0:
            listaFiltrada.append(i)

    return listaFiltrada

def numerosImpar(lista):
    
    """
    Filtra los números impares de una lista y los almacena
    en una nueva lista sin modificar la original.

    Parámetros:
        lista (list): Lista de números enteros que serán filtrados.

    Retorno:
        list: Nueva lista que contiene únicamente los números impares.
    """
    
    listaFiltrada = []
    
    for i in lista:
        if i % 2 != 0:
            listaFiltrada.append(i)
                
    return listaFiltrada


def criterioCantCifras(lista):
    """
    Clasifica los números de una lista según su cantidad de cifras,
    generando cinco listas independientes con valores de 1 a 5 cifras.
    Posteriormente muestra cada lista en pantalla.

    Parámetros:
        lista (list): Lista de números enteros que serán clasificados.

    Retorno:
        None.
    """

    listaUnaCifra = []
    listaDosCifras = []
    listaTresCifras = []
    listaCuatroCifras = []
    listaCincoCifras = []

    for i in lista:
        if 0 <= i <= 9:
            listaUnaCifra.append(i)
        elif 10 <= i <= 99:
            listaDosCifras.append(i)
        elif 100 <= i <= 999:
            listaTresCifras.append(i)
        elif 1000 <= i <= 9999:
            listaCuatroCifras.append(i)
        else:
            listaCincoCifras.append(i)

    print("Valores de 1 cifra:")
    mostrar_valores(listaUnaCifra, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 2 cifras:")
    mostrar_valores(listaDosCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 3 cifras:")
    mostrar_valores(listaTresCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 4 cifras:")
    mostrar_valores(listaCuatroCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 5 cifras:")
    mostrar_valores(listaCincoCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    
    

def criterioPorValor(lista):
    """
    Función que desdobla una lista en dos, una lista hasta el umbral indicado inclusive y otra lista para los valores superiores

    Parametros:
        lista (list): lista de numeros que van a ser desdoblados
    
    Retorno:
        None
    """
    umbral = pedir_numero("Ingrese el valor umbral: ", 0, 99999)
    hasta_umbral = []
    sobre_umbral = []
    for valor in lista:
        if valor <= umbral:
            hasta_umbral.append(valor)
        else:
            sobre_umbral.append(valor)
    print("Valores hasta el umbral (inclusive):")
    mostrar_valores(hasta_umbral, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores por encima del umbral:")
    mostrar_valores(sobre_umbral, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")


def desdoblamiento(lista):
    """
    Desdoblamiento de valores de una lista

    Paramtros:
        lista (list): lista de valores que serán desdoblados

    Retorno:
        None
    """

    if len(lista) == 0:
        print("Primero debe generar los valores.")
        return
    
    letrasValidas = ["P", "p", "C", "c", "U", "u"] 

    valorErroneo = False
    while not valorErroneo:
        criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")        
        validacion = validacionLetra(letrasValidas, criterio)
        if validacion:
            valorErroneo = True
    
    if validacion:
            if (criterio == "P" or criterio == "p"):
                listaPares = numerosPar(lista)
                listaImpares = numerosImpar(lista)
                mostrar_valores(listaPares, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
                mostrar_valores(listaImpares, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
            
            elif criterio == "C" or criterio == "c":
                criterioCantCifras(lista)

            else:
                criterioPorValor(lista)

def valoresMaximosMinimos(lista):
    """
    Identifica los valores máximo y mínimo de una lista de números enteros. 
    Destacando los máximos entre corchetes [], los mínimos entre paréntesis ()
    y los valores que sean máximo y mínimo al mismo tiempo entre <>.

    Parámetros:
        lista (list): Lista de números enteros que serán analizados.

    Retorno:
        None.
    """
    
    if len(lista) == 0:
        print("Primero debe generar los valores.")
        return

    listaNueva = lista
    maximo = lista[0]
    minimo = lista[0]

    for numero in listaNueva:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    separadorAsterisco()
    print("VALORES DEL JUEGO DE DATOS (DATOS MÁXIMOS Y MÍNIMOS [máx] (mín) <máx/mín>)")
    separadorAsterisco()
    print("A\tB\tC\tD\tE\tF\tG\tH\tI\tJ")
    print("=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======\t=======")
    print()

    cantidadenfila = 0
    for numero in lista:
        if numero == maximo and numero == minimo:
            print("<", numero, ">", sep="", end="\t")
        elif numero == maximo:
            print("[", numero, "]", sep="", end="\t")
        elif numero == minimo:
            print("(", numero, ")", sep="", end="\t")
        else:
            print(numero, end="\t")
        cantidadenfila = cantidadenfila + 1
        if cantidadenfila == 10:
            print()
            cantidadenfila = 0
    print()
    separadorAsterisco()
        



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal del programa.
    Inicializa la lista de números y ejecuta el menú principal,
    permitiendo al usuario seleccionar las distintas operaciones
    disponibles hasta que decida salir.

    Parámetros:
        Ninguno.

    Retorno:
        None.
    """
    
    numeros = []
    lista = []
    
    
    while True:
        while True:
            opciones = 7	
            print()
            print("---------------------------")
            print("MENÚ DEL PROGRAMA           ")
            print("---------------------------")
            print("[1] ... Generar valores ...")
            print("[2] ... Mostrar valores ...")
            print("[3] ... Eliminar valores repetidos ...")
            print("[4] ... Filtrar valores ...")
            print("[5] ... Desdoblar valores  ")
            print("[6] ... Valores top N  ")
            print("[7] ... Valores maximos y minimos  ")            
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            generarNumeros(lista)
        elif opcion == "2":   # Opción 2
            if len(lista) == 0:
                print("Primero debe generar los valores.")
            else:
                mostrar_valores(lista, "VALORES DEL JUEGO DE DATOS (TODOS LOS DATOS)")
        elif opcion == "3":   # Opción 3
            punto_3(lista)
        elif opcion == "4":   # Opción 4
            filtrar(lista)
        elif opcion == "5":   # Opción 5
            desdoblamiento(lista)
        elif opcion == "6":   # Opción 6
            valoresTopN(lista)
        elif opcion == "7":   # Opción 7
            valoresMaximosMinimos(lista)
            

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
