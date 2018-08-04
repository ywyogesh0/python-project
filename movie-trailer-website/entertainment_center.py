# entertainment_center.py
# Movies list for Movie Trailer Website


import media
import fresh_tomatoes

# Inception
inception = media.Movie("Inception", "posters/inception.jpg", "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Shutter Island
shutter_island = media.Movie("Shutter Island", "posters/shutter_island.jpg",
                             "https://www.youtube.com/watch?v=YDGldPitxic")

# Mission: Impossible - Fallout (2018)
mission_impossible = media.Movie("Mission: Impossible - Fallout (2018)", "posters/mission_impossible.jpg",
                                 "https://www.youtube.com/watch?v=wb49-oV0F78")

# Now You See Me
now_you_see_me = media.Movie("Now You See Me", "posters/now_you_see_me.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

# Se7en
se7en = media.Movie("Se7en", "posters/se7en.jpg", "https://www.youtube.com/watch?v=znmZoVkCjpI")

# Avengers Infinity War
avengers = media.Movie("Avengers Infinity War", "posters/avengers.jpg", "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Movie instance list
movies_list = [inception, shutter_island, mission_impossible, now_you_see_me, se7en, avengers]

# Opening Movies Trailer Web Page
fresh_tomatoes.open_movies_page(movies_list)
