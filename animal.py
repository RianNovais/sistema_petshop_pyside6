from dataclasses import dataclass

@dataclass
class Animal():
    nome: str
    tipo : str
    raça : str
    idade : int
    tutor : str