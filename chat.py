import requests 
import random

actor_search_url = 'https://api.themoviedb.org/3/search/person'
api_key_tmdb = "11d2517a2127bf5caf2461cdb7063868"

actor_name = "Dwayne Johnson"

search_actor_url = f'https://api.themoviedb.org/3/search/person'

params = {
    'api_key': api_key_tmdb,
    'query': actor_name,
}

response_discover = requests.get(search_actor_url, params=params)

actor_data = response_discover.json()

if 'results' in actor_data and actor_data['results']:
    actor_id = actor_data['results'][0]['id']

    discover_movies_url = f'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': api_key_tmdb,
        'with_cast': actor_id,
    }

    response = requests.get(discover_movies_url, params=params).json()

    if 'results' in response:
        random_movies = random.sample(response['results'], 20)
        all_movies = []
        for movie in random_movies:
            movie_id = movie['id']
            title = movie['title']
            year = movie['release_date']
            poster_path = movie['poster_path']
            overview = movie['overview']
            formatted_img_url = f"https://image.tmdb.org/t/p/w400{poster_path}"
            data_movie = {
                "title": title,
                "year": year,
                "poster": formatted_img_url,
                "overview": overview,
            }
            all_movies.append(data_movie)
        print(all_movies)
else:
    print("Actor not found in TMDB database.")