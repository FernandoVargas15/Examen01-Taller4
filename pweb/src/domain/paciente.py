from typing import Optional
from pydantic import BaseModel


# Entidad de dominio: Paciente
class Paciente(BaseModel):
    id: str
    nombre: str
    email: str


# DTO para la creación de pacientes
class PacienteCreate(BaseModel):
    nombre: str
    email: str


# DTO para la actualización de pacientes
class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
