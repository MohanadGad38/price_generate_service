from dataclasses import dataclass
import time
import random
from typing import List
import logging
import pika
from pika.adapters.blocking_connection import BlockingChannel
import pika.connection
import json
credentials = pika.PlainCredentials('mohanad.gad', '19941994')
connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials
)
connection = pika.BlockingConnection(connection_params)
channel: BlockingChannel = connection.channel()
channel.exchange_declare(exchange='Stocks', exchange_type='direct')
test = {"id": 1, "email": "mohanad.gad"}
channel.basic_publish(exchange='Stocks', routing_key="stock.price",
                      body=json.dumps({"email": test['email']}))
print('message sent')
channel.basic_publish(
    exchange="Stocks", routing_key="stock.info", body=json.dumps(test))
print("message")
connection.close()

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
