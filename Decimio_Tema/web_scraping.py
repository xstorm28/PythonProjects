import bs4
import requests
import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


parrafo_especial = sopa.select('div')[3].getText()

print(parrafo_especial)