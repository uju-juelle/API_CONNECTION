import requests


home_page_endpoint = "http://127.0.0.1:8000/api/"

# response = requests.get(home_page_endpoint)

# print(response.text)


POST_DATA = {
    "title": "Blog post 1",
    "content": "Blog post 2",
    "author": "ina",
    "source": "channels"}


new_post = requests.post(home_page_endpoint, data=POST_DATA)

print(new_post.json())