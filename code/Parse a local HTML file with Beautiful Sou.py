from bs4 import BeautifulSoup

with open("output1.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
