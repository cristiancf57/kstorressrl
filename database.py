import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="root",
    database="kstorres_db" 
)

cursor = conexion.cursor()

print('\nPROFESIONES')

cursor.execute('SELECT * FROM profesiones')
resultados = cursor.fetchall()
for row in resultados:
    print(row)

conexion.close()