import logging
logging.basicConfig(level=logging.DEBUG)


def add(x, y):
    logging.info("Dodaje %s i %s" % (num1, num2))
    return x + y


def deduct(x, y):
    logging.info("Odejmuje %s i %s" % (num1, num2))
    return x - y


def multiply(x, y):
    logging.info("Mnoze %s i %s" % (num1, num2))
    return x * y


def divide(x, y):
    logging.info("Dziele %s i %s" % (num1, num2))
    return x / y


def power(x, y):
    logging.info("Poteguje %s i %s" % (num1, num2))
    return x ** y


def operation(action):
    return {
        '1': add,
        '2': deduct,
        '3': multiply,
        '4': divide,
        '5': power
    }[action]


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

    print(operation(choice)(num1, num2))
