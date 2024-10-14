import requests
import os
import csv
from bs4 import BeautifulSoup


def check_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Ruta del archivo CSV
    urls_validas = 'urls_validas.csv'
    urls_no_validas = 'urls_no_validas.csv'

    # Eliminar el archivo si existe
    if os.path.exists(urls_validas):
        os.remove(urls_validas)
    if os.path.exists(urls_no_validas):
        os.remove(urls_no_validas)

    # Crear archivos CSV
    with open('urls_validas.csv', 'a', newline='') as valid_file, \
         open('urls_no_validas.csv', 'a', newline='') as invalid_file:
        valid_writer = csv.writer(valid_file)
        invalid_writer = csv.writer(invalid_file)

        # Encuentra todos los enlaces
        links = soup.find_all('a')

        contador_fail = 0
        contador_ok = 0

        for link in links:
            href = link.get('href')
            if href:
                if href.endswith('/'):
                    print(f'URL CON BARRA AL FINAL: {href}')
                    contador_ok = contador_ok + 1
                    valid_writer.writerow([href])
                else:
                    print(f'URL SIN BARRA AL FINAL: {href}')
                    contador_fail = contador_fail + 1
                    invalid_writer.writerow([href])


        print(f'Contador OK: {contador_ok}')
        print(f'Contador FAIL: {contador_fail}')

# URL de la página a analizar
#url = "https://www.eltrecetv.com.ar/"
url = "https://www.eltrecetv.com.ar/ultimas-noticias/"


# Ejecutar la función
check_urls(url)
