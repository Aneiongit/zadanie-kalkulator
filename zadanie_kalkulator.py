import sys
import logging
logging.basicConfig(level=logging.DEBUG)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if __name__ == "__main__":
    print("Mini kalkulator.")
    print("1 Dodawanie")
    print("2 Odejmowanie")
    print("3 Mnozenie")
    print("4 Dzielenie")

    choice = input("Podaj dzialanie, poslugujac sie odpowiednia liczba (1/2/3/4): ")

    num1 = int(input("Podaj pierwsza liczbe: "))
    num2 = int(input("Podaj druga liczbe: "))

    if choice == '1':
        logging.debug("Dodaje", num1, 'i', num2)
        print("Wynik to:", add(num1, num2))

    elif choice == '2':
        logging.debug("Odejmuje", num1, 'i', num2)
        print("Wynik to:", subtract(num1, num2))

    elif choice == '3':
        logging.debug("Mnoze", num1, 'i', num2)
        print("Wynik to:", multiply(num1, num2))

    elif choice == '4':
        logging.debug("Dziele", num1, 'i', num2)
        print("Wynik to:", divide(num1, num2))
    exit(0)
