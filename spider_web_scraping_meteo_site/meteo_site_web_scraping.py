import requests
from bs4 import BeautifulSoup
import json


# create a function that crawl to an specify url after the cities and its specific meteor information
def weather_in_RO():
    url = 'https://www.meteoromania.ro/vremea/starea-vremii-romania/'
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'lxml')

    # create a variable that looks after a selector
    city_list_selection = soup.select('select[name="statie"] > option')

    # using a list comprehensive to extract the text
    city_list = [city.text for city in city_list_selection]
    new_list = city_list.pop(0)

    # another methode to extract the name and its afferent info
    # city_list_li = soup.body.findAll('ul', {'class': 'slides'})
    # city_list = [city.text for city in city_list_li]

    # create a variable that looks after the city info
    city_info_div = soup.body.findAll('div', {'class': 'text'})

    # using a list comprehensive to extract the text
    city_info = [info.text for info in city_info_div]

    extracted_info = dict(zip(city_list, city_info))

    json_object = json.dumps(extracted_info)

    # write in JL file
    with open('InfoScraped.jl', 'w', encoding='utf-8') as f:
        for k, v in extracted_info.items():
            json.dump({k: v}, f, ensure_ascii=False, indent=4)
            f.write('\n')


if __name__ == '__main__':
    weather_in_RO()
