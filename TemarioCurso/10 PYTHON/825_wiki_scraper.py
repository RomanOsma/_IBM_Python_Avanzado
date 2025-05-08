from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scrape_url(url: str):
  headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    print('La petición fue exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer todos los
    titulos = [titulo.string for titulo in soup.find_all('h1')]
    # print(titulos)

    # Extraer todos los enlaces <a>
    enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]
    # print(enlaces)

    # extraer todo el contenido de la página de texto
    # all_text = soup.get_text()
    # print(all_text)

    # extraer el texto del elemento main
    # main_text = soup.find('main').get_text()
    # print(main_text)

    # extraer de la id mw-content-text
    # content_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
    # print(content_text)

    # extrar el open graph si existe
    # og_image = soup.find('meta', {'property': 'og:image'})
    
    og_image = soup.find('meta', property='og:image')
    if og_image:
      print(og_image['content'])
    else:
      print('No se encontró la imagen')

scrape_url('https://midu.dev')