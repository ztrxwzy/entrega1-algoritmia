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
    print("*" * 50  )

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
        


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    numeros = []
    separadorAsterisco()
    numeros = generarNumeros(numeros)
    
    print(numeros)
    
    numeros = generarNumeros(numeros)

    
    print(numeros)
   
    

main()

