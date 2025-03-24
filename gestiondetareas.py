import json # manejo de información
from datetime import datetime # para poder las fechas

# clase tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False # Hasta que nostros no le demos una indicación debe mantenerse en false es decir sin completar
        
    def marcar_completada(self):
        self.completado = True
        
    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha
    
# clase usuario    
class Usuario:
    def __init__(self, nombre_usuario, password):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tarea.append(tarea)
        
    def eliminar_tarea(self, titulo_tarea):
        self.tarea = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]
        #recorre toda la lista de tareas hgata llegar a la tarea que tenga el titulo igual al ingresado

    def obtener_tareas(self):
        return self.tareas
    
    
    
    