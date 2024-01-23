# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Python Projects/Sample Projects/Movie Reccomendation/movies.db'
# Bootstrap(app)
# db = SQLAlchemy(app)

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     movie_id = db.Column(db.Integer)
#     title = db.Column(db.String(250), unique=False, nullable=False)
#     year = db.Column(db.Integer, unique=False, nullable=False)
#     overview = db.Column(db.String(250), unique=False, nullable=False)
#     review = db.Column(db.String(250), unique=False, nullable=False)
#     img_url = db.Column(db.String, unique=True, nullable=False)

# with app.app_context():
#     db.create_all()



# class AddMovie(FlaskForm):
#      movie_title = StringField('Movie Title', validators=[DataRequired()])

# api_key_tmdb = "11d2517a2127bf5caf2461cdb7063868"

# #URL FOR DATA 
# base_url = 'https://api.themoviedb.org/3/movie/now_playing'
# 
# params = {"api_key": api_key_tmdb}

# response = requests.get(base_url, params=params)
# movie_title = response.json()

# random_movies = random.sample(movie_title['results'], 12)
# all_movies = []
# for movie in random_movies:
#     movie_id = movie['id']
#     title = movie['title']
#     year = movie['release_date']
#     poster_path = movie['poster_path']
#     overview = movie['overview']
#     formatted_img_url = f"https://image.tmdb.org/t/p/w400{poster_path}"
#     data_movie = {
#         "title": title,
#         "year": year,
#         "poster": formatted_img_url,
#         "overview": overview,
#     }
#     all_movies.append(data_movie)
@app.route("/add")
def add():
    form = AddMovie()
    return render_template("add.html", form=form)


@app.route("/search", methods=['GET', 'POST'])
def search():
    movie = request.form.get('movie-tv')
    response = requests.get(movie_search_url, params={"api_key": api_key_tmdb, "query": movie})
    data = response.json()['results']
    return render_template("movie_search.html", movies=data)
  