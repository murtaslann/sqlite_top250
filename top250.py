from sqlite_top250 import *
import time

list = List()

print("""
TOP250 MOVİE DATABASE;

1. List Movies

2. Add Movie

3. Query Movie

4. Delete Movie

5. Number Of Movies

İf want quit write 'quit'!!
""")

while True:
    transaction = input("Transaction: ")

    if(transaction == "quit" and "Quit" and "QUİT"):
        print("Exit is in progress!!")
        time.sleep(1)
        print("Good Bye!")
        break
    elif(transaction == "1"):
        list.informations()
    elif (transaction == "2"):
        movie = input("Movie Name: ")
        imbd = float(input("İmbd: "))
        year = int(input("Year of capture:"))

        print("Movie Adding,Please Wait...")
        MV = Movies(movie,imbd,year)
        time.sleep(1)
        list.movie_add(MV)
        print("Movie Added!")

    elif (transaction == "3"):
        movie = input("Which movie do you want to question?")

        print("Movie in query.. Please Wait!")
        time.sleep(1)
        list.movie_query(movie)

    elif (transaction == "4"):
        movie = input("Which movie want you delete? ")
        answer = input("Are you sure? (y/n)")

        if (answer == "n"):
            print("deletion canceled!!")
        else:
            print("The movie is being deleted!")
            time.sleep(1)
            list.delmovie(movie)
            print("Deleted the movie..")

    elif (transaction == "5"):
        list.numberofmovie()
    else:
        print("Invalid process!")




