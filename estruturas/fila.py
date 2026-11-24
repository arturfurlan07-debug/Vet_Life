class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, valor):
        novo = NoFila(valor)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor

    def primeiro(self):
        if self.inicio is None:
            return None
        return self.inicio.valor

    def vazia(self):
        return self.inicio is None

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
