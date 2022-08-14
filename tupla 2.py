print("\n\nSolicitar 15 nombres y almacenarlos")

#Solicitar 15 nombres
nombres=[]
for i in range(15):
    nombres.append(input("Ingrese un nombre: "))

#Ordenar los nombres de forma ascendente
nombres.sort()
print ("\n\nOrden ascendente: ", nombres)

#Ordenar los nombres de forma descendente
nombres.sort(reverse=True)
print ("\n\nOrden descendente: ", nombres)


#Lista de nombres que terminan con vocal:
def vocaless(nombres):
    if nombres in ('a','e','i','o','u','A','E','I','O','U'):
        return 'vocal'
    elif letra in ('y','Y'):
        return 'vocal/consonante'
    else:
        return 'consonante'

print(vocaless)
