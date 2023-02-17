import requests
from bs4 import BeautifulSoup

url = "https://www.dbe.academy/"
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, "html.parser")

company = soup.select('h1')

print(get_text)
print(company)
