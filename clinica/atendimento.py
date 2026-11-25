from datetime import datetime
from estruturas.fila import Fila
from estruturas.lista import Lista


class Chegada:
    def __init__(self, nome_animal, nome_tutor, queixa, emergencia, cpf_tutor):
        self.nome_animal = nome_animal
        self.nome_tutor = nome_tutor
        self.queixa = queixa
        self.emergencia = emergencia
        self.cpf_tutor = cpf_tutor
        self.data_hora = datetime.now()


class Consultorio:
    def __init__(self, numero):
        self.numero = numero
        self.chegada = None


class Atendimento:
    def __init__(self, quantidade_consultorios):
        self.fila_emergencia = Fila()
        self.fila_normal = Fila()
        self.consultorios = Lista()
        for numero in range(1, quantidade_consultorios + 1):
            self.consultorios.adicionar(Consultorio(numero))

    def registrar_chegada(self, nome_animal, nome_tutor, queixa, emergencia=False, cpf_tutor=None):
        chegada = Chegada(nome_animal, nome_tutor, queixa, emergencia, cpf_tutor)
        if emergencia:
            self.fila_emergencia.enfileirar(chegada)
        else:
            self.fila_normal.enfileirar(chegada)
        return chegada

    def proximo(self):
        if not self.fila_emergencia.vazia():
            return self.fila_emergencia.primeiro()
        return self.fila_normal.primeiro()

    def consultorio_livre(self):
        return self.consultorios.buscar("chegada", None)

    def chamar_proximo(self):
        consultorio = self.consultorio_livre()
        if consultorio is None:
            return None
        if not self.fila_emergencia.vazia():
            chegada = self.fila_emergencia.desenfileirar()
        else:
            chegada = self.fila_normal.desenfileirar()
        if chegada is None:
            return None
        consultorio.chegada = chegada
        return consultorio, chegada

    def liberar_consultorio(self, numero):
        consultorio = self.consultorios.buscar("numero", numero)
        if consultorio is not None:
            consultorio.chegada = None

    def total_espera(self):
        return len(self.fila_emergencia) + len(self.fila_normal)
