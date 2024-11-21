import json
import requests
from bs4 import BeautifulSoup

url = 'https://somoskudasai.com/noticias/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos los artículos
articles = soup.find_all('article', class_='ar por')

# Crear una lista con los artículos
articles_data = []

for article in articles:
    # Obtener el título y la URL
    title = article.find('h2', class_='ar-title white-co mab fz4 lg-fz5').get_text() if article.find('h2', class_='ar-title white-co mab fz4 lg-fz5') else 'No title'
    article_url = article.find('a')['href'] if article.find('a') else 'No URL'

    # Intentar obtener la fecha de creación
    contenedor_fecha = article.find('div', class_="ar-mt white-co fz3")
    fecha_create = contenedor_fecha.find('span', class_="db op5").get_text() if contenedor_fecha and contenedor_fecha.find('span') else 'No Date'

    # Conseguir el tag del articulo
    tag = article.find('span', class_ = "typ ttu fwb fz2 white-bg primary-co brd1 dib pdx1 mab").get_text()

    # Intentar obtener la imagen asociada al artículo
    img_tag = article.find('figure', class_='im brd1 black-bg z1')
    img_url = img_tag.find('img')['src'] if img_tag and img_tag.find('img') else None
    
    # Crear el diccionario con los datos
    article_data = {
        'title_post': title,
        'url_post': article_url,
        'img_post': img_url,
        'tag_post': tag,
        'fecha_created_post': fecha_create
    }
    
    articles_data.append(article_data)

# Guardar los datos en un archivo JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles_data, f, ensure_ascii=False, indent=4)

print("Datos guardados en articles.json")
