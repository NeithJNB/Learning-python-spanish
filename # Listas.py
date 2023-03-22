# Listas

lista = [1,2,4,5]
lista2 = [11,12,13,14,15]

print("La lista 1 es: ",lista)
print("La lista 2 es: ",lista2)

#El comando .append() nos sirve para agregar algo a la lista en la ultima pocicion.
lista.append(6)
print("Agregando el numero 6 a la lista...\n")
print("La lista 1 ahora es: ", lista,"\n")
print("Agregando el numero que falta (3)...\n")

#El comando .extend() nos permite insertar algo en la lista
#en una pocicion determinada, de esta forma: 
#         (2,3)(a,b) En la pocicion "a" se inserta "b" 
lista.insert(2,3)

print("La lista 1 ahora es: ",lista,"\n")
print("Agregando los numeros del 7 al 10 a la lista 1...\n")

#La funcion .extend sirve para extender la lista. Funciona como una "Concatenacion" a la lista.
lista.extend([7,8,9,10])

print("La lista 1 ahora es: ",lista)
print("Sumando lista 1 + lista 2...\n")
#Las listas tambien se pueden concatenar de la manera original (a+b)
lista3 = lista + lista2

print("La suma de la lista 1 y lista 2 es: ",lista3,"\n") 
print("¡Ahora se llama lista 3!\n\n")

print("El valor '5' está en la lista3?: ")

#Se "pregunta" si '5' está en la lista, si está da true, si no, da false
5 in lista3
if True:
    print("Si")
else:
    print("No")



print("En que pocicion está '5' en la lista3?: ")

#Se indica el valor que se quiere saber, en este caso es '5' así:
print(lista.index(5))

print("La lista 4 es: ")
lista4= [1,2,3,4,8,6,1,2,4,8]

print(lista4,"\n\n")
print("Cuantas veces está el numero '1' en la lista4?")

#Entre los parentecis se escribe lo que se quiere "contar" en este caso el 1
print(lista4.count(1)) 

print("Quiero eliminar el numero '3' de la lista!")

#La funcion .pop se encarga de eliminar el elemento que queramos de la lista dandole la pocición de este en la lista.
lista4.pop(2)

print("La lista 4 queda así: ",lista4,"\n")

print("Ahora quiero eliminar el numero '6'  de la lista!")

#La funcion .remove() nos elimina el elemento que queramos dandole el elemento que queramos eliminar.
lista4.remove(6)

print("La lista 4 queda así: ",lista4,"\n")

print("Ahora quiero eliminar todos los elementos de la lista 4!")

#La funcion .clear() nos permite eliminar todos los elementos en una lista
lista4.clear()

print("La lista 4 queda así: ",lista4,"\n\n\n")

lista5 = [1,2,3,4,5]

print("La lista 5 es: ",lista5,"\n")

print("Quiero que la lista se de la vuelta!")

#La funcion reverse hace que la lista quede en reversa a como se rellenó.
lista5.reverse()

print("La lista 5 quedó así: ",lista5,"\n")

print("Ahora quiero que la lista se copie dos veces!")

lista5= lista5 * 2

print("La lista 5 queda asi: ",lista5,"\n\n\n")

lista6= [5,4,-7,9,0,1,3]

print("La lista 6 es: ",lista6,"\n\n")

print("Quiero que la lista quede acomodada de menor a mayor!\n")

#La funcion .sort() nos ayuda a ordenar la lista de enteros de menor a mayor.
lista6.sort()

print("La lista 6 queda asi: ",lista6,"\n")

print("Ahora de mayor a menor!\n")

#Si le agregamos en los parentecis la oracion "reverse=True" se ordenará de mayor a menor.
lista6.sort(reverse=True)

print("La lista 6 queda así: ",lista6,"\n")
