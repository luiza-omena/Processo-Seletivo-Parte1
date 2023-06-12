from random import randint
import os
os.system("cls")

# Gera uma lista com 20 numeros aleatorios de 1 a 100


def list_generate() -> list:
    list = []
    for i in range(20):
        list.append(randint(1, 100))
    return list


list = list_generate()
max = max(list)


print(f"""Lista gerada: {list}
O maior número da lista de números aleatórios é {max}""")
