import requests

def verificar_enlace(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"El enlace {url} está funcionando")
        else:
            print(f"*************El enlace {url} está roto ({response.status_code})*************")
    except requests.exceptions.RequestException as e:
        print(f"Error al verificar el enlace {url}: {e}")

    
listado_urls = [
    "https://www.eltrecetv.com.ar/",
    "https://www.eltrecetv.com.ar/ultimas-noticias/",
    "https://www.eltrecetv.com.ar/programas/",
    "https://www.eltrecetv.com.ar/programas/noticias-y-actualidad/",
    "https://www.eltrecetv.com.ar/programas/entretenimiento/",
    "https://www.eltrecetv.com.ar/programas/ficcion/",
    "https://www.eltrecetv.com.ar/programas/retrotrece/",
    "https://www.eltrecetv.com.ar/capitulos/",
    "https://www.eltrecetv.com.ar/capitulos/noticias-y-actualidad/",
    "https://www.eltrecetv.com.ar/capitulos/entretenimiento/",
    "https://www.eltrecetv.com.ar/capitulos/ficcion/",
    "https://www.eltrecetv.com.ar/capitulos/retrotrece/",
    "https://www.eltrecetv.com.ar/virals/",
]

for url in listado_urls:
    verificar_enlace(url)