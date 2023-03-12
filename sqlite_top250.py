import time
import sqlite3

class Movies():
    def __init__(self,movie,imdb,year):
        self.movie = movie
        self.imdb = imdb
        self.year = year

    def __str__(self):
        return f"Movie: {self.movie}\nİmdb: {self.imdb}\nYear: {self.year}"

class List():
    def __init__(self):
        self.connect()

    def connect(self):
        self.connect = sqlite3.connect("top250.db")

        self.cursor = self.connect.cursor()

        self.cursor.execute("Create table if not exists top250 (movie TEXT,imdb REAL,rate REAL)")  # datebase created
        self.connect.commit()

    def connect_end(self):
        self.connect.close()

    def informations(self):
        sorgu = "Select * from top250"

        self.cursor.execute(sorgu)

        movies = self.cursor.fetchall()

        if(len(movies) == 0):
            print("Db have not movie!!")
        else:
                for i in movies:
                    movie = Movies(i[0],i[1],i[2])
                    print(movie)


    def movie_add(self,movie):
        sorgu = "Insert into top250 Values(?,?,?)"

        self.cursor.execute(sorgu,(movie.movie,movie.imdb,movie.year))

        self.connect.commit()

    def movie_query(self,movie):
        sorgu = "Select * from top250 where movie = ?"

        self.cursor.execute(sorgu,(movie,))

        movies = self.cursor.fetchall()

        if(len(movies) == 0):
            print("Db dont have any movie")
        else:
            mv = Movies(movies[0][0],movies[0][1],movies[0][2])
            print(mv)

    def delmovie(self,movie):
        sorgu = "Delete from top250 where movie = ?"

        self.cursor.execute(sorgu,(movie,))

        self.connect.commit()

    def numberofmovie(self):
        sorgu = "Select * from top250"

        self.cursor.execute(sorgu)

        movies = self.cursor.fetchall()

        if(len(movies) == 0):
            print("Db dont have any movie")
        else:
            meter = 0
            for i in movies:
                meter += 1
            print(f"There are {meter} movies in the DB")










