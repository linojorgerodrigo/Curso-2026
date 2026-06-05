#Comercio

# 1. Importamos el módulo datetime
from datetime import date

fecha = date.today()
#Modulo 1
def calcular_iva(subtotal, tasa_iva=21):
    return subtotal * (tasa_iva / 100)

def calcular_descuento(subtotal, porcentaje_descuento):
    return subtotal * (porcentaje_descuento / 100)

def imprimir_ticket(comercio, producto, subtotal, porcentaje_desc=0):
    descuento = calcular_descuento(subtotal, porcentaje_desc)
    subtotal_con_descuento = subtotal - descuento
    iva = calcular_iva(subtotal_con_descuento)
    total = subtotal_con_descuento + iva
    
    print("\n" + "=" * 40)
    print(f"{comercio.upper():^40}")
    print("=" * 40)
    print("--- Fecha: ",fecha, "---")
    print("=" * 40)
    print(f"Detalle: {producto}")
    print("-" * 40)
    print(f"Subtotal bruto:          ${subtotal:>10.2f}")
    
    if porcentaje_desc > 0:
        print(f"Descuento ({porcentaje_desc}%):       -${descuento:>10.2f}")
        print(f"Subtotal neto:           ${subtotal_con_descuento:>10.2f}")
        
    print(f"IVA (21%):               +${iva:>10.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR:           ${total:>10.2f}")
    print("=" * 40)
    print(f"{'¡Gracias por su compra!':^40}")
    print("=" * 40 + "\n")

#Modulo 2
# --- ENTRADA DE DATOS ---
print("--- SISTEMA DE VENTAS ---")
print("--- Fecha: ",fecha, "---")
producto = input("Nombre del producto: ")

# Validamos que los números sean correctos
try:
    subtotal = float(input("Ingrese el precio del producto: $ "))
    descuento = float(input("Ingrese el % de descuento (0 si no tiene): "))
    
    # Pasamos los 4 argumentos en el orden correcto:
    # 1. Comercio ("Mi Comercio")
    # 2. Producto
    # 3. Subtotal
    # 4. Descuento
    imprimir_ticket("Mi Comercio", producto, subtotal, descuento)

except ValueError:
    print("\n[!] Error: Por favor, ingrese solo números para el precio y el descuento.")