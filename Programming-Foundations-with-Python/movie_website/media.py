import webbrowser

class Movie():
    """
    This is to store movie information.
    """
    # get access through __doc__
    
    # class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] # it is a constant, use all caps

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # two underscores, special functions exist in python
        # self is self object, self is toy story, it has to be intialized in every class 

        # instance variables, not local variable
        self.title = movie_title 
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance methods
    def show_trailor(self): #take self as input within the class
        webbrowser.open(self.trailer_youtube_url) # open the url, string, should use self. to recall the code

# titanic = media.Movie('titanic','boat sink','url','url')

