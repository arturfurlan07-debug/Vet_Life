from estruturas.lista import Lista


class Animal:
    def __init__(self, nome, especie, raca, idade):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade


class Tutor:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.animais = Lista()


class CadastroTutores:
    def __init__(self):
        self.tutores = Lista()

    def cadastrar_tutor(self, nome, cpf, telefone):
        if self.buscar_tutor(cpf) is not None:
            return None
        tutor = Tutor(nome, cpf, telefone)
        self.tutores.adicionar(tutor)
        return tutor

    def buscar_tutor(self, cpf):
        return self.tutores.buscar("cpf", cpf)

    def remover_tutor(self, cpf):
        return self.tutores.remover("cpf", cpf)

    def cadastrar_animal(self, cpf, nome, especie, raca, idade):
        tutor = self.buscar_tutor(cpf)
        if tutor is None:
            return None
        if tutor.animais.buscar("nome", nome) is not None:
            return None
        animal = Animal(nome, especie, raca, idade)
        tutor.animais.adicionar(animal)
        return animal

    def buscar_animal(self, cpf, nome_animal):
        tutor = self.buscar_tutor(cpf)
        if tutor is None:
            return None
        return tutor.animais.buscar("nome", nome_animal)

    def remover_animal(self, cpf, nome_animal):
        tutor = self.buscar_tutor(cpf)
        if tutor is None:
            return None
        return tutor.animais.remover("nome", nome_animal)
