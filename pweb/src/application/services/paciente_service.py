from typing import List, Optional
from src.application.ports.paciente_repository import PacienteRepository
from src.domain.paciente import (Paciente, PacienteCreate, PacienteUpdate)


class PacienteService:
    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    # Caso de uso: Registrar un nuevo paciente
    def register_paciente(self, paciente_data: PacienteCreate) -> Paciente:
        # Reglas de negocio
        if not paciente_data.nombre or not paciente_data.email:
            raise ValueError("El nombre y el correo electrónico son obligatorios")

        # Validar que el email no esté registrado
        if self.repository.find_by_email(paciente_data.email):
            raise ValueError(
                f"El correo electrónico {paciente_data.email} ya está registrado"
            )

        return self.repository.save(paciente_data)

    # Caso de uso: Obtener paciente por ID
    def get_paciente(self, paciente_id: str) -> Optional[Paciente]:
        return self.repository.find_by_id(paciente_id)

    # Caso de uso: Listar todos los pacientes
    def get_all_pacientes(self) -> List[Paciente]:
        return self.repository.find_all()

    # Caso de uso: Actualizar paciente
    def update_paciente(
        self,
        paciente_id: str,
        paciente_update: PacienteUpdate
    ) -> Optional[Paciente]:

        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None

        # Validar email duplicado
        if (
            paciente_update.email is not None
            and paciente_update.email != paciente.email
            and self.repository.find_by_email(paciente_update.email)
        ):
            raise ValueError(
                f"El correo electrónico {paciente_update.email} ya está en uso"
            )

        return self.repository.update(paciente_id, paciente_update)

    # Caso de uso: Eliminar paciente
    def delete_paciente(self, paciente_id: str) -> bool:
        return self.repository.delete(paciente_id)
