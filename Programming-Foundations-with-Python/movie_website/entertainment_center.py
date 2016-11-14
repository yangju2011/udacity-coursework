import media #previous python file, use class from a filename
import fresh_tomatoes

# toy_story = media.Movie("Toy Story", "Toy comes to life", "http://media.comicbook.com/uploads1/2015/03/group-disney-announces-toy-story-4-is-happening-126226.jpeg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# similar to turtle.Turtle(), initialize an object
# init is constructor, and gets called
# self is the instance

# print (toy_story.storyline)

# toy_story.show_trailor() #instance.function(), will open the webbrowser

# avatar = media.Movie("Avatar", "Aliens on earth", "poster-link", "trailer-url")

# print (avatar.storyline)


captain_america = media.Movie("Captain America", "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.", "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=dKrVegVI0Us")
suicide_squad = media.Movie("Suicide Squad", "A secret government agency recruits imprisoned supervillains to execute dangerous black ops missions in exchange for clemency.", "http://ia.media-imdb.com/images/M/MV5BMjM1OTMxNzUyM15BMl5BanBnXkFtZTgwNjYzMTIzOTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=fyJH39ZbPAg")
a_space_odyssey = media.Movie("2001: A Space Odyssey", "Humanity finds a mysterious, obviously artificial object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.", "http://ia.media-imdb.com/images/M/MV5BNDYyMDgxNDQ5Nl5BMl5BanBnXkFtZTcwMjc1ODg3OA@@._V1_UY268_CR9,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=lfF0vxKZRhc")
a_clockwork_orange = media.Movie("A Clockwork Orange", "In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society's crime problem - but not all goes according to plan.", "http://ia.media-imdb.com/images/M/MV5BMTY3MjM1Mzc4N15BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=xHFPi_3kc1U")
inception = media.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=8hP9D6kZseM")
three_idiots = media.Movie("3 Idiots", "Two friends looking for a lost buddy deal with a forgotten bet, a wedding they are forced to crash and an out of control funeral.", "http://ia.media-imdb.com/images/M/MV5BMTMyOTg0ODQ1OF5BMl5BanBnXkFtZTcwNjc0NTMwNQ@@._V1_UY268_CR3,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=xvszmNXdM4w")
zootopia = media.Movie("Zootopia", "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.", "http://ia.media-imdb.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=jWM0ct-OLsM")
begin_again = media.Movie("Begin Again", "A chance encounter between a disgraced music-business executive and a young singer-songwriter new to Manhattan turns into a promising collaboration between the two talents.", "http://ia.media-imdb.com/images/M/MV5BNjAxMTI4MTgzMV5BMl5BanBnXkFtZTgwOTAwODEwMjE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=uTRCxOE7Xzc")

movies = [captain_america, suicide_squad, a_space_odyssey, a_clockwork_orange, inception, three_idiots, zootopia, begin_again]

fresh_tomatoes.open_movies_page(movies)

print (media.Movie.VALID_RATINGS) # use class to get access to the list, share the list

# print (media.Movie.__doc__) # will show """ quote information 

# print (media.Movie.__name__) # will show  Movie, which is the class name

# print (media.Movie.__module__) # will show filename (module), which is media 
