import webbrowser

class movie():
    """This class provides a way to store movie related information"""
    
    # Set the values of an instance of the "movie" class    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

