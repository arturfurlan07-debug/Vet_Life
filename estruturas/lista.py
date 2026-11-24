class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1

    def buscar(self, atributo, valor_procurado):
        atual = self.inicio
        while atual is not None:
            if getattr(atual.valor, atributo) == valor_procurado:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, atributo, valor_procurado):
        anterior = None
        atual = self.inicio
        while atual is not None:
            if getattr(atual.valor, atributo) == valor_procurado:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.valor
            anterior = atual
            atual = atual.proximo
        return None

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
        