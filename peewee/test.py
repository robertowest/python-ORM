import peewee
import datetime

database = peewee.MySQLDatabase("lubresrl", host="192.168.1.2", user="roberto", password="roberto")

class Usuario(peewee.Model):
    usuario = peewee.CharField( unique=True )
    email = peewee.CharField( index=True )
    fecha_creacion = peewee.CharField( default=datetime.datetime.now)
    class Meta:
        database = database     # instanciada en la primera linea
        db_table = 'Usuarios'

if __name__ == '__main__':
    if not Usuario.table_exists():
        Usuario.create_table()

    username = input("Ingrese un nombre : ")
    if not Usuario.select().where( Usuario.usuario == username ).exists():
        email = input("Ingrese un correo electrónico : ")
        new_user = Usuario.create(usuario=username, email=email)
        new_user.save()
    else:
        print( "Ya existe el usuario : ", username )
