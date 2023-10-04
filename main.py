import requests
from bs4 import BeautifulSoup
import re
# https://www.quote.cc/stoic-quotes/
# https://wisdomquotes.com/stoic-quotes/
url = "https://www.quote.cc/stoic-quotes/"
response = requests.get(
    url,
    headers={
        "Accept-Language":
        "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Accept-Encoding":
        "gzip, deflate",
        "Upgrade-Insecure-Requests":
        "1",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    })
soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("blockquote")
with open("quotes.txt", "a+") as file:
    for i in quotes:
        file.write(i.text + "\n")