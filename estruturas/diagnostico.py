from estruturas.arvore import Arvore, NoArvore


def criar_arvore_animal():
    animal = NoArvore("Animal")

    digestorio = NoArvore("Sistema digestório")
    digestorio.adicionar_filho(NoArvore("Estômago", "D01"))
    digestorio.adicionar_filho(NoArvore("Intestino", "D02"))

    respiratorio = NoArvore("Sistema respiratório")
    respiratorio.adicionar_filho(NoArvore("Pulmões", "R01"))
    respiratorio.adicionar_filho(NoArvore("Traqueia", "R02"))

    pele = NoArvore("Pele")
    pele.adicionar_filho(NoArvore("Pelos", "P01"))
    pele.adicionar_filho(NoArvore("Unhas", "P02"))

    animal.adicionar_filho(digestorio)
    animal.adicionar_filho(respiratorio)
    animal.adicionar_filho(pele)

    return Arvore(animal)
