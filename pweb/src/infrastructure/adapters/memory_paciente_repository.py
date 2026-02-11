from typing import List, Optional
import uuid

from src.application.ports.paciente_repository import PacienteRepository
from src.domain.paciente import (
    Paciente,
    PacienteCreate,
    PacienteUpdate
)


class MemoryPacienteRepository(PacienteRepository):

    def __init__(self):
        self.pacientes: dict[str, Paciente] = {}

    def save(self, paciente: PacienteCreate) -> Paciente:
        paciente_id = str(uuid.uuid4())

        new_paciente = Paciente(
            id=paciente_id,
            nombre=paciente.nombre,
            email=paciente.email
        )

        self.pacientes[paciente_id] = new_paciente
        return new_paciente

    def find_by_id(self, paciente_id: str) -> Optional[Paciente]:
        return self.pacientes.get(paciente_id)

    def find_by_email(self, email: str) -> Optional[Paciente]:
        return next(
            (p for p in self.pacientes.values() if p.email == email),
            None
        )

    def find_all(self) -> List[Paciente]:
        return list(self.pacientes.values())

    def update(
        self,
        paciente_id: str,
        paciente_update: PacienteUpdate
    ) -> Optional[Paciente]:

        paciente = self.pacientes.get(paciente_id)
        if not paciente:
            return None

        if paciente_update.nombre is not None:
            paciente.nombre = paciente_update.nombre

        if paciente_update.email is not None:
            paciente.email = paciente_update.email

        return paciente

    def delete(self, paciente_id: str) -> bool:
        return self.pacientes.pop(paciente_id, None) is not None
