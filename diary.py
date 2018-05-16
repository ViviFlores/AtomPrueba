from peewee import *

db= SqliteDatabase('diary.db')

#metodos para nuestro diario
class Entry(Model):
    #Fecha - timestamp
    #contenido

    class Meta:
        database = db

def add_entry():
    """Agrega un registro"""

def view_entries():
    """Despliega nuestras entradffasffsdfd"""

def delete_entry():
    """Borra un registro"""

def menu_loop():
    """Muestra el menu con las opciones"""

if __name__ == '__main__':
    menu_loop()
