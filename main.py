from dataclasses import dataclass
import time
import random
import string
from typing import List
import logging
COMPANY_NAMES: List[str] = ['dell', 'php', 'gg', 'hello', 'stocks']
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class Stocks:
    company_name: str
    price: float


def generate_stocks() -> list[Stocks]:
    stocks_list: list[Stocks] = []
    for company in COMPANY_NAMES:
        random_price: float = random.uniform(1, 5000)
        random_company: Stocks = Stocks(company, random_price)
        stocks_list.append(random_company)
    return stocks_list


def main():
    try:
        while True:
            stock_list: list[Stocks] = generate_stocks()
            for company_price in stock_list:
                print(company_price.price)
                logging.info(company_price.price)
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Interrupted! Exiting gracefully...")


if __name__ == "__main__":
    main()
