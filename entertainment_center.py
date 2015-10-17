# This file contains the list of movies to be displayed on the movies page

import media
import fresh_tomatoes

# Create 3 movie objects
shawshank = media.movie("Shawshank Redemption",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

jurassic = media.movie("Jurassic Park",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcT9t_mvZu0k-wS_QqvQmPKc6FMkwJoj0HgUjwLJK7uGG_NtZBxV",
                       "www.youtube.com/watch?v=lc0UehYemQA")

insideman = media.movie("Inside Man",
                        "http://www.gstatic.com/tv/thumb/movieposters/159788/p159788_p_v7_aa.jpg",
                        "www.youtube.com/watch?v=3WRxsmqercg")

#create a list of movies to display
movie_list = [shawshank, jurassic, insideman]

#Open movie page with created list
fresh_tomatoes.open_movies_page(movie_list)
