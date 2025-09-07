# API REST para Tienda Virtual de Videos (Venta-Alquiler)

Este proyecto implementa una API REST para una tienda virtual de videos (venta-alquiler), construida con lenguaje Python y el framework FastAPI.  
El objetivo es gestionar un catálogo de discos (películas o videos digitales) junto con las operaciones de registro de usuarios, ventas y alquileres.

## Estructura del proyecto

- **main.py**: Punto de entrada de la aplicación de la API FastAPI

**entidades/**: Directorio de paquetes que contiene todas las clases
```
entidades/
├── __init__.py
├── disco.py
├── venta.py
├── alquiler.py
├── catalogo.py
```

## Instalación y ejecución

1. Clonar el repositorio  
   ```bash
   git clone https://github.com/Flores890/test-alquiler-video.git
   ```
2. Entrar al directorio  
   ```bash
   cd test-alquiler-video
   ```
3. Crear y activar entorno virtual (opcional, recomendado)  
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```
4. Instalar dependencias  
   ```bash
   pip install fastapi uvicorn pydantic
   ```
5. Ejecutar el servidor  
   ```bash
   uvicorn main:app --reload
   ```
6. Acceder a la API  
   - Documentación interactiva (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentación alternativa (ReDoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints principales (versión inicial)

| Método | Endpoint            | Descripción                          |
|--------|---------------------|--------------------------------------|
| GET    | /discos/            | Lista los discos disponibles         |
| POST   | /discos/            | Agregar un nuevo disco               |
| PUT    | /discos/{id}        | Actualizar información de un disco   |
| DELETE | /discos/{id}        | Eliminar un disco                    |
| POST   | /usuarios/          | Registro de nuevo usuario            |
| POST   | /ventas/            | Registrar ventas                     |
| POST   | /alquileres/        | Registrar alquiler                   |

## Tecnologías utilizadas

- Python 3.12.8
- FastAPI
- Uvicorn (Servidor ASGI)

## Proyecto desarrollado como caso de estudio

**Nombre:** Katerin Flores B.  
**Email:** <fkaterin78@gmail.com>  
**GitHub:** [Flores890](https://github.com/Flores890)
