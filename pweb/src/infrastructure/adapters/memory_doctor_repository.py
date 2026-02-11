from typing import List, Optional
from src.application.ports.doctor_repository import DoctorRepository
from src.domain.doctor import (Doctor, DoctorCreate, DoctorUpdate)

class MemoryDoctorRepository(DoctorRepository):

    def __init__(self):
        self.doctores: dict[int, Doctor] = {}
        self.current_id: int = 1

    def save(self, doctor: DoctorCreate) -> Doctor:
        new_doctor = Doctor(
            id=self.current_id,
            nombre=doctor.nombre,
            especialidad=doctor.especialidad
        )

        self.doctores[self.current_id] = new_doctor
        self.current_id += 1
        return new_doctor

    def find_by_id(self, doctor_id: int) -> Optional[Doctor]:
        return self.doctores.get(doctor_id)

    def find_all(self) -> List[Doctor]:
        return list(self.doctores.values())

    def update(
        self,
        doctor_id: int,
        doctor_update: DoctorUpdate
    ) -> Optional[Doctor]:

        doctor = self.doctores.get(doctor_id)
        if not doctor:
            return None

        if doctor_update.nombre is not None:
            doctor.nombre = doctor_update.nombre

        if doctor_update.especialidad is not None:
            doctor.especialidad = doctor_update.especialidad

        return doctor

    def delete(self, doctor_id: int) -> bool:
        return self.doctores.pop(doctor_id, None) is not None
