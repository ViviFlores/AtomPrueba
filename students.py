from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username= CharField(max_length=255, unique=True)
    points=IntegerField(default=0)

    class Meta:
        database= db
#Lista con informacion
students=[
    {'username':'Aldo',
     'points':8},
    {'username':'Pedro',
     'points':9},
    {'username':'Panchita',
     'points':5},
    {'username':'Ariel',
     'points':10},
]

#metodo que añade los registros en la base de datos
def add_students():
    for student in students:
        try:
            #crea el nuevo registro
            Student.create(username=student['username'], #student es el registro q estamos recorriendo,username llave del diccionario
                            points=student['points'])
        except IntegrityError: #ese registroya ya existe, en lugar de crear lo va obtener
            #obtener el regstro
            student_record= Student.get(username=student['username'])#get para obtener un unico registro, restriccion->queremos el estudiante cuyo username estamos recorriendo
            #colocamos los puntos al registro obtenido
            student_record.points= student['points']
            student_record.save()#guardar base de datos

#metodo para obtener el mejor estudiante
def top_student():
    student= Student.select().order_by(Student.points.desc()).get() #usamos get porq se encrga de tomar un solo registro
    return student

if __name__=='__main__':
    db.connect()
    db.create_tables([Student],safe=True)
    add_students()
    print('El mejor estudiante es: {}'.format(top_student().username)) #Las llaves (llamados campos de formato), son reemplazadas con los objetos pasados en el método format
    #format-->Los datos que queremos incluir dentro de la cadena se pasan como argumentos a la función format.
