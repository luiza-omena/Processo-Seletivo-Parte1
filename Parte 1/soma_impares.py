import os
# Limpa o terminal
os.system("cls")

# Abre o arquivo e o transforma em uma unica string


def le_arquivo(arquivo: str) -> str:
    with open(arquivo, "r") as numeros:
        return numeros.read()

# Pega a string e a tranforma em uma lista, dividindo por ',' onde será separado
# e passando cada item da lista pra int


def cria_lista(string: str) -> list:
    lista_str = string.split(',')
    lista_int = [int(i) for i in lista_str]
    return lista_int

# Soma cada item impar da lista e retorna essa soma


def soma_impares(numeros: list) -> int:
    soma = 0
    for i in numeros:
        if i % 2 != 0:
            soma += i
    return soma


# Main (chama as funções)
arq_string = le_arquivo("numeros.csv")
lista_numeros = cria_lista(arq_string)
result = soma_impares(lista_numeros)
print(f"A soma dos números ímpares do arquivo é {result}")
