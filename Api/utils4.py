import requests
from decouple import config

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": config('movie_key')
}

response = requests.get(url, headers=headers)

print(response.text)


# a = {"page":1,"results":[{"adult":"false","backdrop_path":"/h8gHn0OzBoaefsYseUByqsmEDMY.jpg","genre_ids":[28,53,80],"id":603692,"original_language":"en","original_title":"John Wick: Chapter 4","overview":"With the price on his head ever increasing, John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into foes.","popularity":4242.15,"poster_path":"/vZloFAK7NmvMGKE7VkF5UHaz0I.jpg","release_date":"2023-03-22","title":"John Wick: Chapter 4","video":"false","vote_average":7.9,"vote_count":2723}]}

# title = a["results"][0]["original_title"]

# content = a["results"][0]["overview"]

# rating = a["results"][0]["popularity"]


# Movies.objects.create(title=title, content=content, rating=rating)


# print(a["results"][0])


