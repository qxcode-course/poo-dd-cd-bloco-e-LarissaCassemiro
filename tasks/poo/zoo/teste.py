from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, vid: str, entrada: int, tipo: str):
        self.id = vid
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self, tempo_saida: int) -> float:
        pass

    def toString(self) -> str:
        return (
            f"{self.tipo:>10}".replace(" ", "_") + " : " +
            f"{self.id:>10}".replace(" ", "_") + " : " +
            str(self.entrada)
        )

    def __str__(self):
        return self.toString()


class Bike(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Bike")

    def calcularValor(self, tempo_saida: int) -> float:
        return 3.0


class Moto(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Moto")

    def calcularValor(self, tempo_saida: int) -> float:
        minutos = tempo_saida - self.entrada
        return minutos / 20


class Carro(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Carro")

    def calcularValor(self, tempo_saida: int) -> float:
        minutos = tempo_saida - self.entrada
        valor = minutos / 10
        return 5.0 if valor < 5 else valor


class Estacionamento:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.hora_atual = 0

    def tempo(self, minutos: int):
        self.hora_atual += minutos

    def estacionar(self, tipo: str, vid: str):
        if self.buscar(vid) is not None:
            print("fail: veiculo ja existe")
            return

        if tipo == "bike":
            self.veiculos.append(Bike(vid, self.hora_atual))
        elif tipo == "moto":
            self.veiculos.append(Moto(vid, self.hora_atual))
        elif tipo == "carro":
            self.veiculos.append(Carro(vid, self.hora_atual))
        else:
            print("fail: tipo invalido")

    def buscar(self, vid: str):
        for v in self.veiculos:
            if v.id == vid:
                return v
        return None

    def pagar(self, vid: str):
        veiculo = self.buscar(vid)
        if veiculo is None:
            print("fail: veiculo nao encontrado")
            return

        tempo_saida = self.hora_atual
        valor = veiculo.calcularValor(tempo_saida)
        print(f"{veiculo.tipo} chegou {veiculo.entrada} saiu {tempo_saida}. Pagar R$ {valor:.2f}")
        self.veiculos.remove(veiculo)

    def show(self):
        for v in self.veiculos:
            print(v)
        print(f"Hora atual: {self.hora_atual}")


def main():
    est = Estacionamento()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if len(args) == 0:
            continue

        if args[0] == "end":
            break

        elif args[0] == "tempo":
            est.tempo(int(args[1]))

        elif args[0] == "estacionar":
            tipo = args[1]
            vid = args[2]
            est.estacionar(tipo, vid)

        elif args[0] == "pagar":
            vid = args[1]
            est.pagar(vid)

        elif args[0] == "show":
            est.show()

        else:
            print("fail: comando invalido")


main()
