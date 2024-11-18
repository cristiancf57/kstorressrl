import mysql.connector

def nuevo_save(nuevo):
    conexion = mysql.connector.connect(
    host="localhost",  
    user="root", 
    password="root", 
    database="kstorres_db" 
    )
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO producto (descripcion,cantidad,precio) VALUES (?,?,?)',nuevo)
    conexion.commit()
    conexion.close()
