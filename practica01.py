import time
import random
inicio = time.time()

array=random.sample(range(50),20)
print("El arreglo sin ordenar es: ", array)


def ord_burbuja(array):
    

    for i in range(len(array)):
        for j in range(len(array)-i-1):

            if array[j]> array[j+1]:
                aux=array[j]
                array[j]=array[j+1]
                array[j+1]=aux
    print("El arreglo ordenado es: ",array)

def burbuja_optimizada(array):
    for i in range(len(array)):
        intercambio= False
        for j in range (len(array)-i-1):
            if array[j]>array[j+1]:
                aux=array[j]
                array[j]=array[j+1]
                array[j+1]=aux
                intercambio = True
        if intercambio == False:
            break

eleccion=0
while eleccion!=6:

    print("""
          
          Seleccione el método para ordenar el arreglo:
          
          1) Método de burbuja 
          2) Método superburbuja  
          3) Salir 
          """)
    eleccion=int(input())
    
    if eleccion == 1:
        ord_burbuja(array)

        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print("El tiempo que tarda en ejecutarse es :")
        print(tiempo_ejecutado)
       

    if eleccion == 2:
        burbuja_optimizada(array)
        print("El arreglo ordenado es: ",array)
        fin =time.time()
        tiempo_ejecutado = fin - inicio
        print("El tiempo que tarda en ejecutarse es :")
        print(tiempo_ejecutado)

    

    if eleccion == 3:
        print("Gracias por su tiempo :")
        
    break
