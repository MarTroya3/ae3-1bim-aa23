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
nombreequipo = "Barcelona"
clasificacion = "A"
numerojugadores = 30
cadena_sql = """INSERT INTO Equipo (nombreequipo, clasificacion, numerojugadores) \
VALUES ('%s', '%s', %d);""" % (nombreequipo, clasificacion, numerojugadores)

# ejecutar el SQL
cursor.execute(cadena_sql)
nombreequipo = "Liga de Quito"
clasificacion = "A"
numerojugadores = 40
cadena_sql = """INSERT INTO Equipo (nombreequipo, clasificacion, numerojugadores) \
VALUES ('%s', '%s', %d);""" % (nombreequipo, clasificacion, numerojugadores)

# ejecutar el SQL
cursor.execute(cadena_sql)
nombreequipo = "Nacional"
clasificacion = "A"
numerojugadores = 35
cadena_sql = """INSERT INTO Equipo (nombreequipo, clasificacion, numerojugadores) \
VALUES ('%s', '%s', %d);""" % (nombreequipo, clasificacion, numerojugadores)

# ejecutar el SQL
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s  - %d" % (d[0], d[1], d[2]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
