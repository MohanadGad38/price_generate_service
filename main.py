from dataclasses import dataclass
import time
import random


@dataclass
class Stocks:
    company_name: str
    price: float


def main():
    stocks_list: list[Stocks] = []
    dell: Stocks = Stocks("dell", 5)
    stocks_list.append(dell)
    php: Stocks = Stocks("php", 10)
    stocks_list.append(php)
    pepsi: Stocks = Stocks("pepsi", 10)
    stocks_list.append(pepsi)
    cola: Stocks = Stocks("cola", 20)
    stocks_list.append(cola)
    lm: Stocks = Stocks("lm", 21)
    stocks_list.append(lm)
    while True:
        random_float: float = random.uniform(0, 100000)
        for i in range(len(stocks_list)):
            stocks_list[i].price = random_float
            print(stocks_list[i].company_name)
            print(stocks_list[i].price)
            time.sleep(60)


if __name__ == "__main__":
    main()
