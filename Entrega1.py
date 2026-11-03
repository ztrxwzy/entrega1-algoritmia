"""
-----------------------------------------------------------------------------------------------
Título: practica clase 05 
Fecha:23-9
Autor:Carbonari Santino

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
    for i in range(50):
        print("*",end="")
    print()

def generarNumeros(numeros):
    
    
    if len(numeros) > 0:
        respuesta = input("Lista detectada ¿desea remplazarla? (si = 1) (no = 0) ")
        if respuesta == "1": 
            numeros.clear()
            
        else:
            return numeros
    
    cantidad = int(input("¿Cuántos números querés generar? "))
    
    
    for i in range (0,cantidad):
        numero =  random.randint (0,99999)
        numeros.append(numero)
    return numeros
        
def valoresTopN(numeros):
    """
    Identifica y muestra los N valores mayores únicos de una lista.

    Parámetros:
        numeros: Lista de números enteros.

    Retorno:
        Ninguno.
    """

    if len(numeros) == 0:
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

        for numero in numeros:
            if numero not in ranking:
                if mayor is None or numero > mayor:
                    mayor = numero

        if mayor is None:
            break

        ranking.append(mayor)

    print("*******************************************************************************")
    print("VALORES DEL JUEGO DE DATOS (DATOS TOP N)")
    print("*******************************************************************************")

    for i in range(len(ranking)):
        print(i + 1, ". ", ranking[i], sep="")

    print("*******************************************************************************")

    if len(ranking) < n:
        print("Se solicitaron", n, "valores, pero solo existen",
              len(ranking), "valores únicos disponibles.")

"""
                            PUNTOS 4 Y 5
"""

def validacionLetra(letrasValidas, caracter):
    """
    Valida la letra ingresada verificando que esté en la lista de letras válidas

    Parametros:
        letrasValidas (list): lista de letras válidas
        caracter (str): caracter que el usuario ingresa y será validado
    """
    validacion = False
    while not validacion:
        if caracter not in letrasValidas:
            print("Caracter ingresado invalido.")
        else:
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
    
    criterio = input("Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]:")
    
    validacion = validacionLetra(letrasValidas, criterio)
    
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
            
    mostrar_tabla(listaFiltrada, "VALORES DEL JUEGO DE DATOS (DATOS FILTRADOS)")
            
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
        Filtra una lista de numeros, solo guarda los numeros dentro del rango indicado indicado.
            
        Parametro:
            lista (list): lista de numeros
            
        Retorna:
            listaFiltrada (list): lista de numeros filtrada
        """
    
    listaFiltrada = []
    
    minimo = pedir_numero("Ingrese el mínimo: ", 0, 999)
    maximo = pedir_numero("Ingrese el maximo: ", 0, 999)
    
    for i in lista:
        if i <= maximo and i >= minimo:
            listaFiltrada.append(i)
            
    return listaFiltrada

def numerosPar(lista):
    
    """
        Filtra una lista de numeros, solo guarda los numeros pares.
            
        Parametro:
            lista (list): lista de numeros
            
        Retorna:
            None
        """
    
    listaFiltrada = []
    
    for i in lista:
        if i % 2 == 0:
            listaFiltrada.append(i)

    print("Valores pares:")
    mostrar_tabla(listaFiltrada, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")

def numerosImpar(lista):
    
    """
        Filtra una lista de numeros, solo guarda los numeros impares.
                
        Parametro:
            lista (list): lista de numeros
                
        Retorna:
            None
            """
    
    listaFiltrada = []
    
    for i in lista:
        if i % 2 != 0:
            listaFiltrada.append(i)
                    
    print("Valores impares:")
    mostrar_tabla(listaFiltrada, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")


def criterioCantCifras(lista):
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
    mostrar_tabla(listaUnaCifra, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 2 cifras:")
    mostrar_tabla(listaDosCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 3 cifras:")
    mostrar_tabla(listaTresCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 4 cifras:")
    mostrar_tabla(listaCuatroCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores de 5 cifras:")
    mostrar_tabla(listaCincoCifras, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")

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
    mostrar_tabla(hasta_umbral, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")
    print("Valores por encima del umbral:")
    mostrar_tabla(sobre_umbral, "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS)")


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
    
    criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
    
    validacion = validacionLetra(letrasValidas, criterio)
    
    if validacion:
            
            if (criterio == "P" or criterio == "p"):
                numerosPar(lista)
                numerosImpar(lista)
            
            elif criterio == "C" or criterio == "c":
                criterioCantCifras(lista)

            else:
                criterioPorValor(lista)
 

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    numeros = []
    separadorAsterisco()
    numeros = generarNumeros(numeros)
    print(numeros)
    valoresTopN(numeros)

main()
