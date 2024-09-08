import mysql.connector

class CConexion:
    def ConexionBD(self):
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='clientesdb',
                port='3306'
            )
           
            return conexion

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
            return None  # Retornar None si hay un error

# Crear una instancia de la clase
conexion_instance = CConexion()

# Llamar al método ConexionBD y guardar la conexión
conexion = conexion_instance.ConexionBD()

# Asegúrate de cerrar la conexión después de usarla
if conexion:
    # Aquí puedes realizar operaciones en la base de datos

    # Cerrar la conexión
    conexion.close()