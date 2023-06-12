from random import randint
import os
# Limpa o terminal
os.system("cls")

# Gera uma lista com 20 numeros aleatorios de 1 a 100


def gera_lista() -> list:
    lista = []
    for i in range(20):
        lista.append(randint(1, 100))
    return lista


lista = gera_lista()
maior = max(lista)


print(f"""Lista gerada: {lista}
O maior número da lista de números aleatórios é {maior}""")
