from fila import Fila

fila = Fila()
print("Vazia:", fila.vazia())

fila.enfileirar("Rex")
fila.enfileirar("Mia")
fila.enfileirar("Bolt")
print("Tamanho:", len(fila))
print("Primeiro da fila:", fila.primeiro())

print("Atendendo:", fila.desenfileirar())
print("Atendendo:", fila.desenfileirar())
print("Tamanho:", len(fila))

print("Quem ainda espera:")
for animal in fila:
    print("-", animal)

fila.desenfileirar()
print("Vazia:", fila.vazia())
print("Desenfileirar com fila vazia:", fila.desenfileirar())
