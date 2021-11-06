import json
import requests
from bs4 import BeautifulSoup


# create a function that crawl to an specify url after the movies with a specific rating
def get_movies(max_number_of_pages):
    page = 1
    while page <= max_number_of_pages:
        url = 'https://www.cinemagia.ro/filme/?&pn=' + str(page)
        source_code = requests.get(url)
        soup = BeautifulSoup(source_code.content, 'lxml')

        # create a variable that search for titles 
        movies_title_div = soup.find_all('div', {'class': 'title'})

        # using a list comprehensive to extract the text
        movies = [movie.text.strip('\n')[0:movie.text.strip('\n').find('\n')] for movie in movies_title_div]
        movies_imdb = movies.pop(-1)

        # create a variable that search for the ratings 
        rating_imdb_div = soup.find_all('div', {'class': 'rating'})

        # using a list comprehensive to extract the float number of the rating
        rating_imdb = [float(rating.text.strip('\n')[rating.text.strip('\n').find(' ') + 1:]) for rating in
                       rating_imdb_div]
        movies_dictionary = dict(zip(movies, rating_imdb))

        json_object = json.dumps(movies_dictionary)

        # write in JL file
        with open('MoviesWithGoodRating.jl', 'a', encoding='utf-8') as f:
            for k, v in movies_dictionary.items():
                if v >= 9:
                    json.dump({'Movie': k, 'Rating': v}, f, ensure_ascii=False, indent=1)
                    print(f'Movie: {k} : IMDB Rating: {v}')
                    f.write('\n')
        page += 1


if __name__ == '__main__':
    get_movies(50)
