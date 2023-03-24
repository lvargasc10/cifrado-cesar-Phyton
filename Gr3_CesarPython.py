'''
Programa Criptografia Cifrado Cesar
Luisa Mabel Vargas Cardenas
2022-2
'''

# ----------Importacion librerias-------------
from tkinter import *
from tkinter import ttk

# ----------------Funciones-------------
def cifradoCesar(mensaje, clave):

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje.strip()
    resultado = ""

    for caracter in mensaje:

        if caracter in alfabeto:
            posicion = alfabeto.find(caracter)
            nuevaPos = (posicion + clave) % 26
            nuevoCar = alfabeto[nuevaPos]
            resultado += nuevoCar
        else:
            resultado += caracter

    return str(resultado)

def descifradoCesar(mensaje, clave):

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje.strip()
    resultado = ""

    for caracter in mensaje:

        if caracter in alfabeto:
            posicion = alfabeto.find(caracter)
            nuevaPos = (posicion - clave) % 26
            nuevoCar = alfabeto[nuevaPos]
            resultado += nuevoCar
        else:
            resultado += caracter

    return str(resultado)

def funcionEncriptarBtn():

    texto = txtInputEncriptar.get(1.0, "end-1c")
    #clave = int(cmbClave.get(1.0, "end-1c"))
    clave = cmbClave.current()+1
    cifradoCesar(texto, clave)
    lblResultadoEncriptado.config(text=cifradoCesar(texto, clave))
    resultado = lblResultadoEncriptado.cget("text")
    txtInputDesencriptar.delete('1.0', END)
    txtInputDesencriptar.insert(INSERT, resultado)

def funcionDesencriptarBtn():
    texto = txtInputDesencriptar.get(1.0, "end-1c")
    #clave = int(cmbClave.get(1.0, "end-1c"))
    clave = cmbClave.current()+1
    descifradoCesar(texto, clave)
    lblResultadoDesencriptado.config(text=descifradoCesar(texto, clave))

# -------------------------------------------INTERFAZ--------------------------------------------------------
# Configuracion ventana tkinter GUI
ventana = Tk()
ventana.title('Grupo 3 Ciberseguridad Cifrado Cesar')
ventana.resizable(False, False)
ventana.geometry('460x450')

# ------------Creacion Labels,Botones,Texto,Combo
# Label
lblInputTitulo = Label(text="Ingreso text", fg='black',
                       font=("Consolas 12 bold"))
lblResultadoTitulo = Label(
    text="Resultado", fg='black', font=("Consolas 12 bold"))
lblClaveTitulo = Label(text="Clave", fg='black', font=("Consolas 12 bold"))

lblResultadoEncriptado = Label(ventana, text=" ", bd=5, relief="sunken",
                               font="Consolas 10", width=25, height=5, bg="light pink")
lblResultadoDesencriptado = Label(
    ventana, text=" ", bd=5, relief="sunken", font="Consolas 10", width=25, height=5, bg="light green")

# Text
#cmbClave = Text(ventana, width=10 , height=1, bg = "white")
txtInputEncriptar = Text(ventana, width=20, height=5, bg="light pink")
txtInputDesencriptar = Text(ventana, width=20, height=5, bg="light green")

# Combo
cmbClave = ttk.Combobox(
    ventana, width=10, textvariable=IntVar(), state="readonly")
cmbClave['values'] = list(range(1, 21))
cmbClave.current(0)

# Boton
btnCifrar = Button(ventana, text="Cifrar", fg="black", font=("Consolas", 11),
                   command=funcionEncriptarBtn, activeforeground="red", activebackground="pink", bg='pink')
btnDescifrar = Button(ventana, text="Descifrar", fg="black", font=(
    "Consolas", 11), command=funcionDesencriptarBtn, activeforeground="green", activebackground="lime", bg='light green')

# -------------------Ajuste Label-Texto
lblResultadoEncriptado.bind('<Configure>', lambda e: lblResultadoEncriptado.config(
    wraplength=lblResultadoEncriptado.winfo_width()))
lblResultadoDesencriptado.bind('<Configure>', lambda e: lblResultadoDesencriptado.config(
    wraplength=lblResultadoDesencriptado.winfo_width()))

# -------------------Ubicacion en el Grid.
# Label
lblInputTitulo.grid(row=1, column=0, padx=30, pady=10)
lblResultadoTitulo.grid(row=1, column=1, padx=30, pady=10)
lblClaveTitulo.grid(row=0, column=0, padx=100, pady=20)

lblResultadoEncriptado.grid(row=2, column=1)
lblResultadoDesencriptado.grid(row=4, column=1)

# Text
txtInputEncriptar.grid(row=2, column=0)
txtInputDesencriptar.grid(row=4, column=0)

# Combo
cmbClave.grid(row=0, column=1, padx=30, pady=10)

# Boton
btnCifrar.grid(row=3, column=0, padx=20, pady=20)
btnDescifrar.grid(row=5, column=0, padx=20, pady=20)

ventana.mainloop()
