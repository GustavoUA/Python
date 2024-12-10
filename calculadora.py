import tkinter as tk

# Función para actualizar la pantalla de la calculadora
#eval evalua la pantalla todo lo que pongamos devuelve error sino se puede calcular.
def agregar_simbolo(simbolo):
    if simbolo == 'C':
        pantalla.delete(0, tk.END)
    elif simbolo == '=':
        try:
            resultado = str(eval(pantalla.get()))
            pantalla.delete(0, tk.END)
            pantalla.insert(0, resultado)
        except Exception as e:
            pantalla.delete(0, tk.END)
            pantalla.insert(0, "Error")
    else:
        pantalla.insert(tk.END, simbolo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora creada por Gustavo UA")

# Crear la pantalla de la calculadora el bd indica el grosor del borde
pantalla = tk.Entry(ventana, font=("Arial", 16), justify="right", bd=10, bg="lightgrey")
pantalla.grid(row=0, column=0, columnspan=4)

# Definir los botones de la calculadora
#el número entre comillas, donde lo ponemos en la fila 1,2,3,4,5, donde empieza es decir desde
#la posicion 0 de la columna despues la siguuiente columna en la 1 y la siguiente columan en la 2
#finalmente en la columna 3 siendo un total ed 3 columnas 5 filas la reparticion de números.
#el = ocupa desde la columna 0 hasta la 4, ocupando la fila 5 y empezando en la posicion 1.
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0,1, 4)  # El botón '=' ocupa dos columnas
]

# Crear los botones y agregarlos a la ventana
for texto, fila, columna, *args in botones:
    colspan = args[1] if args else 1
    rowspan = args[0] if args else 1
    boton = tk.Button(ventana, text=texto, font=("Arial", 16), padx=20, pady=20,
                     command=lambda t=texto: agregar_simbolo(t))
    boton.grid(row=fila, column=columna, columnspan=colspan, rowspan=rowspan, sticky="nsew")

# Ajustar el tamaño de las filas y columnas
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

#PROGRAMA BÁSICO EN PYTHON EXPLICADO Y CREADO POR GUSTAVOUA.
#ESPERO QUE LES GUSTE.