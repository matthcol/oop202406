from dataclasses import dataclass
from datetime import date
from typing import Self


@dataclass
class Person:
    """represents a person with its firstname, lastname, birthdate
    """

    # attributes
    firstname: str
    lastname: str
    birthdate: date

    # methods
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} ({self.birthdate:%d/%m/%Y})"
    
    def to_json(self) -> str:
        return f'''{{ 
    "firstname": "{self.firstname}",
    "lastname": "{self.lastname}",
    "birthdate": "{self.birthdate}" 
}}'''
    
    def copy(self) -> Self:
        return Person(firstname=self.firstname, lastname=self.lastname, birthdate=self.lastname)