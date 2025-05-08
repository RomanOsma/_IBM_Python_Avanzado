import requests
import argparse

from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument('url', type=str, help='The URL of the site you want to scrape and check')
args = parser.parse_args()
url = args.url

headers = {
  'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
  print('La petición fue exitosa')

  soup = BeautifulSoup(response.text, 'html.parser')

  print(f"\033[34mRevisando la página: {url}\033[0m")
  print("\nSEO básico:")

  titulo_pagina = soup.title.string

  if titulo_pagina:
    print(f"\033[46mEl título de la página es: {titulo_pagina}\033[0m")
    if len(titulo_pagina) < 70:
      print("\033[32m✅  El título de la página tiene una longitud adecuada\033[0m")
    else:
      print("⚠️  El título de la página es DEMASIADO largo")

  # extrae todos los titulos h1
  titulos = [titulo.text for titulo in soup.find_all('h1')]
  if not titulos:
    print("\033[31m❌  No se encontraron títulos h1 en la página\033[0m")
  elif len(titulos) > 1:
    print("\033[31m❌  Hay más de un título h1 en la página\033[0m")
    for titulo in titulos:
      print(titulo)
  else:
    print("\033[32m✅  Hay un título h1 en la página\033[0m")