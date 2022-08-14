diccionario = {
        "Código":1, "Nombre":"Arandanos", "Precio":"Q.100.00",
        "Código2":2, "Nombre2":"Galletas", "Precio2":"Q.200.00",
        "Código3":3, "Nombre3":"Chocolate", "Precio3":"Q.20.00",
        "Código4":4, "Nombre4":"Dulces", "Precio4":"Q.10.00",
        "Código5":5, "Nombre5":"Maíz", "Precio5":"Q.5.00",
        "Código6":6, "Nombre6":"Fresas", "Precio6":"Q.10.00",
        "Código7":7, "Nombre7":"Platanos", "Precio7":"Q.5.00",
        "Código8":8, "Nombre8":"Helados", "Precio8":"Q.200.00",
        "Código9":9, "Nombre9":"Jabón", "Precio9":"Q.10.00",
        "Código10":10, "Nombre10":"Cemento", "Precio10":"Q.300.00",
        "Código11":11, "Nombre11":"Mangos", "Precio11":"Q.5.00",
        "Código12":12, "Nombre12":"Zapatos", "Precio12":"Q.500.00"
    }
print("Los productos almacenados son: ")
print(diccionario)

#Aumento de los productos del 10%:
diccionario = {
        "Código":1, "Nombre":"Arandanos", "Precio":"Q.100.00", "Aumento":"Q.110.00",
        "Código2":2, "Nombre2":"Galletas", "Precio2":"Q.200.00","Aumento2":"Q.220.00",
        "Código3":3, "Nombre3":"Chocolate", "Precio3":"Q.20.00","Aumento3":"Q.22.00",
        "Código4":4, "Nombre4":"Dulces", "Precio4":"Q.10.00","Aumento4":"Q.11.00",
        "Código5":5, "Nombre5":"Maíz", "Precio5":"Q.5.00","Aumento5":"Q.5,5.00",
        "Código6":6, "Nombre6":"Fresas", "Precio6":"Q.10.00","Aumento6":"Q.11.00",
        "Código7":7, "Nombre7":"Platanos", "Precio7":"Q.5.00","Aumento7":"Q.5,5.00",
        "Código8":8, "Nombre8":"Helados", "Precio8":"Q.200.00","Aumento8":"Q.220.00",
        "Código9":9, "Nombre9":"Jabón", "Precio9":"Q.10.00","Aumento9":"Q.11.00",
        "Código10":10, "Nombre10":"Cemento", "Precio10":"Q.300.00","Aumento10":"Q.330.00",
        "Código11":11, "Nombre11":"Mangos", "Precio11":"Q.5.00","Aumento11":"Q.5,5.00",
        "Código12":12, "Nombre12":"Zapatos", "Precio12":"Q.500.00","Aumento12":"Q.550.00"
    }

print("\nprecio + 10% del precio: ")
print("Código: ", diccionario["Código"],"Nombre: ", diccionario["Nombre"],"Precio: ", diccionario["Precio"],"Aumento: ", diccionario["Aumento"])
print("Código: ", diccionario["Código2"],"Nombre: ", diccionario["Nombre2"],"Precio: ", diccionario["Precio2"],"Aumento2: ", diccionario["Aumento2"])
print("Código: ", diccionario["Código3"],"Nombre: ", diccionario["Nombre3"],"Precio: ", diccionario["Precio3"],"Aumento3: ", diccionario["Aumento3"])
print("Código: ", diccionario["Código4"],"Nombre: ", diccionario["Nombre4"],"Precio: ", diccionario["Precio4"],"Aumento4: ", diccionario["Aumento4"])
print("Código: ", diccionario["Código5"],"Nombre: ", diccionario["Nombre5"],"Precio: ", diccionario["Precio5"],"Aumento5: ", diccionario["Aumento5"])
print("Código: ", diccionario["Código6"],"Nombre: ", diccionario["Nombre6"],"Precio: ", diccionario["Precio6"],"Aumento6: ", diccionario["Aumento6"])
print("Código: ", diccionario["Código7"],"Nombre: ", diccionario["Nombre7"],"Precio: ", diccionario["Precio7"],"Aumento7: ", diccionario["Aumento7"])
print("Código: ", diccionario["Código8"],"Nombre: ", diccionario["Nombre8"],"Precio: ", diccionario["Precio8"],"Aumento8: ", diccionario["Aumento8"])
print("Código: ", diccionario["Código9"],"Nombre: ", diccionario["Nombre9"],"Precio: ", diccionario["Precio9"],"Aumento9: ", diccionario["Aumento9"])
print("Código: ", diccionario["Código10"],"Nombre: ", diccionario["Nombre10"],"Precio: ", diccionario["Precio10"],"Aumento10: ", diccionario["Aumento10"])
print("Código: ", diccionario["Código11"],"Nombre: ", diccionario["Nombre11"],"Precio: ", diccionario["Precio11"],"Aumento11: ", diccionario["Aumento11"])
print("Código: ", diccionario["Código12"],"Nombre: ", diccionario["Nombre12"],"Precio: ", diccionario["Precio12"],"Aumento12: ", diccionario["Aumento12"])


#Modificación de un producto:
print("\n\nModificar un producto: ")
diccionario.update({"Código":"100000"})
diccionario.update({"Nombre":"NOMBRE INVENTADO"})
diccionario.update({"Precio":"100000"})
diccionario.update({"Aumento":"100000"})
print(diccionario)
