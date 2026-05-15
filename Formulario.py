import customtkinter as ctk # Importamos la librería moderna
from tkinter import messagebox # El cartel de mensajes sigue siendo el estándar

# 1. Configuración de la apariencia
ctk.set_appearance_mode("System")  # Detecta si Windows está en modo oscuro o claro
ctk.set_default_color_theme("blue") # Temas disponibles: "blue", "green", "dark-blue"

# 2. Lógica del programa (Es igual a la anterior)
def validar_multiplo():
    try:
        n1 = int(entrada_nro1.get())
        n2 = int(entrada_nro2.get())
        
        if n1 % n2 == 0:
            messagebox.showinfo("Resultado", f"Sí, {n1} es múltiplo de {n2}.")
           
        else:
            messagebox.showwarning("Resultado", f"No, {n1} no es múltiplo de {n2}.")
           
            
    except ValueError:
        messagebox.showerror("Error", "Ingresá solo números enteros.")
        
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")
    
    finally:
        entrada_nro1.delete(0, 'end')
        entrada_nro2.delete(0, 'end')
        entrada_nro1.focus()
        

# 3. Interfaz Gráfica con CustomTkinter
ventana = ctk.CTk() # Nota que ahora es CTk en lugar de Tk
ventana.title("Validador Moderno - FP")
ventana.geometry("400x320")


# Usamos CTkLabel en lugar de Label
titulo = ctk.CTkLabel(ventana, text="Validador de Múltiplos", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# Primer campo
ctk.CTkLabel(ventana, text="Primer número:").pack(pady=0)
entrada_nro1 = ctk.CTkEntry(ventana, placeholder_text="Ej: 10") # Agregamos texto de ayuda
entrada_nro1.pack(pady=10)



# Segundo campo
ctk.CTkLabel(ventana, text="Segundo número:").pack(pady=0)
entrada_nro2 = ctk.CTkEntry(ventana, placeholder_text="Ej: 2")
entrada_nro2.pack(pady=10)

# Botón Moderno (CTkButton)
boton = ctk.CTkButton(ventana, text="Verificar", command=validar_multiplo)
boton.pack(pady=20)




ventana.mainloop()