from dataclasses import field

from pydantic import BaseModel, EmailStr, Field

class Usuario:
    Nombre: str = Field(..., min_length=8, max_length=64, description="Nombre completo del usuario")
    Apellido: str = Field(..., min_length=8, max_length=64, description="Apellido del usuario")
    correo: str = Field(..., min_length=8, max_length=64, description="Correo del usuario")

    contrasenia: str = Field(...,min_length=8, max_length=64, description="Contraseña del usuario")
