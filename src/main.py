import os
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.database import engine
from src.models import BaseModel
from .vehiculos import Vehiculo, crear_vehiculo, obtener_vehiculos, obtener_vehiculo, eliminar_vehiculo
from typing import List
from fastapi.middleware.cors import CORSMiddleware
# importamos los routers desde nuestros modulos
from src.example.router import router as example_router

load_dotenv()

ENV = os.getenv("ENV")
ROOT_PATH = os.getenv(f"ROOT_PATH_{ENV.upper()}")


@asynccontextmanager
async def db_creation_lifespan(app: FastAPI):
    BaseModel.metadata.create_all(bind=engine)
    yield





app = FastAPI(root_path=ROOT_PATH, lifespan=db_creation_lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O agrega ["*"] para permitir todas las solicitudes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/vehiculos/", response_model=Vehiculo)
def crear_vehiculo_endpoint(vehiculo: Vehiculo):
    return crear_vehiculo(vehiculo)

@app.get("/vehiculos/", response_model=List[Vehiculo])
def obtener_vehiculos_endpoint():
    return obtener_vehiculos()

@app.get("/vehiculos/{vehiculo_id}", response_model=Vehiculo)
def obtener_vehiculo_endpoint(vehiculo_id: int):
    return obtener_vehiculo(vehiculo_id)

@app.delete("/vehiculos/{vehiculo_id}")
def eliminar_vehiculo_endpoint(vehiculo_id: int):
    return eliminar_vehiculo(vehiculo_id)

# asociamos los routers a nuestra app
app.include_router(example_router)
