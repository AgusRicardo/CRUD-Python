import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image, ImageTk

# Importa la clase Alumnos
from alumnos import Alumnos

class AplicacionCRUD:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Alumnos")
        self.ventana.iconbitmap("img/student.ico")
        self.ventana.configure(bg="lightblue")

        self.modo_oscuro = False  # Bandera para rastrear el modo claro/oscuro
        # Cargar la imagen para el botón de modo oscuro
        self.imagen_modo_oscuro = Image.open("img/modo-oscuro.png")  # Reemplaza "modo_oscuro.png" con la ruta de tu imagen
        self.imagen_redimensionada = self.imagen_modo_oscuro.resize((22, 22))
        self.imagen_modo_oscuro = ImageTk.PhotoImage(self.imagen_redimensionada)

        # Crear un botón para cambiar entre modos claro y oscuro
        self.boton_modo_oscuro = ttk.Button(ventana, image=self.imagen_modo_oscuro, command=self.cambiar_modo)
        self.boton_modo_oscuro.pack()
		
		# Carga la imagen del logo
        self.logo = Image.open("img/logo1.png")
        fondo = Image.new("RGBA", self.logo.size, (255, 255, 255, 0))
        fondo.paste(self.logo, (0, 0), self.logo)
        self.logo = ImageTk.PhotoImage(fondo)

        # Crea una etiqueta con el logo y establece el fondo como transparente
        self.label_logo = tk.Label(ventana, image=self.logo, bg="lightblue")
        self.label_logo.pack()

        # Crea un nuevo estilo y configura el color de fondo
        estilo = ttk.Style()
        estilo.configure("Label.TLabel", background="lightblue", foreground="black", font=("Arial", 11))
        estilo.configure('Fondo.TFrame', background='lightblue')
        estilo.configure("TButton",
        background="green",
        foreground="green",
        font=("Arial", 12),
        borderwidth=2,
        relief="flat",
        cursor="hand2",
    )

        # Crea el marco y asigna el estilo personalizado
        self.marco_alta = ttk.Frame(ventana, style='Fondo.TFrame')

        # Crear un objeto Menú
        self.barra_menu = tk.Menu(ventana)
        ventana.config(menu=self.barra_menu)

        # Crear un menú "Alumnos" en la barra de menú
        menu_alumnos = tk.Menu(self.barra_menu, tearoff=0)
        menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Menú", menu=menu_alumnos)
        self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Agregar opciones al menú "Alumnos"
        menu_alumnos.add_command(label="Cargar alumno", command=self.mostrar_formulario_alta)
        menu_alumnos.add_command(label="Modificar alumno", command=self.mostrar_formulario_modificar)
        menu_alumnos.add_command(label="Listado alumnos", command=self.mostrar_listado_alumnos)
        menu_alumnos.add_command(label="Eliminar alumno", command=self.mostrar_formulario_eliminar)
        menu_ayuda.add_command(label="Instrucciones", command=self.mostrar_ayuda)

        # Crea una instancia de la clase Alumnos
        self.alumno1 = Alumnos()


    def cambiar_modo(self):
        # Cambiar entre modo claro y oscuro
        if self.modo_oscuro:
            self.ventana.configure(bg="lightblue")
            self.label_logo.configure(bg="lightblue")
            estilo = ttk.Style()
            estilo.configure('Fondo.TFrame', background='lightblue')
            estilo.configure("Label.TLabel", background="lightblue", foreground="black", font=("Arial", 11))

            #Cambiar imagen
            self.imagen_modo_oscuro = Image.open("img/modo-oscuro.png") 
            self.imagen_redimensionada = self.imagen_modo_oscuro.resize((22, 22))
            self.imagen_modo_oscuro = ImageTk.PhotoImage(self.imagen_redimensionada)
            self.boton_modo_oscuro["image"] = self.imagen_modo_oscuro
        else:
            self.ventana.configure(bg="#313d47")
            self.label_logo.configure(bg="#313d47")
            estilo = ttk.Style()
            estilo.configure('Fondo.TFrame', background='#313d47')
            estilo.configure("Label.TLabel", background="#313d47", foreground="white", font=("Arial", 11))
            #Cambiar imagen
            self.imagen_modo_claro = Image.open("img/modo-claro.png") 
            self.imagen_redimensionada = self.imagen_modo_claro.resize((22, 22))
            self.imagen_modo_claro = ImageTk.PhotoImage(self.imagen_redimensionada)
            self.boton_modo_oscuro["image"] = self.imagen_modo_claro


        self.modo_oscuro = not self.modo_oscuro

    def mostrar_ayuda(self):
        # Limpia el marco actual
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        instrucciones = """
        ▶ Alta alumno:
            1- Presionar del menú desplegable la opción "Cargar Alumno"
            2- Completar los campos Nombre, Fecha de Nacimiento y Dirección
            3- Presionar el botón [Confirmar]
            4- Se visualiza un cartel en modo de confirmación indicando que los datos fueron cargados

        ▶ Consulta por legajo:
            1- Presionar del menú desplegable la opción "Consulta por legajo"
            2- Completar el campo legajo
            3- Presionar el botón [Consultar]
            4- Se visualiza como se autocompletan todos los campos con la información del alumno

        ▶ Listado de alumnos:
            1- Presionar del menú desplegable la opción "Listado de alumnos"
            2- Presionar el botón [Listado alumnos]
            3- Se visualiza un listado de los alumnos con sus respectivos datos

        ▶ Eliminar alumno:
            1- Presionar del menú desplegable la opción "Eliminar alumno"
            2- Completar el campo legajo
            3- Presionar el botón [Borrar]
            4- Se visualiza un cartel en modo de confirmación indicando que se eliminó el alumno

        ▶ Modificar alumno:
            1- Presionar del menú desplegable la opción "Modificar alumno"
            2- Completar el campo legajo
            3- Presionar el botón [Consultar]
            4- Se visualiza como se autocompletan todos los campos con la información del alumno
            5- Modificar uno o mas campos
            6- Presionar el botón [Modificar]
            7- Se visualiza un cartel en modo de confirmación indicando que se modificó el alumno
        """

        etiqueta_instrucciones = ttk.Label(self.marco_alta, text=instrucciones, wraplength=700, justify="left", style="Label.TLabel")
        etiqueta_instrucciones.grid(row=0, column=0, padx=20, pady=5)

        # Asegura que se vean los cambios en la ventana
        self.marco_alta.pack()


    def mostrar_formulario_alta(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada para el formulario de alta
        label_nombre = ttk.Label(self.marco_alta, text="Nombre:", style="Label.TLabel")
        label_fecha = ttk.Label(self.marco_alta, text="Fecha de Nacimiento:", style="Label.TLabel")
        label_direccion = ttk.Label(self.marco_alta, text="Dirección:", style="Label.TLabel")

        entry_nombre = ttk.Entry(self.marco_alta)
        entry_fecha = DateEntry(self.marco_alta, date_pattern="dd/mm/yyyy", maxdate=datetime.today().date())
        entry_direccion = ttk.Entry(self.marco_alta)

        label_nombre.grid(row=0, column=0, padx=5, pady=5)
        label_fecha.grid(row=1, column=0, padx=5, pady=5)
        label_direccion.grid(row=2, column=0, padx=5, pady=5)

        entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        entry_fecha.grid(row=1, column=1, padx=5, pady=5)
        entry_direccion.grid(row=2, column=1, padx=5, pady=5)

        # Botón para guardar el alumno
        boton_guardar = ttk.Button(self.marco_alta, text="Guardar",command=lambda: self.guardar_alumno(entry_nombre.get(), entry_fecha.get(), entry_direccion.get()))
        boton_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        entry_nombre.delete(0, 'end')
        entry_fecha.delete(0, 'end')
        entry_direccion.delete(0, 'end')
        # Agregar el marco a la ventana principal
        self.marco_alta.pack()

    def guardar_alumno(self, nombre, fecha, direccion):
        # Lógica para guardar un nuevo alumno
        if nombre and fecha and direccion:
            datos = (nombre, fecha, direccion)
            resultado = self.alumno1.alta(datos)
            mb.showinfo(title= "Confirmación", message=f"Se ha dado de alta al alumno/a: {nombre}")

            # Actualizar la lista de alumnos si es necesario
            self.actualizar_tabla()
        else:
            mb.showerror("Error", "Por favor, complete todos los campos.")

    def actualizar_tabla(self):
        # Obtener todos los registros de la base de datos
        registros = self.alumno1.recuperar_todos()

        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los nuevos registros en la tabla en el orden correcto
        for alumno in registros:
            self.tree.insert("", 0, values=(alumno[0], alumno[1], alumno[2], alumno[3]))


    def mostrar_formulario_modificar(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        label_legajo = ttk.Label(self.marco_alta, text="Legajo del alumno:", style="Label.TLabel")
        entry_legajo = ttk.Entry(self.marco_alta)
        label_legajo.grid(row=0, column=0, padx=5, pady=5)
        entry_legajo.grid(row=0, column=1, padx=5, pady=5)

        def cargar_datos():
            legajo = entry_legajo.get()
            datos_alumno = self.alumno1.consulta((legajo,))
            if datos_alumno:
                # Mostrar los datos del alumno en el formulario de modificación
                nombre, fecha_nacimiento, direccion = datos_alumno[0]

                label_nombre = ttk.Label(self.marco_alta, text="Nombre:", style="Label.TLabel")
                entry_nombre = ttk.Entry(self.marco_alta)
                label_fecha = ttk.Label(self.marco_alta, text="Fecha de Nacimiento:", style="Label.TLabel")
                entry_fecha = ttk.Entry(self.marco_alta)
                label_direccion = ttk.Label(self.marco_alta, text="Dirección:", style="Label.TLabel")
                entry_direccion = ttk.Entry(self.marco_alta)

                label_nombre.grid(row=1, column=0, padx=5, pady=5)
                entry_nombre.grid(row=1, column=1, padx=5, pady=5)
                label_fecha.grid(row=2, column=0, padx=5, pady=5)
                entry_fecha.grid(row=2, column=1, padx=5, pady=5)
                label_direccion.grid(row=3, column=0, padx=5, pady=5)
                entry_direccion.grid(row=3, column=1, padx=5, pady=5)

                entry_nombre.insert(0, nombre)
                entry_fecha.insert(0, fecha_nacimiento)
                entry_direccion.insert(0, direccion)

                # Botón para guardar los cambios
                def guardar_cambios():
                    nombre = entry_nombre.get()
                    fecha_nacimiento = entry_fecha.get()
                    direccion = entry_direccion.get()

                    if nombre and fecha_nacimiento and direccion:
                        datos_modificados = (nombre, fecha_nacimiento, direccion, legajo)
                        resultado = self.alumno1.modificacion(datos_modificados)
                        mb.showinfo(title= "Confirmación", message=f"Se ha actualizado la información del alumno/a: {nombre}")

                        # Actualizar la tabla
                        self.actualizar_tabla()
                        self.marco_alta.destroy()
                    else:
                        mb.showerror("Error", "Por favor, complete todos los campos.")

                boton_guardar = ttk.Button(self.marco_alta, text="Guardar Cambios", command=guardar_cambios)
                boton_guardar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
            else:
                mb.showerror("Error", "No se encontró al alumno con el legajo proporcionado.")

        boton_buscar = ttk.Button(self.marco_alta, text="Buscar Alumno", command=cargar_datos)
        boton_buscar.grid(row=0, column=2, padx=5, pady=5)

        self.marco_alta.pack()

    def mostrar_formulario_eliminar(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        label_legajo = ttk.Label(self.marco_alta, text="Legajo del alumno:", style="Label.TLabel")
        entry_legajo = ttk.Entry(self.marco_alta)
        label_legajo.grid(row=0, column=0, padx=5, pady=5)
        entry_legajo.grid(row=0, column=1, padx=5, pady=5)

        def eliminar_alumno():
            legajo = entry_legajo.get()
            if legajo:
                resultado = self.alumno1.baja((legajo,))
                if resultado > 0:
                    mb.showinfo("Resultado", f"Alumno con legajo {legajo} ha sido eliminado exitosamente.")
                    # Actualizar la tabla
                    self.actualizar_tabla()
                    self.marco_alta.destroy()
                else:
                    mb.showerror("Error", "No se encontró al alumno con el legajo proporcionado.")
            else:
                mb.showerror("Error", "Por favor, ingrese el legajo del alumno a eliminar.")

        boton_eliminar = ttk.Button(self.marco_alta, text="Eliminar Alumno", command=eliminar_alumno)
        boton_eliminar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.marco_alta.pack()

    def mostrar_listado_alumnos(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        # Crear una tabla para mostrar los alumnos
        self.tree = ttk.Treeview(self.marco_alta, columns=("#","Legajo", "Nombre", "Fecha Nacimiento", "Dirección"))

        # Definir las columnas
        columnas = [
            ("#", 40),
            ("Legajo", 80),
            ("Nombre", 200),
            ("Fecha Nacimiento", 200),
            ("Dirección", 200)
        ]

        for i, (col_name, col_width) in enumerate(columnas):
            self.tree.heading("#{}".format(columnas.index((col_name, col_width))), text=col_name, anchor="center")
            self.tree.column("#{}".format(columnas.index((col_name, col_width))), width=col_width, anchor="center")

        self.tree.grid(row=0, column=0, padx=5, pady=5)

        # Invocar el método para actualizar la tabla
        self.actualizar_tabla()

        self.marco_alta.pack()



if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionCRUD(ventana)
    ventana.mainloop()
