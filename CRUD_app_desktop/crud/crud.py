from ast import Delete
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import CConexion  # Asegúrate de que la clase CConexion esté correctamente importada
from clientes import CClientes

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.textBoxId = None
        self.textBoxNombres = None
        self.textBoxApellidos = None
        self.combo = None
        self.groupBox = None
        self.tree = None
        self.Formulario()  # Llamada al método Formulario

    def Formulario(self):  # Asegúrate de que esta línea esté correctamente indentada
        try:
            self.base = Tk()
            self.base.geometry("1200x300")
            self.base.title("Formulario")

            self.groupBox = LabelFrame(self.base, text="Datos del personal", padx=5, pady=5)
            self.groupBox.grid(row=0, column=0, padx=10, pady=10)

            labelId = Label(self.groupBox, text="ID:", width=13, font=("arial")).grid(row=0, column=0)
            self.textBoxId = Entry(self.groupBox)
            self.textBoxId.grid(row=0, column=1)

            labelNombres = Label(self.groupBox, text="Nombres:", width=13, font=("arial")).grid(row=1, column=0)
            self.textBoxNombres = Entry(self.groupBox)
            self.textBoxNombres.grid(row=1, column=1)

            labelApellidos = Label(self.groupBox, text="Apellidos:", width=13, font=("arial")).grid(row=2, column=0)
            self.textBoxApellidos = Entry(self.groupBox)
            self.textBoxApellidos.grid(row=2, column=1)

            labelSexo = Label(self.groupBox, text="Sexo:", width=13, font=("arial")).grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            self.combo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            self.combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(self.groupBox, text="Guardar", width=10, command=self.guardarRegistros).grid(row=4, column=0)
            Button(self.groupBox, text="Actualizar", width=10, command=self.modificarRegistros).grid(row=4, column=1)
            Button(self.groupBox, text="Eliminar", width=10, command = self.eliminarRegistros).grid(row=4, column=2)

            self.groupBox = LabelFrame(self.base, text="Lista del personal", padx=5, pady=5)
            self.groupBox.grid(row=0, column=1, padx=5, pady=5)

            # Crear un treeview
            self.tree = ttk.Treeview(self.groupBox, column=("ID", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            self.tree.column("#1", anchor=CENTER)
            self.tree.heading("#1", text="ID")

            self.tree.column("#2", anchor=CENTER)
            self.tree.heading("#2", text="Nombres")

            self.tree.column("#3", anchor=CENTER)
            self.tree.heading("#3", text="Apellidos")

            self.tree.column("#4", anchor=CENTER)
            self.tree.heading("#4", text="Sexo")
            
            #agregar datos a la tabla 
            for row in CClientes.mostrarClientes():
             self.tree.insert("", "end", values=row)

             #Ejecutar la funcion de hacer click y mostrar el resultado en el Entry
             self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

            self.tree.pack()

            self.base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

    def guardarRegistros(self):
        try:
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get()

            if CClientes.ingresarClientes(nombres, apellidos, sexo):
              messagebox.showinfo("Información", "Los datos fueron guardados")
            else:
                messagebox.showerror("Error", "No se pudieron guardar los datos")
            self.actualizarTreeview()
            
            # Limpiamos los campos
            self.textBoxNombres.delete(0, tk.END)
            self.textBoxApellidos.delete(0, tk.END)

        except ValueError as error:
            print("Error al ingresar los datos: {}".format(error))
    def actualizarTreeview(self):
        try:
            # Borrar todos los elementos actuales del Treeview
            for i in self.tree.get_children():
                self.tree.delete(i)

            # Obtener datos de la base de datos (Asegúrate de que `ingresarClientes` no devuelva nada)
            # Asegúrate de que `CClientes.mostrarClientes()` devuelve una lista de tuplas
            for row in CClientes.mostrarClientes():
                self.tree.insert("", "end", values=row)

        except ValueError as error:
            print("Error al actualizar tabla: {}".format(error))
            
    def seleccionarRegistro(self, event):
       try:
        # Obtener el ID del elemento seleccionado
            itemSeleccionado = self.tree.focus()
            if itemSeleccionado:
                values = self.tree.item(itemSeleccionado)['values']

                self.textBoxId.delete(0, tk.END)
                self.textBoxId.insert(0, values[0])
            
                self.textBoxNombres.delete(0, tk.END)
                self.textBoxNombres.insert(0, values[1])
            
                self.textBoxApellidos.delete(0, tk.END)
                self.textBoxApellidos.insert(0, values[2])
            
                self.combo.set(values[3])
            
       except ValueError as error:
         print("Error al seleccionar registro: {}".format(error))
            
    def modificarRegistros(self):
        try:
            Id = self.textBoxId.get()
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get()

            # Verificar que Id no sea vacío y que sea un número
            if not Id.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número.")
                return
        
            # Asegúrate de que los valores no sean None
            if CClientes.modificarClientes(Id, nombres, apellidos, sexo):
                messagebox.showinfo("Información", "Los datos fueron modificados exitosamente")
            else:
                messagebox.showerror("Error", "No se pudieron modificar los datos")

            self.actualizarTreeview()
        
            # Limpiamos los campos
            self.textBoxId.delete(0, tk.END)
            self.textBoxNombres.delete(0, tk.END)
            self.textBoxApellidos.delete(0, tk.END)

        except Exception as error:  # Usar Exception para atrapar cualquier error
            print("Error al actualizar los datos: {}".format(error))

    def eliminarRegistros(self):
        try:
            # Obtener los valores de los campos de texto
            Id = self.textBoxId.get()
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()

            # Validar si el ID no está vacío
            if not Id:
                messagebox.showerror("Error", "Debes seleccionar un registro para eliminar")
                return

            # Llamar a la función para eliminar el registro
            if CClientes.eliminarClientes(Id):
                messagebox.showinfo("Información", "Los datos fueron eliminados correctamente")
                self.actualizarTreeview()  # Llamar al método de la clase para actualizar el Treeview
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro")

            # Limpiar los campos después de la eliminación
            self.textBoxId.delete(0, tk.END)
            self.textBoxNombres.delete(0, tk.END)
            self.textBoxApellidos.delete(0, tk.END)

        except Exception as error:  # Capturar cualquier excepción
            print("Error al eliminar los datos: {}".format(error))
formulario_clientes = FormularioClientes()