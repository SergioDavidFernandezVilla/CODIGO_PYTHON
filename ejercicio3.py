from bs4 import BeautifulSoup
import requests

url = "https://somoskudasai.com/noticias/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# extraer titulos
article = soup.find("article", class_="ar por")
titulos = soup.find_all()
for titulo in titulos:
    print(titulo.text)