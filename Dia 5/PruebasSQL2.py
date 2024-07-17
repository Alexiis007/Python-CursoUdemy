import pyodbc

try:
    conn = pyodbc.connect('Driver=SQL Server;Server=ESILENOVO05\\SQLEXPRESS;Database=Pruebas;Trusted_Connection=yes;')
    print("Conexion Existosa")
    cursor = conn.cursor()
    cursor.execute("select @@version")
    row = cursor.fetchone()
    print(row)
except Exception as e:
    print(e)
