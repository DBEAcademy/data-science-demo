import requests
from bs4 import BeautifulSoup
#write the output to html file with Python BeautifulSoup
url = "https://www.dbe.academy/"
get_url = requests.get(url)
get_text = get_url.text
soup = BeautifulSoup(get_text, "html.parser")

company = soup.select('h1')

print(get_text)
print(company)


with open("output1.html", "w") as file:
    file.write(str(soup))
