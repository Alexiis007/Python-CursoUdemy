import pyodbc

try:
    # usamos la conexión
    conn = pyodbc.connect('Driver=SQL Server;Server=ESILENOVO05\\SQLEXPRESS;Database=Pruebas;Trusted_Connection=yes;')
    # creamos un cursor en base a la conexión
    cursor = conn.cursor()
    # Dato para el ejemplo que será mandado como  parámetro
    nombre = 'Pepillo'
    edad = '9999'
    # Ejecucion del sp por medio de su nombre y agregado de los parámetros si es que tiene.
    cursor.execute(f"InsertEmpleado2 {nombre}, {edad}")
    # En este punto el SP se ejecutó y tenemos a nuestra disposicion los datos en el cursor
    cursor.commit()
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f"Error de conexión a la base de datos: {e}")
