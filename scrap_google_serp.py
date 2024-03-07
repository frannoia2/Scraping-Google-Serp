import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap_serp(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'es-ES,es;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition std-1)'}
    respuesta = requests.get(url, headers=headers)
    print(respuesta.status_code)
    if(respuesta.status_code != 200):
        print(respuesta)

    search_results = []
    soup = BeautifulSoup(respuesta.content, 'html.parser')


    for elemento in soup.find_all('div', {'class': 'tF2Cxc'}):
        try:
            url_element = elemento.find('a').get('href')
            if url:
                if(url_element.find('https') != -1 and url_element.find('http') == 0):
                    url = url_element
                    titulo = elemento.find('h3').text
                    try:
                        descripcion = elemento.find('div', {'class':'IsZvec'}).text
                    except:
                        descripcion = elemento.find('div', {'class':'kb0PBd cvP2Ce'}).text
                    search_results.append({ "Titulo": titulo,
                                            "Enlace": url,
                                            "Descripcion": descripcion})
        except Exception as e:
            print("Error:", e)
            continue

    df = pd.DataFrame(search_results)
    df.to_json('scrap_google_serp.json', orient='records', indent=2, force_ascii= False)

query = "selenium"
scrap_serp(query)
