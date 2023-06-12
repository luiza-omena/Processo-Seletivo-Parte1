import os
os.system("cls")


def read_file(file: str) -> str:
    with open(file, "r") as numbers:
        return numbers.read()

# Pega a string e a tranforma em uma lista, dividindo por ',' onde será separado
# e passando cada item da lista pra int


def create_list(string: str) -> list:
    str_list = string.split(',')
    str_list = [int(i) for i in str_list]
    return str_list


def sum_odds(numbers: list) -> int:
    sum = 0
    for i in numbers:
        if i % 2 != 0:
            sum += i
    return sum


file_string = read_file("numeros.csv")
numbers_list = create_list(file_string)
result = sum_odds(numbers_list)
print(f"A soma dos números ímpares do arquivo é {result}")
