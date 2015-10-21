# This file contains the list of movies to be displayed on the movies page

import media
import fresh_tomatoes

# Create 3 movie objects
shawshank = media.movie("Shawshank Redemption",
                        "goo.gl/7Igms1",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

jurassic = media.movie("Jurassic Park",
                       "http://goo.gl/4bqgtt",
                       "www.youtube.com/watch?v=lc0UehYemQA")

insideman = media.movie("Inside Man",
                        "http://goo.gl/qdLWnh",
                        "www.youtube.com/watch?v=3WRxsmqercg")

# create a list of movies to display
movie_list = [shawshank, jurassic, insideman]

# Open movie page with created list
fresh_tomatoes.open_movies_page(movie_list)
