from bs4 import BeautifulSoup
with open("jon.html") as html:
    print(type(html))
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', {"id": "about"})
    print(divs)