import mysql.connector
import tkinter as tk

def iniciar_sesion():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="nombre_de_la_base_de_datos"
    )

    mycursor = mydb.cursor()

    username = usuario.get()
    password = contrasena.get()

    sql = "SELECT * FROM tabla_de_usuarios WHERE username = %s AND password = %s"
    val = (username, password)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    if len(myresult) > 0:
        resultado.config(text="Inicio de sesión exitoso")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Login")

# Crear los campos de entrada y el botón
tk.Label(ventana, text="Nombre de usuario").grid(row=0)
usuario = tk.Entry(ventana)
usuario.grid(row=0, column=1)
tk.Label(ventana, text="Contraseña").grid(row=1)
contrasena = tk.Entry(ventana, show="*")
contrasena.grid(row=1, column=1)
tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion).grid(row=2, column=1)

# Crear la etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.grid(row=3)

# Mostrar la ventana
ventana.mainloop()
