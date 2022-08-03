CATEGORY = 'dishwashing'  # Заполнить алиас нужной категории
REGIONS = ['RU-MOW', 'RU-SPE']
FIELDNAMES = ['id', 'title', 'price', 'promo_price', 'url']


FILTER_VALUES = {
    'promo': 'false',
}
REQUEST_PARAMS = {
    'expand': 'meta.facet.ages.adults,meta.facet.gender.adults,webp',
    'meta': '*&limit=30',
    'offset': 0,
    'sort': 'popularity:desc',
}
PRODUCTS_PER_PAGE = 30
BASE_URL = 'https://api.detmir.ru/v2/products'
COOKIES = {}
HEADERS = {
    'authority': 'api.detmir.ru',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.detmir.ru',
    'referer': 'https://www.detmir.ru/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'detmir-ui',
}
