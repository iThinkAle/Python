# Questo programma permettere di convertere i soldi da una valuta all'altra.
# By iThinkAle

from currency_converter import CurrencyConverter
import datetime
c = CurrencyConverter()


now = datetime.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def convert():
    try:
        newcurrency = c.convert(quantity, currency1, currency2)
        print(f"{quantity} in {currency2} (alle {dt_string}) è: {newcurrency}")
    except ValueError:
        print("Errore! Valuta non supportata!")


def main():
    print("Benvenuto nel convertitore di valuta.")
    currency1 = input("Inserisci la valuta da convertire (codice (es: USD, EUR)): ")
    currency2 = input("Inserisci la valuta a cui vuoi che la tua cifra sia convertita (codice): ")
    quantity = float(input("Inserisci la cifra di denaro da convertire: "))
    global currency1, currency2, quantity
    convert()


if __name__ == "__main__":
    main()
