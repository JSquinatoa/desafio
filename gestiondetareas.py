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