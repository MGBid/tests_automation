import requests
import os
import csv
from bs4 import BeautifulSoup



# URL de la página a analizar
#url = "https://www.eltrecetv.com.ar/"
url = "https://www.eltrecetv.com.ar/ultimas-noticias/"

# Ruta del archivo CSV
urls_validas = 'urls_ult_notic_validas.csv'
urls_no_validas = 'urls_ult_notic_no_validas.csv'

# Eliminar el archivo si existe
if os.path.exists(urls_validas):
    os.remove(urls_validas)
if os.path.exists(urls_no_validas):
    os.remove(urls_no_validas)

def check_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Crear archivos CSV
    with open('urls_ult_notic_validas.csv', 'a', newline='') as valid_file, \
         open('urls_ult_notic_no_validas.csv', 'a', newline='') as invalid_file:
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
                    contador_ok = contador_ok + 1
                    valid_writer.writerow([href])
                else:
                    contador_fail = contador_fail + 1
                    invalid_writer.writerow([href])


        print(f'Contador OK: {contador_ok}')
        print(f'Contador FAIL: {contador_fail}')


def itera_500_urls():
    base_url = "https://www.eltrecetv.com.ar/ultimas-noticias/pagina/"
    for i in range(1, 501):
        pagina = base_url + str(i) + "/"
        print(f'Pagina {pagina}')
        check_urls(pagina)


# Ejecutar la función
check_urls(url)
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/74/")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/75/")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/129")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/235")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/285")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/335")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/388")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/439")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/440")
check_urls("https://www.eltrecetv.com.ar/ultimas-noticias/pagina/486")



print('Pasamos a las PÁGINAS')
#itera_500_urls()
