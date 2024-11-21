print("EJERCICIO 1: Recuerdos devueltos")

contador = int(input("Ingrese un numero para iniciar su contador: "))
maximo = int(input("Ingrese el numero maximo deseado: "))

while contador <= maximo:
    contador += 1
    print("El numero actual es: ", contador)


""" 
ListNumers = [21,2,4,2,3,4,5]

print("DATOS DE SUMA! \n")
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

result = num1 + num2

print("El resultado de la suma es: ", result)

opcion = input("Elige una opción (1, 2, 3): ")

match opcion:
    case "1":
        print("Elegiste la opción 1")
    case "2":
        print("Elegiste la opción 2")
    case "3":
        print("Elegiste la opción 3")
    case _:
        print("Opción no válida")

print("Bucle de un arreglo!")
for i in range(len(ListNumers)):
    print(f"Iteracion {ListNumers[i]}") """