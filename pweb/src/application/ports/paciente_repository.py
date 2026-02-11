from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.paciente import (Paciente, PacienteCreate, PacienteUpdate )


class PacienteRepository(ABC):

    @abstractmethod
    def save(self, paciente: PacienteCreate) -> Paciente:
        pass

    @abstractmethod
    def find_by_id(self, paciente_id: str) -> Optional[Paciente]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Paciente]:
        pass

    @abstractmethod
    def find_all(self) -> List[Paciente]:
        pass

    @abstractmethod
    def update(
        self,
        paciente_id: str,
        paciente_update: PacienteUpdate
    ) -> Optional[Paciente]:
        pass

    @abstractmethod
    def delete(self, paciente_id: str) -> bool:
        pass
