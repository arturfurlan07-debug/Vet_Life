from lista import Lista


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


lista = Lista()
lista.adicionar(Pessoa("Ana", "111"))
lista.adicionar(Pessoa("Bruno", "222"))
lista.adicionar(Pessoa("Carla", "333"))
print("Tamanho:", len(lista))

achada = lista.buscar("cpf", "222")
print("Buscou 222:", achada.nome)
print("Buscou 999:", lista.buscar("cpf", "999"))

removida = lista.remover("cpf", "111")
print("Removeu:", removida.nome)
print("Tamanho:", len(lista))

print("Nomes que sobraram:")
for pessoa in lista:
    print("-", pessoa.nome)
