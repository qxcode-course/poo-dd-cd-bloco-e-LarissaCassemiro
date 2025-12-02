from abc import ABC, abstractmethod

class Animal (ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome 

    def apresentar_nome(self, nome: str): 
        print(f"eu sou {self.nome}")

    @abstractmethod
    def fazer_som(self) -> None:
        pass
    @abstractmethod
    def mover(self) -> None:
        pass

    
def apresentar(animal: Animal):
    animal.fazer_som()
    animal.mover()
    animal.apresentar_nome()

class Leao(Animal):
    def __init__(self, nome: str)-> None:
        super().__init__(nome)

    def fazer_som(self):
        print("graaaam")
    def mover(self):
        print("caminhando em silencio")

    def apresentar_nome(self, nome):
        pass

class Elefante(Animal):
    def __init__(self, nome: str)-> None:
        super().__init__(nome)

    def fazer_som(self):
        print("fuuuur")
    def mover(self):
        print("passos macios")

    def apresentar_nome(self, nome):
        pass


class Cobra(Animal):
    def __init__(self, nome: str)-> None:
        super().__init__(nome)

    def fazer_som(self):
        print("sssss")
    def mover(self):
        print("rastejaaando")

    def apresentar_nome(self, nome):
        pass