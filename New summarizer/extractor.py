import  requests
from bs4 import BeautifulSoup

def get_news(URL):
    response = requests.get(URL)
    header = {
        'Accept-Language': "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    news = soup.find(class_="story_details").get_text()
    return news

 
