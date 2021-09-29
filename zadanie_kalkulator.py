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

def power(x, y):
    return x ** y


if __name__ == "__main__":
    print("Mini kalkulator.")
    print("1 Dodawanie")
    print("2 Odejmowanie")
    print("3 Mnozenie")
    print("4 Dzielenie")
    print("5 Potegowanie")

    choice = input("Podaj dzialanie, poslugujac sie odpowiednia liczba (1/2/3/4/5): ")

    num1 = float(input("Podaj pierwsza liczbe: "))
    num2 = float(input("Podaj druga liczbe: "))

    def operation(choice):
        return {
            '1': num1 + num2,
            '2': num1 - num2,
            '3': num1 * num2,
            '4': num1 / num2,
            '5': num1 ** num2
                }[choice]

    print(operation(choice))
