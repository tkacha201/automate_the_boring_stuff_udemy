import bs4, requests

def get_laptop_bg_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#features > div.product-sidebar > div.offer.preorder.update-price > div.price-container.update-price > span.price')
    return elems[0].text.strip()
    




price = get_laptop_bg_price('https://laptop.bg/laptops-apple-MacBook_Air_2020-apple_macbook_air_133_m1_november_2020_mgn73zea_z125_16GB')
print('The price is ' + price)
