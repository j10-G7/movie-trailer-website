import fresh_tomatoes
import media

# Create instances of class "movie". Each object will contain information about a movie -
# the movie's title, storyline (description), the url of a poster image, and the url of a youtube video.

harvey = media.movie("Harvey",
                     "James Stewart, and his 6-foot rabbit named Harvey",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/6/69/Harvey_1950_poster.jpg/220px-Harvey_1950_poster.jpg",
                     "https://www.youtube.com/watch?v=hBvpxzl54D8")

mary_poppins = media.movie("Mary Poppins",
                           "A strict but wonderful nanny",
                           "http://ia.media-imdb.com/images/M/MV5BMTY1MDQwNTM3Ml5BMl5BanBnXkFtZTgwNzA3ODg3MDE@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=5BHoDW9f7vY")

music_man = media.movie("The Music Man",
                        "A travelling salesman stirs up River City, Iowa",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Original_movie_poster_for_the_film_The_Music_Man_1962.jpg/220px-Original_movie_poster_for_the_film_The_Music_Man_1962.jpg",
                        "https://www.youtube.com/watch?v=y_IAI1xIjAI")

my_dinner_with_andre = media.movie("My Dinner With Andre",
                                   "Two men talk about the meaning of life",
                                   "http://upload.wikimedia.org/wikipedia/en/thumb/a/a5/My_Dinner_with_Andre_1981_film_theatrical_release_poster.jpg/220px-My_Dinner_with_Andre_1981_film_theatrical_release_poster.jpg",
                                   "https://www.youtube.com/watch?v=Y7BI3bvNKdU")

sound_of_music = media.movie("The Sound of Music",
                             "A nanny of seven grows to love her charges",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Sound_of_music.jpg/220px-Sound_of_music.jpg",
                             "https://www.youtube.com/watch?v=xIjobdArtiA")

titanic = media.movie("Titanic (1953)",
                      "1953 movie about the Titanic - very powerful!",
                      "http://upload.wikimedia.org/wikipedia/en/f/f2/Titanic_1953_film.jpg",
                      "https://www.youtube.com/watch?v=B0TxAyqApRk")

# Set variable "movies" to a list of the objects that we just created
movies = [harvey, mary_poppins, music_man, my_dinner_with_andre, sound_of_music, titanic]

# fresh_tomatoes.py contains a function called open_movies_page().
# open_movies_page() accepts a list of movie objects.
# It creates or replaces a web page called fresh_tomatoes.html,
# which contains information about the movies.
# We will now call open_movies_page(), sending it the list of movie objects.
fresh_tomatoes.open_movies_page(movies)
