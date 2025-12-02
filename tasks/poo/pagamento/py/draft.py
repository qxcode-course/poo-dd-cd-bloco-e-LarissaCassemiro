from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class MetodoPix(MetodoPagamento):
    def __init__(self, chave: str):
        self.chave = chave 
    
    def processar_pagamento(self, valor:float):
       print(f"pagando chave: {self.chave}, valor> {self.valor} com pix")


# teste
class Pagamento:
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor 
        self.descricao: str = descricao

    def pagar(self):
        self.metodo.processar_pagamento(self.valor)

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str, metodo: MetodoPagamento):
        self.valor: float = valor
        self.descricao = descricao
        self.metodo = metodo 
    
    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
    
    @abstractmethod
    def processar(self):
        pass
    
class CartaoCredito(Pagamento):
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor


def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

class Pix(Pagamento):
    def __init__(self, chave: int, banco: str, valor, descricao):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        try:
            self.validar_valor()
            print(f"{self.banco}:{self.chave}")
        except ValueError as e:
            print (e)

class Boleto(Pagamento):
    def __init__(self, codigo_de_barras: int, vencimento: str, valor, descricao):
        super().__init__(valor, descricao)
        self.codigo_de_barras = codigo_de_barras
        self.vencimento = vencimento 

    def processar(self):
            print("Boleto gerado. Aguardando pagamento...")


pag: Pagamento = CartaoCredito(nome= "David", descricao="Coxinha", limite=500.00, num=123, valor=0.50)
pagamentos: list[Pagamento] = [pag]
processar_pagamentos(pagamentos)