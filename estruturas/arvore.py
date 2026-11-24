from estruturas.lista import Lista


class NoArvore:
    def __init__(self, nome, codigo=None):
        self.nome = nome
        self.codigo = codigo
        self.estado = "Saudável"
        self.filhos = Lista()

    def adicionar_filho(self, filho):
        self.filhos.adicionar(filho)


class Arvore:
    def __init__(self, raiz):
        self.raiz = raiz

    def exibir(self):
        self._pre_ordem(self.raiz, 0)

    def _pre_ordem(self, no, nivel):
        codigo = f" (cód. {no.codigo})" if no.codigo else ""
        alerta = " [ALTERADO]" if no.estado == "Alterado" else ""
        print("    " * nivel + "- " + no.nome + codigo + alerta)
        for filho in no.filhos:
            self._pre_ordem(filho, nivel + 1)

    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, no, codigo):
        if no.codigo == codigo:
            return no
        for filho in no.filhos:
            achado = self._buscar(filho, codigo)
            if achado is not None:
                return achado
        return None

    def marcar_alterado(self, codigo):
        no = self.buscar(codigo)
        if no is None:
            return False
        no.estado = "Alterado"
        return True
