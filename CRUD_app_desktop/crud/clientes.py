import mysql.connector
from conexion import CConexion  # Asegúrate de que la clase CConexion esté correctamente importada

class CClientes:
    
   def mostrarClientes():
    try:
        # Crear una instancia de CConexion
        conexion = CConexion()
        cone = conexion.ConexionBD()  # Llama al método para obtener la conexión
        cursor = cone.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM usuarios;")
        miResultado = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        cone.close()

        return miResultado

    except mysql.connector.Error as error:
        print("Error al mostrar datos: {}".format(error))
        return None 




   @staticmethod
   def ingresarClientes(nombres, apellidos, sexo):
        cursor = None  # Inicializar cursor
        conexion = None  # Inicializar conexión
        
        try:
            cone = CConexion()  # Crear una nueva instancia de CConexion
            conexion = cone.ConexionBD()
            if conexion is None:  # Verifica que la conexión se estableció correctamente
                print("No se pudo establecer la conexion.")
                return False
            
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s)"
            valores = (nombres, apellidos, sexo)
            cursor.execute(sql, valores)
            conexion.commit()  # Confirma los cambios
            print(cursor.rowcount, "Registro ingresado")
            return True  # Indica que la operación fue exitosa

        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))
            return False  # Indica que hubo un error
        
        finally:
            if cursor:
                cursor.close()  # Cierra el cursor
            if conexion:
                conexion.close()  # Cierra la conexión
   @staticmethod
   def modificarClientes(Id, nombres, apellidos, sexo):
        try:
            cone = CConexion()  # Crear una nueva instancia de CConexion
            conexion = cone.ConexionBD()
            if conexion is None:  # Verifica que la conexión se estableció correctamente
                print("No se pudo establecer la conexion.")
                return False
        
            cursor = conexion.cursor()
            sql = "UPDATE usuarios SET nombres=%s, apellidos=%s, sexo=%s WHERE id=%s"
            valores = (nombres, apellidos, sexo, Id)
            cursor.execute(sql, valores)
            conexion.commit()  # Confirma los cambios
            print(cursor.rowcount, "Registro modificado")

            return cursor.rowcount > 0  # Retorna True si se modificó al menos un registro

        except mysql.connector.Error as error:
            print("Error al modificar datos: {}".format(error))
            return False
    
        finally:
            if cursor:
                cursor.close()  # Cierra el cursor
            if conexion:
                conexion.close()  # Cierra la conexión
   @staticmethod
   def eliminarClientes(Id):
        try: 
            cone = CConexion()  # Crear una nueva instancia de CConexion
            conexion = cone.ConexionBD()
            cursor = conexion.cursor()  # Asegúrate de definir el cursor

            # Definir correctamente la tupla 'valores'
            sql = "DELETE FROM usuarios WHERE id = %s"
            valores = (Id,)  # Debe ser una tupla, incluso con un solo valor

            cursor.execute(sql, valores)
            conexion.commit()  # Confirmar la transacción

            print(cursor.rowcount, "Registro eliminado")

        except mysql.connector.Error as error:
            print("Error al eliminar datos: {}".format(error))
            return False

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

        return True