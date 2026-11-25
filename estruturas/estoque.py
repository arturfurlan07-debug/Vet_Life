from estruturas.fila import Fila
from estruturas.lista import Lista


class Lote:
    def __init__(self, numero, fornecedor, preco_compra, data_compra, validade, quantidade):
        self.numero = numero
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.data_compra = data_compra
        self.validade = validade
        self.quantidade = quantidade


class Produto:
    def __init__(self, codigo, nome, preco_venda, minimo):
        self.codigo = codigo
        self.nome = nome
        self.preco_venda = preco_venda
        self.minimo = minimo
        self.lotes = Fila()

    def total(self):
        soma = 0
        for lote in self.lotes:
            soma += lote.quantidade
        return soma


class Perda:
    def __init__(self, codigo, nome_produto, numero_lote, quantidade, valor, data):
        self.codigo = codigo
        self.nome_produto = nome_produto
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.valor = valor
        self.data = data


class Estoque:
    def __init__(self):
        self.produtos = Lista()
        self.perdas = Lista()
        self.proximo_lote = 1

    def cadastrar_produto(self, codigo, nome, preco_venda, minimo):
        if self.buscar_produto(codigo) is not None:
            return None
        produto = Produto(codigo, nome, preco_venda, minimo)
        self.produtos.adicionar(produto)
        return produto

    def buscar_produto(self, codigo):
        return self.produtos.buscar("codigo", codigo)

    def comprar_lote(self, codigo, fornecedor, preco_compra, data_compra, validade, quantidade):
        produto = self.buscar_produto(codigo)
        if produto is None:
            return None
        lote = Lote(self.proximo_lote, fornecedor, preco_compra, data_compra, validade, quantidade)
        self.proximo_lote += 1
        produto.lotes.enfileirar(lote)
        return lote

    def descartar_vencidos(self, hoje):
        descartados = 0
        for produto in self.produtos:
            lotes_bons = Fila()
            while not produto.lotes.vazia():
                lote = produto.lotes.desenfileirar()
                if lote.validade is not None and lote.validade < hoje:
                    valor = lote.quantidade * lote.preco_compra
                    perda = Perda(produto.codigo, produto.nome, lote.numero, lote.quantidade, valor, hoje)
                    self.perdas.adicionar(perda)
                    descartados += 1
                else:
                    lotes_bons.enfileirar(lote)
            produto.lotes = lotes_bons
        return descartados

    def disponivel(self, codigo, hoje):
        produto = self.buscar_produto(codigo)
        if produto is None:
            return 0
        self.descartar_vencidos(hoje)
        return produto.total()

    def baixar(self, codigo, quantidade, hoje):
        if self.disponivel(codigo, hoje) < quantidade:
            return False
        produto = self.buscar_produto(codigo)
        restante = quantidade
        while restante > 0:
            lote = produto.lotes.primeiro()
            if lote.quantidade <= restante:
                restante -= lote.quantidade
                produto.lotes.desenfileirar()
            else:
                lote.quantidade -= restante
                restante = 0
        return True

    def ajustar_quantidade(self, codigo, numero_lote, nova_quantidade):
        produto = self.buscar_produto(codigo)
        if produto is None:
            return False
        for lote in produto.lotes:
            if lote.numero == numero_lote:
                lote.quantidade = nova_quantidade
                return True
        return False

    def abaixo_do_minimo(self):
        alertas = Lista()
        for produto in self.produtos:
            if produto.total() < produto.minimo:
                alertas.adicionar(produto)
        return alertas
