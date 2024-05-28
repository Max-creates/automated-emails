import requests


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'
    API_KEY = 'apiKey=f64765660c394c1781fbcc5fafe717ad'

    def __init__(self, interest: str, from_date: str, to_date: str, language: str):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'https://newsapi.org/v2/everything?'\
              f'qInTitle={self.interest}&'\
              f'from={self.from_date}&'\
              f'to={self.to_date}&'\
              f'language={self.language}&'\
              f'{self.API_KEY}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles[:5]:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

news_feed = NewsFeed(interest='nasa', from_date='2024-05-20', to_date='2024-05-27', language='en')
print(news_feed.get())
