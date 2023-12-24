from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn
from connection import conn

app = FastAPI()


# Define un modelo Pydantic para el cuerpo de la solicitud
class Usuario(BaseModel):
    username: str
    body: str


@app.get('/usuarios')
def obtener_usuarios():
    try:
        # Utiliza la conexión para ejecutar una consulta
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario;")
            usuarios = cursor.fetchall()
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")

       


@app.post('/usuario')
def crear_usuarios(usuario: Usuario):
    try:
        # Utiliza la conexión para ejecutar una consulta
        with conn.cursor() as cursor:

            cursor.execute("insert into usuario (username, body) values (%s, %s);", (usuario.username, usuario.body))
        conn.commit()  
        return {"mensaje": "Usuario creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")





@app.post('/usuario/{id_usuario}')
def actualizar_usuarios(id_usuario: int, usuario: Usuario):
    try:
        # Utiliza la conexión para ejecutar una consulta
        with conn.cursor() as cursor:
            cursor.execute("UPDATE usuario SET username = %s, body = %s WHERE id = %s;", (usuario.username, usuario.body, id_usuario))
        conn.commit()  
        return {"mensaje": "Usuario actualizado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")
    




@app.delete('/usuario/{id_usuario}')
def eliminar_usuario(id_usuario: int):
    try:
        # Utiliza la conexión para ejecutar una consulta
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE id = %s;", (id_usuario,))
        conn.commit()  
        return {"mensaje": "Usuario eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {str(e)}")
