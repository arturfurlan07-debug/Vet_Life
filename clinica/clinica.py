from clinica.tutores import CadastroTutores
from clinica.atendimento import Atendimento
from clinica.estoque import Estoque
from clinica.prontuario import Prontuarios
from clinica.pagamento import Pagamentos
from clinica.consumo import Consumos


class Clinica:
    def __init__(self, quantidade_consultorios):
        self.tutores = CadastroTutores()
        self.atendimento = Atendimento(quantidade_consultorios)
        self.estoque = Estoque()
        self.prontuarios = Prontuarios()
        self.pagamentos = Pagamentos()
        self.consumos = Consumos()

    def registrar_chegada(self, cpf, nome_animal, queixa, emergencia):
        tutor = self.tutores.buscar_tutor(cpf)
        if tutor is None:
            return None
        animal = self.tutores.buscar_animal(cpf, nome_animal)
        if animal is None:
            return None
        return self.atendimento.registrar_chegada(animal.nome, tutor.nome, queixa, emergencia, cpf)

    def chamar_proximo(self, veterinario):
        chamado = self.atendimento.chamar_proximo()
        if chamado is None:
            return None
        consultorio, chegada = chamado
        return self.prontuarios.abrir(chegada.nome_animal, chegada.nome_tutor,
                                      chegada.cpf_tutor, veterinario, consultorio.numero)

    def adicionar_medicamento(self, numero, codigo, quantidade, hoje):
         if not isinstance(quantidade, int) or quantidade <= 0:
            return False
        prontuario = self.prontuarios.buscar(numero)
        produto = self.estoque.buscar_produto(codigo)
        if prontuario is None or produto is None:
            return False
        if self.estoque.disponivel(codigo, hoje) < quantidade:
            return False
        return prontuario.adicionar_medicamento(codigo, produto.nome, quantidade, produto.preco_venda)

    def remover_medicamento(self, numero, codigo):
        prontuario = self.prontuarios.buscar(numero)
        if prontuario is None:
            return None
        return prontuario.remover_medicamento(codigo)

    def adicionar_procedimento(self, numero, nome, valor):
        if not nome or not isinstance(valor, (int, float)) or valor < 0:
            return False
        prontuario = self.prontuarios.buscar(numero)

    def remover_procedimento(self, numero, nome):
        prontuario = self.prontuarios.buscar(numero)
        if prontuario is None:
            return None
        return prontuario.remover_procedimento(nome)

    def dar_alta(self, numero):
        prontuario = self.prontuarios.buscar(numero)
        if prontuario is None or prontuario.alta:
            return False
        prontuario.dar_alta()
        self.atendimento.liberar_consultorio(prontuario.consultorio)
        return True

    def fechar_prontuario(self, numero, forma, parcelas, hoje):
        prontuario = self.prontuarios.buscar(numero)
        if prontuario is None:
            return None, "Prontuário não encontrado."
        if not prontuario.alta:
            return None, "O animal ainda não recebeu alta."
        for med in prontuario.medicamentos:
            if self.estoque.disponivel(med.codigo, hoje) < med.quantidade:
                return None, "Estoque insuficiente de " + med.nome + "."
        pagamento = self.pagamentos.registrar(prontuario.nome_tutor, prontuario.numero, forma, parcelas,
                                              prontuario.valor_medicamentos(),
                                              prontuario.valor_procedimentos())
        if pagamento is None:
            return None, "Forma de pagamento inválida."
        for med in prontuario.medicamentos:
            if not self.estoque.baixar(med.codigo, med.quantidade, hoje):
                return None, "Não foi possível baixar o estoque de " + med.nome + "."
            self.consumos.registrar(prontuario, med)
        prontuario.fechar()
        self.prontuarios.remover(numero)
        return pagamento, ""
