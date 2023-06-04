import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt


URL = "https://netco.kg"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="product-wrap")
    netco_elektronika = []

    for item in items:
        netco_elektronika.append(
            {
                "title_url": URL + item.find("div", class_="static").find("a").get("data-url"),
                "title_text": item.find(class_="name").get_text(),
                "image": URL + item.find("img").get("src"),
                "price": item.find('div', class_='price').get_text(),

            }
        )

    return netco_elektronika


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        netco_elektronika1 = []
        for page in range(0, 1):
            html = get_html(f"https://netco.kg/catalog/mobilnye_telefony_i_aksessuary/", params=page)
            netco_elektronika1.extend(get_data(html.text))
        return netco_elektronika1
        # print(f'\n{netco_elektronika1}\n')

    else:
        raise Exception("Parse Error......")


# parser()