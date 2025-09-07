from dataclasses import field

from pydantic import BaseModel, EmailStr, Field

class Disco:
    codigo: str = Field(..., min_length=8, max_length=8, description="Codigo ded identificacion unica de la entidad ")
    nome: str = Field(...,min_length=8, max_length=64, description="Titulo o nombre de la pelicula")
    sinopsis: str= Field(...,min_length=16, max_length= 256, description="Sinopsis de la pelicula")
    director: str = Field(...,min_length=4, max_length=64, description="Nombre del director de la pelicula")
    duracion: int = Field(...,ge=1, le=2, description="Tiempo de duracion de la pelicula")
    tamanio: int= Field(...,ge=1, le=5, description="Tamaño de la pelicula en GB")
    precio_venta: int = Field(...,ge=100, le= 500, description="Precio en que se vende el disco digital")
    precio_rentta : int = Field(...,ge=50, le=70, description = "Precio en que se renta el disco digital")

    #Ejemplo que se debe mostrar en la documentacion de la API
    model_config ={
        "json_Scheme_extra":{
            "example":{
            "codigo": "cod-100",
            "nome": "Lilo & Stitch",
            "sinopsis": "En el vibrante y paradisíaco archipiélago de Hawái, donde la brisa salada se mezcla con el ritmo del ukulele,"
                        " conocemos a Lilo, una niña tan imaginativa como solitaria. Marcada por la ausencia de sus padres, "
                        "Lilo navega por la vida bajo la atenta pero a veces desbordada mirada de su hermana mayor, Nani. "
                        "Su mundo da un svuelco cósmico cuando adopta a un «perro» callejero inusual, un encuentro que cambiará sus vidas "
                        "para siempre.",
            "director": "Dean Fleischer Camp",
            "tamanio": 3,
            "precio_venta": 400,
            "precio_renta":70,
            "codigo":"cod-100",
            }



        }
    }

class Usuario:
    Nombre: str = Field(..., min_length=8, max_length=64, description="Nombre completo del usuario")
    Apellido: str = Field(..., min_length=8, max_length=64, description="Apellido del usuario")
    correo: str = Field(..., min_length=8, max_length=64, description="Correo del usuario")
    contrasenia: str = Field(...,min_length=8, max_length=64, description="Contraseña del usuario")