import requests
import random
from flask import Flask, render_template , request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from manager import MovieManager


app = Flask(__name__)
movie_manager = MovieManager()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route("/")
def home():
    all_movies = movie_manager.movies_now_playing()
    popular_movies = movie_manager.movies_by_popularity()
    upcoming_movies = movie_manager.upcoming_movie()

    return render_template('index.html', all_movies=all_movies, popular_movies=popular_movies, upcoming_movies=upcoming_movies)


@app.route("/add")
def add():
    movie_title = request.form.get('movie-tv')
    return render_template ("add.html", movie_title=movie_title)

@app.route("/search", methods=['GET', 'POST'])
def search_movie():
    movie_title = request.form.get("movie-tv")
    movies = movie_manager.search_movie(movie_title)
    return render_template("movie_search.html", movies=movies)

@app.route("/search_by_actor", methods=['GET', 'POST']) 
def search_movie_actor():
    actor_name = request.form.get('actor-name')
    movies = movie_manager.movies_by_actor(actor_name)
    return render_template ("movie_search.html", movies=movies)

@app.route("/genre-search/", methods=['GET', 'POST'])
def genre_search():
    genre = request.args.get('genre')
    if genre is not None:
        movies = movie_manager.movies_by_genre(user_genre=genre)
        return render_template("movie_search.html", movies=movies)
    else:
        return "Genre is None"
    

@app.route("/search-by-year", methods=['GET', 'POST'])
def year_search():
    year = request.args.get('year')
    print(year)
    movies = movie_manager.movies_by_year(year=year)
    return render_template("movie_search.html", movies=movies)



@app.route("/about-movie", methods=['GET', 'POST'])
def about_movie():
    movie_id = request.args.get('id')
    return redirect(url_for('movie_details', id=movie_id))

@app.route("/movie-details")
def movie_details():
    movie_id = request.args.get('id')
    # Retrieve movie details based on the movie_id
    movie_details = movie_manager.get_movie_by_id(movie_id)
    return render_template("about_movie.html", movie_details=movie_details)


if __name__ == "__main__":
    
    app.run(debug=True)