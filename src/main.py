import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://godvillegame.com/login"
    
    # Get URL content
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())