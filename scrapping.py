import os.path

import requests
import csv
import logging
from time import sleep
from pathlib import Path

from config import *

logger = logging.getLogger('parse_detmir')


def write_to_csv(data, fieldnames, filename, directory='files'):
    """
    Записывает список с товарами в csv-файл.
    """
    Path(directory).mkdir(exist_ok=True)
    path = Path(directory) / filename
    try:
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, dialect='excel', quotechar='"', fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            logger.info(f'"message": "Файл {filename} записан"')
    except PermissionError:
        logger.warning(f'"error": "Ошибка записи, файл {filename} занят другой программой"')


def get_prices(product_item):
    """
    Возвращает обычную и, если есть, промо-цену товара.
    """
    if product_item['old_price']:
        return product_item['old_price']['price'], product_item['price']['price']
    return product_item['price']['price'], None


def dict_to_str_params(params_dictionary):
    """
    Склеивает параметры в одно str значение для использования с ключом filter.
    """
    return ';'.join([':'.join([key, value]) for key, value in params_dictionary.items()])


def parse(url, params, cookies, headers):
    """
    Возвращает список продуктов всей категории.
    """
    products = []
    params['offset'] = 0
    while True:
        try:
            # raise requests.HTTPError
            response = requests.get(url, params=params, cookies=cookies, headers=headers)
            logger.info(response.status_code)
            response.raise_for_status()
            items = response.json()['items']
            logger.info(response.url)
        except requests.ConnectionError:
            sleep_time = 10
            logger.warning(f'Connection error. Start sleeping for {sleep_time} secs')
            sleep(sleep_time)
            continue
        except KeyError:
            logger.warning('"error": "В ответе отсутствуют товары"')
            break
        if not items:
            logger.info('"message": "Город обработан"')
            break
        for item in items:
            price, promo_price = get_prices(item)
            product = {
                'id': item['id'],
                'title': item['title'],
                'price': price,
                'promo_price': promo_price,
                'url': item['link']['web_url'],
            }
            products.append(product)
        params['offset'] = params['offset'] + PRODUCTS_PER_PAGE
    return products


def main():
    logging.basicConfig(level=logging.WARN)
    region_iso_codes = REGIONS
    for region in region_iso_codes:
        FILTER_VALUES['withregion'] = region
        FILTER_VALUES['categories[].alias'] = CATEGORY
        REQUEST_PARAMS['filter'] = dict_to_str_params(FILTER_VALUES)
        try:
            products = parse(BASE_URL, REQUEST_PARAMS, COOKIES, HEADERS)
        except requests.HTTPError as err:
            logger.warning(f'"error": "Ошибка ответа сервера при парсинге {region} {err}"')
            continue
        filename = f"{CATEGORY}-{region}.csv"
        write_to_csv(products, FIELDNAMES, filename)
    logger.info('"message": "Парсинг закончен"')


if __name__ == '__main__':
    main()
