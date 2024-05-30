import requests


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'
    API_KEY = 'apiKey=f64765660c394c1781fbcc5fafe717ad'

    def __init__(self, interest: str, from_date: str, to_date: str, language: str='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles[:5]:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles: list[dict] = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.API_KEY}'
        return url


if __name__ == '__main__':
    news_feed = NewsFeed(interest='nasa', from_date='2024-05-20', to_date='2024-05-27', language='en')
    print(news_feed.get())
