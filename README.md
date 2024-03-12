# Scraping-Google-Serp

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)


Scripts para scrapear los resultados de una búsqueda en Google, usando distintos métodos.
Su funcionamiento nos scrapea el título, la url y la descripción de los primeros resultados de una búsqueda que le pasemos como parámetro y nos lo devuelve en formato .json.
## 2 versiones:
- Utilizando Selenium: Esta versión tiene las ventajas de al usar la opción del driver headless, nos permite simular el funcionamiento humano real, además podemos scrapear páginas dinamicas. 

* Utilizando BeautifulSoup: Con esta versión obtemenos el código HTML de la página para poder trabajar con él y encontrar lo que deseemos. 