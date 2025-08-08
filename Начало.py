book = "Книга"

name = input("Введите имя человека: ")


with open(book, "r", encoding="utf-8") as file:
    for line in file:
        print(line)