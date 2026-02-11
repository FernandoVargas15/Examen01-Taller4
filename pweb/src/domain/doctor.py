from typing import Optional
from pydantic import BaseModel

class Doctor(BaseModel):
    id: int
    nombre: str
    especialidad: str

class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str

class DoctorUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None
