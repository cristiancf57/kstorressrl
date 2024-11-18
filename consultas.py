import mysql.connector

def profesiones():
    conexion = mysql.connector.connect(
    host="localhost",  
    user="root", 
    password="root", 
    database="kstorres_db" 
    )

    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM profesiones')
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def cargos():
    conexion = mysql.connector.connect(
    host="localhost",  
    user="root", 
    password="root", 
    database="kstorres_db" 
    )
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM roles')
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

