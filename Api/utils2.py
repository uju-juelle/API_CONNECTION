from decouple import config
# import requests

# endpoint = "https://newsdata.io/api/1/news?country=ng&apikey=pub_config('pub')"

# response = requests.get(endpoint)

# print(response.json())

news_dictionary = {'status': 'success', 'totalResults': 753, 'results': [{'title': 'Wikipedia Censors Drug Dealer Information On Tinubu Page – Hundeyin Reports', 'link': 'https://www.herald.ng/wikipedia-censors-drug-dealer-information-on-tinubu-page-hundeyin-reports/', 'keywords': ['News', 'Politics', 'Bola Tinubu', 'David Hundeyin', 'Wikipedia'], 'creator': ['John Ogunsemore'], 'video_url': None, 'description': 'Award-winning journalist, David Hundeyin says President Bola Tinubu’s Wikipedia page has been edited to downplay his drug dealing allegations. One of the most visited sites globally, Wikipedia is a free online encyclopedia created and edited by volunteers around the world. It is a top source of information about prominent people and events. In a tweet, […] The post Wikipedia Censors Drug Dealer Information On Tinubu Page – Hundeyin Reports appeared first on ..', 'content': 'Award-winning journalist, David Hundeyin says President Bola Tinubu’s Wikipedia page has been edited to downplay his drug dealing allegations. One of the most visited sites globally, Wikipedia is a free online encyclopedia created and edited by volunteers around the world. It is a top source of information about prominent people and events. In a tweet, Hundeyin said that the Wikipedia page of Tinubu, who was inaugurated as Nigeria’s president on Monday, had been edited and a drug trafficking section in his entry merged with the nondescript “Allegations of corruption” header. Hundeyin, who has been a ferocious Tinubu critic, said that the editing was done by a super-editor at Wikipedia, “Morbidthoughts”.” “Hi @Wikipedia, your super-editor “Morbidthoughts” who has spent months vandalising my Wikipedia page, has also recently removed the drug trafficking section in Bola Ahmed Tinubu’s entry, and merged it with the nondescript “Allegations of corruption” header. “Kindly explain why,” the journalist tweeted. Hi @Wikipedia , your super-editor "Morbidthoughts" who has spent months vandalising my Wikipedia page, has also recently removed the drug trafficking section in Bola Ahmed Tinubu\'s entry, and merged it with the nondescript "Allegations of corruption" header. Kindly explain why. pic.twitter.com/XXfKYAZqx7 — David Hundeyin (@DavidHundeyin) May 29, 2023 He added, “I am aware that undisclosed paid editing is supposed to earn any Wikipedia editor a lifetime ban from editing, and I have also raised my concerns about this particular editor with the Nigerian Wikipedia community, to no effect. “Why is this editor still active on your platform?”', 'pubDate': '2023-05-30 07:54:11', 'image_url': None, 'source_id': 'herald', 'category': ['politics'], 'country': ['nigeria'], 'language': 'english'}]}

# print(news_dictionary["results"])

# print(news_dictionary['results'][0])

# print(news_dictionary['results'][0]['title'])


api_news_title = news_dictionary['results'][0]['title']

api_news_creator = news_dictionary['results'][0]['creator']

api_news_full_description = news_dictionary['results'][0]['description']

api_news_source_id = news_dictionary['results'][0]['source_id']


# print(api_news_title, api_news_creator, api_news_full_description, api_news_source_id)

import requests
# from Api.models import News

# endpoint = "http://127.0.0.1:8000/api/"

# response = requests.post(endpoint, data={"title":api_news_title, "content":api_news_full_description, "author":api_news_creator, "source":api_news_source_id})

# print(response.json())

# News.objects.create(title=api_news_title, content=api_news_full_description, author=api_news_creator, source=api_news_source_id)

endpoint = "https://newsdata.io/api/1/news?country=ng&apikey=pub_{config}('pub')"

response = requests.get(endpoint)
news_dictionary = dict(response.json())

print(response.json())

for i in range(0,5):   
    api_news_title = news_dictionary['results'][i]['title'] 
    api_news_creator = news_dictionary['results'][i]['creator']
    api_news_full_description = news_dictionary['results'][i]['description']
    api_news_source_id = news_dictionary['results'][i]['source_id']

    endpoint = "http://127.0.0.1:8000/api/"


    response = requests.post(endpoint, data={"title":api_news_title, "content":api_news_full_description, "author":api_news_creator, "source":api_news_source_id})

