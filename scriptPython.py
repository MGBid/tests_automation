import requests
from bs4 import BeautifulSoup

def check_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todos los enlaces (ajusta el selector según la estructura de la página)
    links = soup.find_all('a')

    # Listo los links a través del for MNC
    print('** La longitud del listado es ', len(links), ' **')
    for link in links:
        print('--------------------------------------------------------------------------------------')
        print('El link que itera')
        print(link)
        print('---------------------------------------------------')
        print('Tomamos el href:')
        href = link.get('href')
        print('Print de HREF:')
        print(href)
        print('--------------------------------------------------------------------------------------')


    for link in links:
        href = link.get('href')
        if href and not href.endswith('/'):
            print(f"URL sin barra al final: {href}")

# URL de la página a analizar
url = "https://tn.com.ar/"

# Ejecutar la función
check_urls(url)