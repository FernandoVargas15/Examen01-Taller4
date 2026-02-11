from typing import List
from fastapi import FastAPI, HTTPException
from src.application.services.paciente_service import PacienteService
from src.infrastructure.adapters.memory_paciente_repository import (MemoryPacienteRepository)
from src.domain.paciente import (Paciente, PacienteCreate,PacienteUpdate)

app = FastAPI(title="Microservicio de Pacientes")

# Inyección de dependencias
paciente_repository = MemoryPacienteRepository()
paciente_service = PacienteService(paciente_repository)


# Crear paciente
@app.post("/pacientes", response_model=Paciente)
def create_paciente(paciente: PacienteCreate):
    try:
        return paciente_service.register_paciente(paciente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Obtener todos los pacientes
@app.get("/pacientes", response_model=List[Paciente])
def get_pacientes():
    return paciente_service.get_all_pacientes()


# Obtener paciente por ID
@app.get("/pacientes/{paciente_id}", response_model=Paciente)
def get_paciente(paciente_id: str):
    paciente = paciente_service.get_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente


# Eliminar paciente
@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: str):
    if not paciente_service.delete_paciente(paciente_id):
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado"
        )
    return {"mensaje": "Paciente eliminado correctamente"}
