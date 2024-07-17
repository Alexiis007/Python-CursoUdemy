import pyodbc


conn = pyodbc.connect('Driver=SQL Server;Server=ESILENOVO05\\SQLEXPRESS;Database=Pruebas;Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("INSERT INTO EMPLEADOS VALUES('HolaMundoPhyton',20,2,100,999)")
cursor.commit()
cursor.close()
conn.close()
