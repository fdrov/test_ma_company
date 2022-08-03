# Парсинг данных с сайта «Детский мир»
Скрипт позволяет скачать в csv-файл список всех товаров определенной категории.

> Скрипт написан в тестовых целях. Использовать ответственно.

## Технические требования
* должен быть установлен Python 3.8 и выше
* библиотеки из файла requirements.txt

## Запуск
1. Создать и запустить виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```
2. Установить зависимости:
```bash
pip install -r requirements.txt
```
3. Заполнить в файле `config.py` параметр CATEGORY значением категории, которую нужно спарсить
Например, для страницы https://www.detmir.ru/catalog/index/name/lego/ нужно заполнить так:
```
CATEGORY = 'lego'
```

4. Запустить сам скрипт 
```bash
python scrapping.py
```
5. По окончании парсинга в директории `/files` появятся файлы csv с именем формата `*категория*-*регион*.csv`. По-умолчанию парсятся регионы Москва и Санкт-Петербург.


### Для отладки

- Пример полного URL запроса
` EXAMPLE_FULL_URL https://api.detmir.ru/v2/products?filter=categories[].alias:konstruktory_wooden;promo:false;withregion:RU-SPE&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=30&offset=30&sort=popularity:desc`
- Пример итоговых параметров для подстановки к URL категории
```python
PARAMS = {
    'filter': 'categories[].alias:dishwashing;promo:false;withregion:RU-SPE',
    'expand': 'meta.facet.ages.adults,meta.facet.gender.adults,webp',
    'meta': '*&limit=30',
    'offset': 0,
    'sort': 'popularity:desc',
}
```
