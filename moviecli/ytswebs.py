import requests
from bs4 import BeautifulSoup
from config import Config as c


def search_movie(movie, quality, genre, year, rating, language, order_by):
    url = c.SEARCH_URL
    payload = {
        "keyword": movie,
        "quality": quality,
        "genre": genre,
        "rating": rating,
        "year": year,
        "language": language,
        "order_by": order_by
    }

    response = requests.post(url, data=payload)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    browse_content = soup.find_all('div', class_='browse-content')[0]
    rows_div = browse_content.find_all('div', class_='row')[0]
    search_result = rows_div.find_all('div', recursive=False)

    results = []

    for div in search_result:
        bmt = div.find('a', class_='browse-movie-title')
        result_title = bmt.text
        result_link = bmt['href']
        result_cover = div.find('img', class_='img-responsive')['src']
        result_year = div.find('div', 'browse-movie-year').text
        result = (result_title, result_link, result_cover, result_year)
        results.append(result)
    
    return results




