import requests 
from bs4 import BeautifulSoup
f = open("quotes.pdf", "a")
for quotes in BeautifulSoup(requests.get("https://parade.com/937586/parade/life-quotes/").text, 'html.parser').find_all('p'):
    None if (quotes.get_text().find('.') == -1) else f.write(quotes.get_text()[quotes.get_text().index('.')+2:] + "\n") if (quotes.get_text()[0:quotes.get_text().index('.')].isdigit()) else None