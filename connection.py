import psycopg2
from psycopg2 import sql

# Parámetros de conexión
dbname = 'fastAPI'
user = 'postgres'
password = 'admin7895'
host = 'localhost'  # o la dirección IP de tu servidor PostgreSQL
port = '8086'       # el puerto por defecto de PostgreSQL es 5432


# Establecer la conexión
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Conexión exitosa")

except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)



