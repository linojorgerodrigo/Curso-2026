from datetime import date, datetime
import random


import customtkinter as ctk
from tkinter import messagebox

""""
hoy = date.today()

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
np = nombre +" "+ apellido

fecha_nac = input("Ingrese su fecha de nacimiento (DD-MM-YYYY): ")


edad = int(input("Ingrese su edad: "))

# Formateo de fechas
hoy_formateado = hoy.strftime("%d-%m-%Y")

print(" ")
print("El día de hoy: ", hoy_formateado)
print(" ")
print("Nombre completo: " , np)
print("Su fecha de nacimiento es: ", fecha_nac)
print("Su edad es: ", edad)
"""


#------------------------------------
"""
n1 = int(input("Ingrese un numero: "))
n2 = random.randint(1,10)
if n1 == n2:
    print("es igual a:",n2)
else:
    print("No es igual. El número era: ", n2)
    
"""
#------------------------------------

"""
anio_actual=date.today().year

edad=int(input('ingrese su edad: '))
anio_nac=anio_actual-edad

print('el año de nacimiento es: ',anio_nac)

"""

#---------------------------------------
"""
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

if n1 == n2:
    print("los nuemros ingresados son iguales")
else:
    print("los nuemros ingresados NO son iguales")

if n1 >= n2:
    print(n1,'es mayor a ', n2)
else:
    print(n1,'NO es mayor que ', n2)

"""

#-----------------------------------------------
'''
n1 = int(input("Ingrese un numero: "))

if n1 % 2 == 0:
    print(n1, 'es par')
else:
    print(n1,'es inpar')
    
'''

'''
numero = int(input("Ingresá un número: "))

if numero != 0:
    if numero > 0:
        if numero % 2 == 0:
            print("El número es distinto de 0, positivo y par")
        else:
            print("El número es positivo pero impar")
    else:
        print("El número es distinto de 0 pero negativo")
else:
    print("El número es 0")

'''


'''
numero = int(input("Ingresá un número de varios digitos: "))

digito = numero %10

print(digito)

if digito != 0 and digito >0:
    if digito > 0:
        if digito % 2 == 0:
            print("El número es distinto de 0, positivo y par")
        else:
            print("El número es positivo pero impar")
    else:
        print("El número es distinto de 0 pero negativo")
else:
    print("El número es 0")

'''


#----------------------------------------------------------
'''
1. El Cuadrado (Un cuadrado tiene 4 lados iguales.)
    a. Consigna: Crea una variable llamada lado. Asignale el valor 5.
    b. Crea una variable llamada perimetro_cuadrado y realizá el cálculo
    matemático para obtener el total. (EL resultado es 20)
    c. Al ejercicio anterior introducir los ajustes necesarios para que te pida por
    pantalla “Ingresar un Nro”
'''

'''
lado = 5
perimetro_cuadrado = lado * 4
print (perimetro_cuadrado)

'''

'''
lado = int(input("ingrese medida de un lado del cuadrado: "))
perimetro_cuadrado = lado * 4
print (perimetro_cuadrado)
'''

#----------------------------------------------------------
'''
2. El Rectángulo (Un rectángulo tiene dos pares de lados iguales (base y altura).
    a. Consigna: Crea las variables base = 10 y altura = 5
    b. Desafío: Calculá el perímetro (Resultado : 30)
    c. Al ejercicio anterior introducir los ajustes necesarios para que te pida por
    pantalla “Ingresar sus respectivos valores de forma manual”
'''

'''
base = 10
altura = 5

perímetro = (base + altura)*2
print (perímetro)

'''
'''
base = int(input("ingrese medida de la base del rectangulo: "))
altura = int(input("ingrese medida de la altura del rectangulo: "))

perímetro_rectangulo = (base + altura)*2
print (perímetro_rectangulo)
'''
#----------------------------------------------------------
'''
3. El Calculador de Asados (Suma y Multiplicación)
    a. Enunciado: Crea un programa que pida al usuario cuántos kilos de carne
    compró y cuánto pagó por kilo.
    b. Objetivo: Calcular el gasto total.
    c. Pista: Usá float(input()) porque el precio puede tener decimales.
'''
'''
kilos = float(input("ingrese cantidad de kilos comprados: "))
precio_por_kilo = float(input("ingrese precio por kilo: "))
costo_final = kilos * precio_por_kilo
print(costo_final)

'''
#----------------------------------------------------------
'''
4. ¿Es Par o Impar? (Módulo y Condicional)
    a. nunciado: Pedí al usuario que ingrese un número entero. El programa
    debe decir si el número es "Par" o "Impar".
    b. Lógica: Si el resto de dividir el número por 2 es igual a 0 (numero % 2
    == 0), es par.

'''
'''
numero = int(input("Ingresá un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
'''
#----------------------------------------------------------
'''
5. Repartidor de Caramelos (Resto de una división)
    a. Enunciado: Un abuelo tiene una cantidad de caramelos y quiere
    repartirlos equitativamente entre sus 3 nietos
    b. Consigna: Pedí la cantidad de caramelos por teclado. Informá cuántos le
    tocan a cada nieto y cuántos sobran (el resto).
    c. Pista: Usá / para la división y % para el sobrante.

'''
'''    
caramelos = int(input("Ingresá la cantidad de caramelos: "))
cada_nieto = caramelos /3
sobrante = caramelos%3
print(cada_nieto)

if cada_nieto % 3 == 0:
    print("no sobraron caramelos")
else:
    print("sobraron ",sobrante ,"caramelos")
'''

