import os
os.system("cls")

# Verifica se uma palavra é ou não palíndromo


def is_reversible(word: str) -> bool:
    word = word.lower()
    reverse = word[::-1]
    if word == reverse:
        return True

    return False


word = input("Escreva uma palavra para verificar se é palíndroma: ")
reversible = is_reversible(word)
if reversible == True:
    print(f"Sim, a palavra {word} é palíndroma")
else:
    print(f"Não, a palavra {word} não é palíndroma")
