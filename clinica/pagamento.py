from datetime import datetime
from estruturas.lista import Lista


class Pagamento:
    def __init__(self, pagador, numero_prontuario, forma, parcelas, valor_medicamentos, valor_procedimentos):
        self.pagador = pagador
        self.numero_prontuario = numero_prontuario
        self.forma = forma
        self.parcelas = parcelas
        self.valor_medicamentos = valor_medicamentos
        self.valor_procedimentos = valor_procedimentos
        self.total = valor_medicamentos + valor_procedimentos
        self.data_hora = datetime.now()


class Pagamentos:
    def __init__(self):
        self.lista = Lista()

    def registrar(self, pagador, numero_prontuario, forma, parcelas, valor_medicamentos, valor_procedimentos):
        forma = forma.upper()
        if forma == "PIX" or forma == "DINHEIRO":
            parcelas = None
        elif forma == "CARTAO":
            if parcelas is None or parcelas < 1:
                parcelas = 1
        else:
            return None
        pagamento = Pagamento(pagador, numero_prontuario, forma, parcelas, valor_medicamentos, valor_procedimentos)
        self.lista.adicionar(pagamento)
        return pagamento
