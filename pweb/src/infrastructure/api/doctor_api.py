from typing import List
from fastapi import FastAPI, HTTPException
from src.application.services.doctor_service import DoctorService
from src.infrastructure.adapters.memory_doctor_repository import (MemoryDoctorRepository)
from src.domain.doctor import (Doctor, DoctorCreate, DoctorUpdate)

app = FastAPI(title="Microservicio de Doctores")

# Inyección de dependencias
doctor_repository = MemoryDoctorRepository()
doctor_service = DoctorService(doctor_repository)

# Crear doctor
@app.post("/doctores", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    try:
        return doctor_service.create_doctor(doctor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Obtener todos los doctores
@app.get("/doctores", response_model=List[Doctor])
def get_doctores():
    return doctor_service.get_all_doctors()

# Obtener doctor por ID
@app.get("/doctores/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    doctor = doctor_service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor

# Eliminar doctor
@app.delete("/doctores/{doctor_id}")
def delete_doctor(doctor_id: int):
    if not doctor_service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return {"mensaje": "Doctor eliminado correctamente"}
