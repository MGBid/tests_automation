import requests
from bs4 import BeautifulSoup


def extraer_urls(url):
     """Extrae todos los enlaces (URLs) de una página web.

    Args:
        url (str): La URL de la página web a analizar.

    Returns:
        list: Una lista de objetos BeautifulSoup representando cada enlace encontrado en la página.

    Raises:
        requests.exceptions.RequestException: Si ocurre un error durante la solicitud HTTP.
        ValueError: Si la URL proporcionada no es válida.

    Nota:
        * La función asume que los enlaces están contenidos dentro de etiquetas `<a>`.
        * El número 8 restado al conteo de enlaces es un ajuste específico para la página web en cuestión y podría necesitar ser modificado. Actualmente exceptúa las 8 urls de YouTube, Tik Tok y descargas de APPS para Android & Apple.
    """
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todos los enlaces (ajusta el selector según la estructura de la página)
    links = soup.find_all('a')
    print('** Longitud del listado: ', (len(links) - 8), ' **')
    return links


def check_urls(url):
    """
    Verifica los enlaces de una página web y cuenta los que cumplen ciertos criterios.

    Args:
        url (str): La URL de la página web a analizar.

    Returns:
        None

    Esta función realiza las siguientes tareas:

    1. Extrae todos los enlaces de la página web utilizando la función `extraer_urls`.
    2. Itera sobre cada enlace y verifica si:
        * No termina con una barra `/`.
        * No está en la lista de URLs excluidas.
    3. Incrementa los contadores `contador_ok` o `contador_fail` según corresponda.
    4. Imprime un resumen al finalizar, mostrando el número de enlaces válidos y no válidos.
    """
    links = extraer_urls(url)    

    contador_ok = 0
    contador_fail = 0


    for link in links:
        href = link.get('href')
        urls_fuera_alcance = ["https://www.youtube.com/c/eltrece", "https://www.tiktok.com/@eltrecetv", "https://play.google.com/store/apps/details?id=com.cmd.canal13", "https://apps.apple.com/ar/app/el-trece-tv/id413110207"]

        if href and not href.endswith('/'):
            # Condicional para excluir las urls de YT, Tik Tok y Apps
            if href in urls_fuera_alcance:
                continue
            else:
                print(f"URL sin barra al final: {href}")
                contador_fail = contador_fail + 1
        contador_ok = contador_ok + 1

    print(f'Contador OK: {contador_ok} \nContador FAIL: {contador_fail}  *****')

# URL de la página a analizar
url = "https://www.eltrecetv.com.ar/"


# Ejecutar la función
#check_urls(url)

listado_paginas = [
    "https://www.eltrecetv.com.ar/", 
    "https://www.eltrecetv.com.ar/ultimas-noticias/",
    "https://www.eltrecetv.com.ar/programas/", 
    "https://www.eltrecetv.com.ar/capitulos/", 
    "https://www.eltrecetv.com.ar/grilla/", 
    "https://www.eltrecetv.com.ar/convocatorias/", 
    "https://www.eltrecetv.com.ar/virales/", 
    "https://www.eltrecetv.com.ar/cucinare/", 
    "https://www.eltrecetv.com.ar/videos/",
    "https://www.eltrecetv.com.ar/programas/noticias-y-actualidad/",
    "https://www.eltrecetv.com.ar/capitulos/retrotrece/"
    ]


def ejecutar_check_urls(listado_urls):
    """
    Ejecuta una serie de comprobaciones en una lista de URLs. Mostrando datos por consola

    Args:
        listado_urls (list): Una lista de cadenas, cada una representando una URL.

    Returns:
        None
    """
    for url in listado_urls:
        print(f'Checking: {url}')
        check_urls(url)
        print('Next url...\n\n')
    print(f' {len(listado_urls)} URLs Checked')


# Ejecutar la función de varias urls
ejecutar_check_urls(listado_paginas)
