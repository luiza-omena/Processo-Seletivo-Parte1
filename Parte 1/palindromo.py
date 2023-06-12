import os
# Limpa o terminal
os.system("cls")

# Verifica se uma palavra é ou não palíndromo


def verifica_palindromo(palavra: str) -> bool:
    palavra = palavra.lower()
    inverso = palavra[::-1]
    if palavra == inverso:
        return True
    else:
        return False


palavra = input("Escreva uma palavra para verificar se é palíndroma: ")
palindromo = verifica_palindromo(palavra)
if palindromo == True:
    print(f"Sim, a palavra {palavra} é palíndroma")
else:
    print(f"Não, a palavra {palavra} não é palíndroma")
