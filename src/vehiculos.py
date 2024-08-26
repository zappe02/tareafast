# vehiculos.py
from pydantic import BaseModel
from fastapi import HTTPException
from typing import List

# Modelo de datos para un vehículo
class Vehiculo(BaseModel):
    id: int
    marca: str
    modelo: str
    anio: int

# Lista para almacenar los vehículos
vehiculos_db = []

# Crear un vehículo
def crear_vehiculo(vehiculo: Vehiculo):
    vehiculos_db.append(vehiculo)
    return vehiculo

# Obtener todos los vehículos
def obtener_vehiculos() -> List[Vehiculo]:
    return vehiculos_db

# Obtener un vehículo por ID
def obtener_vehiculo(vehiculo_id: int) -> Vehiculo:
    for vehiculo in vehiculos_db:
        if vehiculo.id == vehiculo_id:
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")

# Eliminar un vehículo por ID
def eliminar_vehiculo(vehiculo_id: int):
    for vehiculo in vehiculos_db:
        if vehiculo.id == vehiculo_id:
            vehiculos_db.remove(vehiculo)
            return {"detail": "Vehículo eliminado"}
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")
