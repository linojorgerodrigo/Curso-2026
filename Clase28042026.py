'''
'''


'''
1. Ejercicio 1: El Cajero Automático
Un cliente quiere retirar dinero de un cajero. El programa debe pedir el PIN (la clave es
1234). Si el usuario se equivoca, el programa debe pedir la clave otra vez.
Consigna: El bucle debe repetirse mientras la clave ingresada sea incorrecta.
Plus: Si se equivoca 3 veces, mostrar un mensaje de "Tarjeta Bloqueada" y terminar.

'''

'''
pin_correcto = "1234"
intentos = 0
acceso = False

while intentos < 3 and acceso==False:
    pin = input("Ingresá tu PIN: ")
    
    if pin == pin_correcto:
        print("Acceso permitido")
        acceso = True
        
    else:
        intentos = intentos+1
        print("PIN incorrecto te quedan ",3 - intentos,' intentos')

if intentos == 3:
    print("Tarjeta bloqueada")

'''

'''
pin_correcto = "1234"
intentos = 0


while intentos < 3:
    pin = input("Ingresá tu PIN: ")
    
    if pin == pin_correcto:
        print("Acceso permitido")
        break
        
    else:
        intentos = intentos+1
        print("PIN incorrecto te quedan",3 - intentos,"intentos")

if intentos == 3:
    print("Tarjeta bloqueada")

'''





'''
2. Liquidación de Cuotas (Bucle PARA)
Una concesionaria de autos en Bahía Blanca ofrece un plan de pago. El usuario ingresa
el monto total de un repuesto y la cantidad de cuotas (entre 2 y 12).
Consigna: Usar un bucle Para para mostrar en pantalla cuánto debe pagar el cliente en
cada mes.
Ejemplo de salida: * "Cuota 1: $5000"
Cuota 2: $5000" ...
Cuota3: $5000 ....
'''

'''
monto = float(input("Ingrese monto del producto: "))
cant_cuotas = int(input("Ingrese cantidad de cuotas entre 2 y 12: "))
cuotas = monto/cant_cuotas

print("------------------------------------------------")
print("Monto total a liquidar en ",cant_cuotas,"cuotas: $",monto)
print("------------------------------------------------")
print("Pago detallado de las ",cant_cuotas,"cuotas:")
print("------------------------------------------------")

for n in range(1,cant_cuotas + 1):
    print("Cuota ",n, ": $",cuotas)

print("¡Plan de pago en ",cant_cuotas,"cuotas finalizado!")
'''











'''
3. Control de Stock (Bucle MIENTRAS)
Un pequeño comercio necesita cargar sus ventas del día hasta que decidan cerrar la caja.
Consigna: El programa debe pedir el precio de los productos vendidos uno por uno. El
ingreso de datos termina cuando el usuario ingresa un precio igual a 0. Al final, el
programa debe mostrar el Total General de la venta.
'''

'''
precio_producto = float(input("Ingrese monto del producto: "))

total=0

while  precio_producto !=0:
    
    
    total=total+precio_producto
    precio_producto = float(input("Ingrese monto del producto: "))
    
print("Total ventas del día: $",total)
'''



'''
4. Contador de Divisores (Integrador)
El usuario ingresa un número cualquiera.
Consigna: El programa debe recorrer con un bucle Para los números del 1 al 10. En
cada vuelta, debe verificar si el número ingresado es divisible por el número actual del
bucle.
Salida: Mostrar en pantalla solo los números que sean divisores exactos.
'''

'''
numero = int(input("Ingrese un numero cualquiera: "))

for n in range(1,11):
    if numero % n == 0:
        print(n)

'''





'''
5. El Validador de Notas (Validación de datos)
En un curso de programación, las notas van del 1 al 10.
Consigna: Pedir al usuario que ingrese una nota. Si la nota es menor a 1 o mayor a
10, usar un bucle para obligar al usuario a ingresar la nota otra vez hasta que sea
válida. Una vez válida, decir si está "Aprobado" (7 o más) o "Desaprobado".
'''

'''
nota = int(input("Ingrese nota: "))

while nota <1 or nota >10:
    nota = int(input("Ingrese nota: "))
if nota >=7:
    print('El alumno está Aprobado!')
else:
    print('El alumno está Desaprobado!')
'''


'''
6. El Número Primo
Concepto: Un número es primo si solo es divisible por 1 y por sí mismo (tiene
exactamente 2 divisores).
Enunciado:
Escribir un programa que pida al usuario ingresar un número entero positivo. El
programa debe determinar si el número es Primo o No Primo.
Pista para el alumno: Debés usar un bucle (Para o Mientras) que cuente cuántas
veces el resto de la división (n MOD i) da cero al dividirlo por todos los números
menores a él.
Condición final: Si al terminar el bucle el contador de divisores es igual a 2, el
número es primo.

'''


'''
7. El Número Perfecto
Concepto: Un número perfecto es aquel que es igual a la suma de sus divisores
propios (todos sus divisores excepto él mismo).
Ejemplo: El 6 es perfecto porque sus divisores son 1, 2 y 3. Si los sumamos: $1 + 2
+ 3 = 6
Enunciado:
Realizar un algoritmo que solicite un número al usuario y determine si es un
Número Perfecto.
Pista para el alumno: Necesitás un bucle que recorra desde el 1 hasta el número
anterior al ingresado. Si encontrás un divisor, debés ir sumándolo en una variable
"acumuladora".
Condición final: Al finalizar, compará si la suma obtenida es igual al número
original.

'''


'''
8. Desafío Integrador (Búsqueda de Primos)
Si ves que avanzan rápido, podés darles este que es más complejo:
Enunciado:
Hacer un programa que muestre por pantalla todos los números primos que existen
entre el 1 y el 100.


Ayuda: Aquí el alumno tendrá que usar un bucle dentro de otro bucle (bucles
anidados). Un bucle para ir del 1 al 100, y otro interno para verificar si cada uno de
esos números es primo.

'''
