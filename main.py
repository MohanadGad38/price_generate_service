from dataclasses import dataclass
import time
import random
from typing import List
import logging
import pika
from pika.adapters.blocking_connection import BlockingChannel
import pika.connection
import json
from dotenv import load_dotenv
import os
load_dotenv('rabbitmq.env')


credentials = pika.PlainCredentials(os.environ.get(
    "RABBITMQ_DEFAULT_USER"), os.environ.get("RABBITMQ_DEFAULT_PASS"))
connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials
)
connection = pika.BlockingConnection(connection_params)
channel: BlockingChannel = connection.channel()
channel.exchange_declare(exchange='Stocks', exchange_type='direct')


COMPANY_NAMES: List[str] = ['dell', 'php', 'gg', 'hello', 'stocks']
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def send(name: str, price: str):
    channel.basic_publish(exchange='Stocks', routing_key="stock.price",
                          body=json.dumps({"company": name, "stock_price": price}))


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
                send(company_price.company_name, company_price.price)
                logging.info(company_price.price)
            time.sleep(10)
    except KeyboardInterrupt:
        connection.close()
        logging.info("Interrupted! Exiting gracefully...")


if __name__ == "__main__":
    main()
