import json  # Manejo de información
from datetime import datetime  # Para manejar las fechas

# Clase Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False  # Hasta que nosotros no le demos una indicación, debe mantenerse en False (es decir, sin completar)
        
    def marcar_completada(self):
        self.completado = True
        
    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha
    
# Clase Usuario    
class Usuario:
    def __init__(self, nombre_usuario, password):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def eliminar_tarea(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]
        # Recorre toda la lista de tareas hasta llegar a la tarea que tenga el título igual al ingresado

    def obtener_tareas(self):
        return self.tareas
    
# Clase Sistema de Gestión de Tareas
class SistemaGestionTareas:
    # Inicialización del sistema de gestión de un archivo
    def __init__(self, archivo_datos="datos_usuario.json"):
        self.usuarios = {}
        self.archivo_datos = archivo_datos
        self.cargar_datos()
        
    def cargar_datos(self):
        # Cargar datos de los usuarios en JSON 
        try:
            with open(self.archivo_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    # Crea un objeto Usuario para cada usuario en los datos
                    usuario = Usuario(nombre_usuario, info["password"])                
                    for tarea_info in info["tareas"]:
                        # Crea un objeto Tarea para cada tarea del usuario
                        tarea = Tarea(tarea_info["titulo"], tarea_info["descripcion"], tarea_info["fecha_vencimiento"])
                        tarea.completado = tarea_info["completado"]
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError:  # Manejo de excepciones 
            print("Archivo de datos no encontrado, se creará uno nuevo al guardar.")
            
    def guardar_datos(self):
        # Guardar los datos de los usuarios en el archivo
        datos = {}  # Diccionario de datos
        for nombre_usuario, usuario in self.usuarios.items():
            # Organiza las tareas y la información del usuario en un diccionario
            datos[nombre_usuario] = {
                "password": usuario.password,
                "tareas": [
                    {"titulo": tarea.titulo, "descripcion": tarea.descripcion, "fecha_vencimiento": tarea.fecha_vencimiento, "completado": tarea.completado}
                    for tarea in usuario.tareas
                ]
            }
            
        with open(self.archivo_datos, "w") as archivo:
            json.dump(datos, archivo)
    
    def registrar_usuario(self, nombre_usuario, password):
        # Registrar un nuevo usuario si el nombre de usuario no existe
        if nombre_usuario in self.usuarios:
            print("El nombre de usuario ya existe.")
            return False
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, password)
            self.guardar_datos()
            print("Usuario registrado con éxito.")
            return True
        
    def iniciar_sesion(self, nombre_usuario, password):
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.password == password:
            print("Inicio de sesión exitoso.")
            return usuario
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None
        
    def menu_usuario(self, usuario):
        while True:
            print("\n1. Crear Tarea")
            print("2. Ver Tareas")
            print("3. Editar Tarea")
            print("4. Completar Tarea")
            print("5. Eliminar Tarea")
            print("6. Cerrar Sesión")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                titulo = input("Título de la nueva Tarea: ")
                descripcion = input("Ingresa la descripción de la tarea: ")
                fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                tarea = Tarea(titulo, descripcion, fecha_vencimiento)
                usuario.agregar_tarea(tarea)
                self.guardar_datos()
                print("\nTarea creada con éxito.\n")
                
            elif opcion == "2":
                tareas = usuario.obtener_tareas()
                if not tareas:
                    print("No tienes tareas.")
                    continue
                for idx, tarea in enumerate(tareas, start=1):
                    estado = "Completado" if tarea.completado else "Pendiente"
                    print(f"{idx}. {tarea.titulo} - {estado} (Vence: {tarea.fecha_vencimiento})")
            
            elif opcion == "3":
                titulo_tarea = input("Título de la tarea a editar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea:
                    nuevo_titulo = input("Nuevo título: ")
                    nueva_descripcion = input("Nueva descripción: ")
                    nueva_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                    tarea.editar_tarea(nuevo_titulo, nueva_descripcion, nueva_fecha)
                    self.guardar_datos()
                    print("Tarea actualizada con éxito.")
                else:
                    print("Tarea no encontrada.")
                    
            elif opcion == "4":
                # Marcar una tarea como completada
                titulo_tarea = input("Título de la tarea a completar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea: 
                    tarea.marcar_completada()
                    self.guardar_datos()
                    print("Tarea marcada como completada.")
                else: 
                    print("Tarea no encontrada.")
                    
            elif opcion == "5":
                # Eliminar una tarea
                titulo_tarea = input("Título de la tarea a eliminar: ")
                usuario.eliminar_tarea(titulo_tarea)
                self.guardar_datos()
                print("Tarea eliminada con éxito.")
                
            elif opcion == "6":
                # Cerrar sesión
                print("Cerrando sesión.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                
# Ejecución del sistema

if __name__ == "__main__":
    sistema = SistemaGestionTareas()
    while True:
        print("\n ----- Sistema de Gestión de tareas -----")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. salir")
        opcion = input("Selecciona un opción: ")
        
        if opcion == "1":
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese la contraseña: ")
            sistema.registrar_usuario(nombre_usuario, password)
        elif opcion == "2":
            nombre_usuario = input("nombre de usuario: ")
            password = input("Contraseña: ")
            usuario = sistema.iniciar_sesion(nombre_usuario, password)
            if usuario:
                sistema.menu_usuario(usuario)
        
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo")
        