import tkinter as tk
from tkinter import ttk, messagebox
from derivacion import obtener_parser, derivacion_paso_a_paso, obtener_arbol, obtener_ast

def mostrar_resultados():
    expresion = entrada_expresion.get().split()  # Tokeniza la entrada en lista
    direccion = direccion_var.get()
    if direccion not in ["izquierda", "derecha"]:
        messagebox.showerror("Error", "Por favor, elige 'izquierda' o 'derecha'.")
        return

    parser = obtener_parser(direccion)

    # Mostrar derivación paso a paso
    try:
        derivaciones = derivacion_paso_a_paso(parser, expresion)
        resultado_derivacion.delete(1.0, tk.END)
        for derivacion in derivaciones:
            resultado_derivacion.insert(tk.END, derivacion + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo derivar la expresión: {e}")
        return

    # Mostrar árbol de derivación
    try:
        obtener_arbol(parser, expresion)  # Abre el árbol de derivación en una ventana gráfica
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el árbol de derivación: {e}")
        return

    # Mostrar el AST
    try:
        obtener_ast(parser, expresion)  # Abre el AST en una ventana gráfica
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el AST: {e}")
        return

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Derivación de Expresiones y AST")
ventana.config(bg="#A9D0F5")  # Color azul claro de fondo

# Entrada de la expresión
tk.Label(ventana, text="Expresión:", bg="#A9D0F5").grid(row=0, column=0, padx=10, pady=10)
entrada_expresion = tk.Entry(ventana, width=50)
entrada_expresion.grid(row=0, column=1, padx=10, pady=10)

# Selección de la dirección de derivación
tk.Label(ventana, text="Dirección:", bg="#A9D0F5").grid(row=1, column=0, padx=10, pady=10)
direccion_var = tk.StringVar(value="izquierda")
ttk.Radiobutton(ventana, text="Izquierda", variable=direccion_var, value="izquierda").grid(row=1, column=1, padx=10, pady=5, sticky="w")
ttk.Radiobutton(ventana, text="Derecha", variable=direccion_var, value="derecha").grid(row=1, column=1, padx=10, pady=5, sticky="e")

# Botón para mostrar los resultados
boton_derivar = tk.Button(ventana, text="Generar Derivación y AST", command=mostrar_resultados, bg="#A9D0F5")
boton_derivar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Área de texto para mostrar la derivación paso a paso
tk.Label(ventana, text="Derivación paso a paso:", bg="#A9D0F5").grid(row=3, column=0, padx=10, pady=10)
resultado_derivacion = tk.Text(ventana, height=10, width=80)
resultado_derivacion.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia el bucle principal de la interfaz
ventana.mainloop()
