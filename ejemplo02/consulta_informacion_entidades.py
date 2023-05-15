"""
    Consulta información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad
nombre = "Glenn"
apellido = "Troya"
cedula = "0504070491"
edad = 19
cadena_sql = """INSERT INTO Jugador (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)
nombre = "Camilo"
apellido = "Hidalgo"
cedula = "0584078491"
edad = 20
cadena_sql = """INSERT INTO Jugador (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)
nombre = "Luis"
apellido = "Chávez"
cedula = "1704070491"
edad = 25
cadena_sql = """INSERT INTO Jugador (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)
# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Jugador"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
