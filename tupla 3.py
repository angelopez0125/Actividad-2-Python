print("\n\nSolicitud de 10 numeros")

lista=[]
for numeros in range(10):
    valor=int(input("Ingrese un número:"))
    lista.append(valor)
    
#Mostrar el número mayor y menor:
mayor=lista[0]
menor=lista[0]
posicion=0

for numeros in range(10):
    if lista[numeros]>mayor:
        mayor=lista[numeros]
    
    if lista[numeros]<menor:
        menor=lista[numeros]
        posicion=numeros
print("\nEl número mayor es: ",mayor)
print("\nEl número menor es: ",menor)

#Mostar los datos de forma descendente:
print("\nOrden descendente: ")
lista.sort()
print (lista)


#Mostrar la suma de los números:
listaSuma= sum(lista)
print("\nLa suma de los número es: ",listaSuma)

#Indicar si la suma es un número primo;
def es_primo(listaSuma):
    n=int(2)
    band= True
    
    while band and (n < listaSuma):
        if listaSuma % n == 0:
           band = False
        else:
            n += 1
    return band

print("El número: ",es_primo(listaSuma))

    
