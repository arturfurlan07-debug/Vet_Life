from estruturas.arvore import Arvore, NoArvore

animal = NoArvore("Animal")

digestorio = NoArvore("Sistema digestório")
digestorio.adicionar_filho(NoArvore("Estômago", "D01"))
digestorio.adicionar_filho(NoArvore("Intestino", "D02"))

respiratorio = NoArvore("Sistema respiratório")
respiratorio.adicionar_filho(NoArvore("Pulmões", "R01"))
respiratorio.adicionar_filho(NoArvore("Traqueia", "R02"))

animal.adicionar_filho(digestorio)
animal.adicionar_filho(respiratorio)

arvore = Arvore(animal)

print("Árvore inicial:")
arvore.exibir()

print()
print("Marcando R01 como alterado:", arvore.marcar_alterado("R01"))
print("Marcando código que não existe:", arvore.marcar_alterado("X99"))

print()
print("Árvore depois do diagnóstico:")
arvore.exibir()
