from estruturas.lista import Lista


class Consumo:
    def __init__(self, numero_prontuario, cpf_tutor, nome_tutor, nome_animal, codigo, nome_produto, quantidade, valor):
        self.numero_prontuario = numero_prontuario
        self.cpf_tutor = cpf_tutor
        self.nome_tutor = nome_tutor
        self.nome_animal = nome_animal
        self.codigo = codigo
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.valor = valor


class Consumos:
    def __init__(self):
        self.lista = Lista()

    def registrar(self, prontuario, medicamento):
        valor = medicamento.quantidade * medicamento.preco_unitario
        consumo = Consumo(prontuario.numero, prontuario.cpf_tutor, prontuario.nome_tutor,
                          prontuario.nome_animal, medicamento.codigo, medicamento.nome,
                          medicamento.quantidade, valor)
        self.lista.adicionar(consumo)
        return consumo