#----------------------------------------------------------
'''
6. Control de Acceso (Condicional Básico)
a. Enunciado: Pedí al usuario su año de nacimiento. Calculá su edad actual
(asumiendo que estamos en 2026).
b. Consigna: Si es mayor o igual a 18, mostrá el mensaje "Acceso
Permitido". Si no, mostrá "Acceso Denegado".

'''

'''
anio_nac = int(input("Ingrese año de nacimiento: "))
anio_actual = 2026
edad = anio_actual - anio_nac
if edad >= 18:
    print('acceso permitido')
else:
    print('acceso denegado')

'''


'''
fecha_nac = input("Ingrese su fecha de nacimiento (DD-MM-YYYY): ")
fecha_actual = date.today()
# Formateo de fechas
#hoy_formateado = fecha_actual.strftime("%d-%m-%Y")
'''

'''
nro =int(input("Ingrese un nro: "))
dig = nro/100
print(dig)
dig = nro//100
print(dig)
dig = nro%100
print(dig)
'''
#----------------------------------------------------------
'''
7. El Descuento del 15% (Porcentajes)
    a. Enunciado: Una tienda de computación en Bahía Blanca ofrece un
    descuento del 15% por pago en efectivo.
    b. Consigna: Pedí el precio del producto. Calculá cuánto es el descuento y
    cuál es el precio final a pagar.
    c. Fórmula: descuento = precio * 0.15

'''

'''
precio = int(input("Ingrese precio: "))
descuento = precio*15/100
precio_final = precio-descuento

print(precio_final)

'''
#----------------------------------------------------------
'''
8. El validador de múltiplos:
    a. Pedí dos números al usuario. El programa debe informar si el primero es
    múltiplo del segundo
    b. Ejemplo: Si ingresa 10 y 5, debe decir "Sí, 10 es múltiplo de 5" (porque
    10 % 5 es 0).

'''

'''
num1 = int(input("Ingrese el primer nro: "))
num2 = int(input("Ingrese el segundo nro: "))

if num1 % num2 == 0:
    print('Sí' ,num1, 'es múltiplo de' ,num2)
else:
    print('No' ,num1, 'es múltiplo de' ,num2)

'''





#----------------------------------------------------------
'''
9. Calculadora de IVA: Pedí al usuario el precio de un producto y mostrá por
    pantalla el precio final con el IVA (21%) incluido.

'''

'''
precio = float(input("Ingrese precio: "))
iva = precio*21/100
precio_final = precio + iva
print(precio_final)

'''





#----------------------------------------------------------
'''
10. Conversor de Moneda: Diseñá un programa que pida una cantidad en Pesos
Argentinos y el tipo de cambio del día (Dólar). Mostrá cuántos dólares puede
comprar el usuario.
'''
'''
pesos = float(input('ingrese la cantidad en pesos: '))
tipo_de_cambio = 1381.87
dolar = pesos / tipo_de_cambio
print('la cantidad de dolares que podes comprar son: ',dolar)
'''



#----------------------------------------------------------
'''
11. Promedio de Notas: Pedí al usuario tres notas de un alumno. Calculá y mostrá el
promedio final.
'''

'''
nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segundo nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

promedio =(nota1+nota2+nota3)/3
print(promedio)

'''

#----------------------------------------------------------
'''
12. Reparto Equitativo: Un grupo de amigos quiere repartir una cuenta de $15.000$
en partes iguales. Pedí la cantidad de amigos e informá cuánto debe poner cada
uno y si sobra algún centavo (el resto).
'''

'''
monto = float(input("Ingrese monto a repartir: "))
personas = int(input("Ingrese cantidad de persona a repartir: "))


monto_por_persona =monto/personas
print(monto_por_persona)

'''

#----------------------------------------------------------
'''
13. Múltiplo de 5: Pedí un número y determiná si es múltiplo de 5. El programa
debe mostrar 0 si es múltiplo y un número distinto de cero si no lo es (usando
%).
'''

