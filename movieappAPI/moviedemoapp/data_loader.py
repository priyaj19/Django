import json

def load_movie_data():
    with open('moviedemoapp/movie1.json') as file:
        movie_data=json.load(file)
    return movie_data

