from datetime import datetime
from estruturas.lista import Lista
from clinica.diagnostico import criar_arvore_animal


class Medicamento:
    def __init__(self, codigo, nome, quantidade, preco_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario


class Procedimento:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Prontuario:
    def __init__(self, numero, nome_animal, nome_tutor, cpf_tutor, veterinario, consultorio):
        self.numero = numero
        self.nome_animal = nome_animal
        self.nome_tutor = nome_tutor
        self.cpf_tutor = cpf_tutor
        self.veterinario = veterinario
        self.consultorio = consultorio
        self.abertura = datetime.now()
        self.medicamentos = Lista()
        self.procedimentos = Lista()
        self.diagnostico = criar_arvore_animal()
        self.alta = False
        self.fechado = False

    def adicionar_medicamento(self, codigo, nome, quantidade, preco_unitario):
        if self.fechado:
            return False
        existente = self.medicamentos.buscar("codigo", codigo)
        if existente is not None:
            existente.quantidade += quantidade
        else:
            self.medicamentos.adicionar(Medicamento(codigo, nome, quantidade, preco_unitario))
        return True

    def remover_medicamento(self, codigo):
        if self.fechado:
            return None
        return self.medicamentos.remover("codigo", codigo)

    def adicionar_procedimento(self, nome, valor):
        if self.fechado:
            return False
        self.procedimentos.adicionar(Procedimento(nome, valor))
        return True

    def remover_procedimento(self, nome):
        if self.fechado:
            return None
        return self.procedimentos.remover("nome", nome)

    def dar_alta(self):
        self.alta = True

    def fechar(self):
        if not self.alta:
            return False
        self.fechado = True
        return True

    def valor_medicamentos(self):
        total = 0
        for med in self.medicamentos:
            total += med.quantidade * med.preco_unitario
        return total

    def valor_procedimentos(self):
        total = 0
        for proc in self.procedimentos:
            total += proc.valor
        return total


class Prontuarios:
    def __init__(self):
        self.abertos = Lista()
        self.proximo_numero = 1

    def abrir(self, nome_animal, nome_tutor, cpf_tutor, veterinario, consultorio):
        prontuario = Prontuario(self.proximo_numero, nome_animal, nome_tutor, cpf_tutor, veterinario, consultorio)
        self.proximo_numero += 1
        self.abertos.adicionar(prontuario)
        return prontuario

    def buscar(self, numero):
        return self.abertos.buscar("numero", numero)

    def remover(self, numero):
        return self.abertos.remover("numero", numero)
