import requests
import os
import random


#API KEY
api_key_tmdb = "11d2517a2127bf5caf2461cdb7063868"


#URLs
base_url = 'https://api.themoviedb.org/3/movie/now_playing'
genre_url = 'https://api.themoviedb.org/3/genre/movie/list'
search_actor_url = f'https://api.themoviedb.org/3/search/person'
movie_id_url = "https://api.themoviedb.org/3/movie/"
#PARAMETERS
params = {"api_key": api_key_tmdb}

def get_movie(response):
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
        return all_movies

    else:
        print("No results found in the API response.")
        return []

class MovieManager():

    def __init__(self):
        pass

    

    def search_movie(self, movie_title):
        movie_search_url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(movie_search_url, params={"api_key": api_key_tmdb, "query": movie_title}).json()
        search_data = response['results']
        return search_data
    
    def get_movie_by_id(self, movie_id):
        url = f'{movie_id_url}{movie_id}?api_key={api_key_tmdb}'
        response = requests.get(url).json()
        movie_data = get_movie(response)
        return movie_data




    def movies_now_playing(self):
        response = requests.get(base_url, params=params)
        movie_title = response.json()
        print(movie_title)
        movie_data = get_movie(response=movie_title)
        return movie_data

    def movies_by_genre(self, user_genre):
        
        user_genre = user_genre.capitalize()

        sci_fi = user_genre.split()
        if len(sci_fi) == 2:
            user_genre = user_genre.title()

        #List of genres from TMDb
        response_genre = requests.get(genre_url, params=params)
        genre_data = response_genre.json()
        genre_id = None

        #Finding the genre Id based on user's input
        for genre in genre_data['genres']:
            if genre['name'] == user_genre:
                genre_id = genre['id']
                break

        if genre_id is not None:
            #Fetching movies on genre
            genre_movies_url = 'https://api.themoviedb.org/3/discover/movie'
            genre_params = {"api_key": api_key_tmdb, "with_genres": genre_id}
            response_genre_movies = requests.get(genre_movies_url, genre_params)
            genre_movie_data = response_genre_movies.json()
            
            #Get random movies from genre specific list
            if 'results' in genre_movie_data:
                movie_data = get_movie(response=genre_movie_data)
                return movie_data
            else:
                print(f"No results found for the genre: {user_genre}")

        else:
             print(f"Genre not found: {user_genre}")



    def movies_by_actor(self, actor_name):
        actor_name = actor_name.title()
        actor_params = {
            "api_key": api_key_tmdb,
            "query": actor_name
        }
        response_discover = requests.get(search_actor_url, params=actor_params)
        actor_data = response_discover.json()
        if 'results' in actor_data and actor_data['results']:
            actor_id = actor_data['results'][0]['id']

            discover_movies_url = f'https://api.themoviedb.org/3/discover/movie'
            params = {
                'api_key': api_key_tmdb,
                'with_cast': actor_id,
            }
            response = requests.get(discover_movies_url, params=params).json()
            movie_data = get_movie(response)
            return movie_data

    def movies_by_year(self, year):
        discover_url = "https://api.themoviedb.org/3/discover/movie"
        user_year = year
        year_params = {
            "api_key": api_key_tmdb,
            "primary_release_year":user_year
        }

        response = requests.get(discover_url, params=year_params).json()
        movie_data = get_movie(response=response)
        return movie_data
                
    def movies_by_popularity(self):
        url = "https://api.themoviedb.org/3/movie/popular"
        response =requests.get(url, params=params).json()
        movie_data = get_movie(response=response)
        return movie_data

    def movies_by_top_rating(self):
        url ="https://api.themoviedb.org/3/movie/top_rated"
        response =requests.get(url, params=params).json()
        movie_data = get_movie(response=response)
        return movie_data

    def upcoming_movie(self):
        url = "https://api.themoviedb.org/3/movie/upcoming"
        response = requests.get(url, params=params).json()
        movie_data = get_movie(response=response)
        return movie_data

man = MovieManager()
data  = man.get_movie_by_id(movie_id=230)