'''
num = int(input("Ingresá un número: "))

resultado = num % 5

if resultado == 0:
    print('es multiplo de 5 porque el resto es: ',resultado)
else:
    print('No es multiplo de 5 porque el resto es: ', resultado)

'''


#----------------------------------------------------------
'''
14. Minutos a Horas: Pedí al usuario una cantidad de minutos (ej: 150). Informá
cuántas horas completas son y cuántos minutos sobran.
a. Pista: Usá // para las horas y % para los minutos restantes.
'''



#----------------------------------------------------------
'''
15. Descuento de Jubilados: Pedí el precio de un medicamento y la edad del cliente.
Si tiene 65 años o más, aplicá un descuento del 40% e informá el precio final.
(Aquí usá un if).
'''





#----------------------------------------------------------
'''
16. Diferencia de Goles: Pedí los goles de dos equipos que jugaron un partido
(Equipo A y Equipo B). Informá cuántos goles de diferencia hubo en el
resultado.
'''




#===================================================================================

'''
numero = int(input("Ingresá un número: "))

while (numero==0)or(numero<=10):
    numero = numero +1
    print(numero)
'''   

'''
numero = int(input("Ingresá un número: "))

while (numero!=0)and(numero<=10):
    numero = numero +1
    #print(numero)
if (numero==0)and(numero<=10):
    print(numero)
else:
    print(numero, "no cumple con ser igual a 0 ni meno ó igual a 10")
    
'''

'''
1. Contador de Intervalos:
    Diseñar un programa que solicite al usuario un número entero positivo y muestre
    por pantalla todos los números desde el 1 hasta el número ingresado, de uno en
    uno.
'''

'''
numero = int(input("Ingresá un número: "))
contador = 0

while contador < numero:
    contador = contador+1
    print(contador)

'''


'''
2. Validación de Datos (Password):
    Crear un algoritmo que simule el acceso a un sistema. El programa debe solicitar
    una contraseña (por ejemplo: "1234"). Mientras la contraseña ingresada sea
    incorrecta, el sistema debe mostrar un mensaje de "Error, intente de nuevo" y
    volver a pedirla. Si es correcta, mostrar "Acceso concedido".
'''




'''
contra = '1234'
passw = input("Ingrese su contraseña: ")

while passw != contra:
    print('Error, intente de nuevo')
    passw = input("Ingrese su contraseña: ")
print("Acceso concedido")
    
'''   

    




'''
3. Generador de Tabla de Multiplicar:
    Solicitar al usuario un número (del 1 al 10) y mostrar su tabla de multiplicar
    completa. El bucle debe iterar desde el 1 hasta el 10, calculando y mostrando el
    resultado en cada paso (Ej: 5 x 1 = 5, 5 x 2 = 10...).
'''


'''
numero = int(input("Ingresá un número del 1 al 10: "))
contador = 0

while contador < 10:
    
    contador = contador+1
    mostrar= numero*contador
    
    
    print(mostrar)
'''  




'''
4. Promedio de Notas con Límite:
    Desarrollar un programa que pregunte al usuario cuántas notas desea cargar.
    Luego, mediante un bucle, solicitar cada una de las notas y, al finalizar la carga,
    calcular y mostrar el promedio general del alumno.
'''

'''
cant_notas = int(input("Ingresá cantidad de notas a cargar: "))
contador = 0
total_notas=0
while contador < cant_notas :
    
    contador = contador + 1
    notas= float(input("Ingresá nota: "))
    
    total_notas = float(total_notas + notas)
    
promedio=total_notas /cant_notas
    
print('El promedio de notas es: ',promedio)

'''   


'''

5. Filtrado de Números Pares:
    Desarrollar un programa que solicite al usuario un número entero positivo N. El
    algoritmo debe mostrar por pantalla todos los números pares comprendidos entre
    el 1 y el N.
    Restricción: Utilizar el operador de módulo (%) dentro del while para verificar
    la paridad antes de imprimir.
''' 

'''

numero = int(input("Ingresá un número entero positivo: "))
contador = 1

while contador <= numero:
    if contador %2 == 0:
        print(contador)
    contador += 1

'''    


   
'''
6. Búsqueda de Máximos y Mínimos:
    Escribir un programa que permita al usuario ingresar una serie de números
    positivos (uno por uno). El ingreso finalizará cuando el usuario introduzca un
    número negativo. Al terminar, el programa debe informar cuál fue el número
    máximo ingresado durante toda la secuencia.
'''


'''
numero = int(input("ingrese un numero positivo: "))
maximo = numero

while numero >= 0:
    if numero > maximo:
        maximo = numero
    numero = int(input("ingrese un numero positivo: "))

print("Máximo:", maximo)

'''



#-----------------------------------------------------------



 