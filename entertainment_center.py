import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
avatar = media.Movie ("Avatar",
                      "A marine on an alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

jurassic_park = media.Movie ("Jurassic Park",
                             "Dinosaurs wreak havoc when they escape",
                             "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                             "https://www.youtube.com/watch?v=lc0UehYemQA")
#print(jurassic_park.storyline)

movies = [toy_story, avatar, jurassic_park]

fresh_tomatoes.open_movies_page(movies)
