from typing import List, Optional
from src.application.ports.doctor_repository import DoctorRepository
from src.domain.doctor import (Doctor, DoctorCreate, DoctorUpdate)


class DoctorService:
    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    # Caso de uso: Registrar un doctor
    def create_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        if not doctor_data.nombre:
            raise ValueError("El nombre del doctor es obligatorio")

        if not doctor_data.especialidad:
            raise ValueError("La especialidad del doctor es obligatoria")

        return self.repository.save(doctor_data)

    # Caso de uso: Obtener doctor por ID
    def get_doctor(self, doctor_id: int) -> Optional[Doctor]:
        return self.repository.find_by_id(doctor_id)

    # Caso de uso: Listar todos los doctores
    def get_all_doctors(self) -> List[Doctor]:
        return self.repository.find_all()

    # Caso de uso: Actualizar doctor
    def update_doctor(
        self,
        doctor_id: int,
        doctor_update: DoctorUpdate
    ) -> Optional[Doctor]:

        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None

        if doctor_update.nombre is not None and not doctor_update.nombre:
            raise ValueError("El nombre del doctor no puede estar vacío")

        if (
            doctor_update.especialidad is not None
            and not doctor_update.especialidad
        ):
            raise ValueError("La especialidad no puede estar vacía")

        return self.repository.update(doctor_id, doctor_update)

    # Caso de uso: Eliminar doctor
    def delete_doctor(self, doctor_id: int) -> bool:
        return self.repository.delete(doctor_id)