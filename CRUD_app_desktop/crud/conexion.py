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

# Llamar al m�todo ConexionBD y guardar la conexi�n
conexion = conexion_instance.ConexionBD()

# Aseg�rate de cerrar la conexi�n despu�s de usarla
if conexion:
    # Aqu� puedes realizar operaciones en la base de datos

    # Cerrar la conexi�n
    conexion.close()