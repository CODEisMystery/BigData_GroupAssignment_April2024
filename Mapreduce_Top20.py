# mapper.py

#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) < 5 or parts[0] == "userId":
        continue  # skip header
    movie_id = parts[1]
    rating = parts[2]
    title = parts[4]
    print(f'{movie_id}\t{title}\t{rating}')



# reducer.py

#!/usr/bin/env python3
import sys

current_movie_id = None
current_title = None
total_rating = 0
rating_count = 0
movie_ratings = []

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) < 3:
        continue
    movie_id, title, rating = parts
    rating = float(rating)

    if current_movie_id == movie_id:
        total_rating += rating
        rating_count += 1
    else:
        if current_movie_id:
            average_rating = total_rating / rating_count
            movie_ratings.append((average_rating, current_title))
        current_movie_id = movie_id
        current_title = title
        total_rating = rating
        rating_count = 1

if current_movie_id:
    average_rating = total_rating / rating_count
    movie_ratings.append((average_rating, current_title))

# Sort the movies by average rating and select the top 20
top_20_movies = sorted(movie_ratings, reverse=True)[:20]

# Print header
print("Top 20 highest average rating movies ")

for rating, title in top_20_movies:
    print(f'{title}\t{rating}')
