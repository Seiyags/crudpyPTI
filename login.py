from conexion import *
import tkinter as it
from tkinter import messagebox

curso = conn.cursor()

ventana = tk.Tk()
ventana.title("CRUD PYTHON")
ventana.geometry("640x480")


lblNombre = tk.Label(text="Nombre: ")
lblNombre =grid(row=0, column=0)

lblUsario = tk.Label("Usuaario")
lblUsuario.grid(row=1,column=0)
entryUsuario = tk.Entry()
entryUsuario.grid(row=1,column=1)

lblPassword = tk.Label(text="Password: ")
lblPassword.grid(row=2, column=1)

entryPassword = tk.Entry(show'*')
entryPassword.grid(row=2, column=1)


def registrar():
    try:
        usuario=entryUsuario.get()
        nombre=entryNombre.get()
        clave=entryPassword.get()
        sql= "INSERT INTO user(name,username, password) VALUES(%s,%s,%s)"
        cursor.execute(sql,(nombre,usuario,clave))
        messagebox.showinfo("Alto de usuario", "registro exitosa")

        conn.commit()
        conn.close()
    except:
        messagebox.showerror("Error al conectar a la base de datos")

btnLogin = tk.Button(text="Log in", command=registrar)
btnLongin.grid(row=3, column=2)



ventana.mainloop()