# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

#import sys
#sys.path.append(r"C:\Users\Seth\iCloudDrive\Udacity\IPND\Lesson3")

#import os
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

obrother = media.Movie("O Brother Where Art Thou",
                        "A man wanders home to his wife",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/5/5b/O_brother_where_art_thou_ver1.jpg/220px-O_brother_where_art_thou_ver1.jpg", # noqa
                        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

#Create a list of "Movie objects" to be passed into the fresh tomatoes function
movies = [toy_story,avatar,obrother]

'''
Pass in the list of movies into the open_movies_page method in the 
fresh_tomatoes class. Opens a web page that will display the poster
for each movie in the list, and will make the posters clickable so that
clicking on them opens a link to that movie's trailer on YouTube.
'''
fresh_tomatoes.open_movies_page(movies)

