from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.doctor import (Doctor, DoctorCreate, DoctorUpdate)

class DoctorRepository(ABC):

    @abstractmethod
    def save(self, doctor: DoctorCreate) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, doctor_id: int) -> Optional[Doctor]:
        pass

    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def update(
        self,
        doctor_id: int,
        doctor_update: DoctorUpdate
    ) -> Optional[Doctor]:
        pass

    @abstractmethod
    def delete(self, doctor_id: int) -> bool:
        pass
