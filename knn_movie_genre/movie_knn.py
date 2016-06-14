from math import sqrt
from operator import itemgetter

from knn_movie_genre import movie


def calc_square_root_distance(sample_movie, m2bc):
    sqrt_distance = sqrt(
        (sample_movie.kisses - m2bc.kisses) ** 2
        + (sample_movie.kicks - m2bc.kicks) ** 2
    )
    return (sample_movie, sqrt_distance)  # returns a tuple


# sample data
sample_data = [movie.movie("California Man", 3, 104, "Romance"),
               movie.movie("He's not reall into dudes", 2, 100, "Romance"),
               movie.movie("Beautiful Woman", 1, 81, "Romance"),
               movie.movie("Kevin Longblade", 101, 10, "Action"),
               movie.movie("Robo Slayer 3000", 99, 5, "Action"),
               movie.movie("Amped", 98, 2, "?")
               ]

# movie to be classified
m2bc = movie.movie("?", 18, 90, "?")

# create an empty list to store the distances
distances = []

# calculate the distance from to unknown film to all the others
for movie in sample_data:
    # calculate the square-root distance between als Xi's and the actual point
    distances.append(calc_square_root_distance(movie, m2bc))

# sort the list
sorted_distances = sorted(distances, key=itemgetter(1))

# print the sorted list
for elem in sorted_distances:
    print(elem)

# Define a k (the k from KNN). This k is, at how many film you want to look.
# k should be smaller than the sample size to kick out outliers.
# Bug big enough to get a good vote!
K = 4

# Count the genres and derive a vote
candidates = list(map(itemgetter(0), sorted_distances[:K]))

# create an empty directory:
genre_count = {}

for elem in candidates:
    genre = elem.genre
    if genre not in genre_count:
        genre_count[genre] = 1
    else:
        genre_count[genre] += 1

nearest_genre = max(genre_count, key=lambda i: genre_count[i])

# Apply the voting results to the unknown film
m2bc.genre = nearest_genre
print("\nGenre '" + nearest_genre + "' has been added to '" + m2bc.title
      + "'! Check next line:\n" + str(m2bc))
