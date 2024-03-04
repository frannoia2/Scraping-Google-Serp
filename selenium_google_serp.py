import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrap_serp(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)

    search_results = []
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g')))
    first_search = driver.find_element(By.CSS_SELECTOR, 'div.MjjYud')
    
    try:
        url_first = first_search.find_element(By.CSS_SELECTOR, 'a')
        url = url_first.get_attribute('href')
        titulo = first_search.find_element(By.XPATH, './/h3[@class="LC20lb MBeuO DKV0Md"]').text
        description = first_search.find_element(By.CSS_SELECTOR, 'div.IsZvec > div > span').text
        search_results.append({ "Titulo": titulo,
                                    "Enlace": url,
                                    "Descripcion": description})
    except Exception as e:
        print("Error: ", e)

    next_searchs =  driver.find_elements(By.XPATH, './/div[@class="N54PNb BToiNc cvP2Ce"]')

    for elemento in next_searchs:
        try:
            url_element = elemento.find_element(By.CSS_SELECTOR, 'a')
            url = url_element.get_attribute('href')
            titulo_elemento = elemento.find_element(By.XPATH, './/h3')
            titulo = titulo_elemento.get_attribute('innerText')
            description_elemento = elemento.find_element(By.XPATH, './/div[@data-sncf]')
            description = description_elemento.get_attribute('innerText')
            search_results.append({ "Titulo": titulo,
                                    "Enlace": url,
                                    "Descripcion": description})
        except Exception as e:
            print("Error:", e)
            continue
            
    driver.quit()
    df = pd.DataFrame(search_results)
    df.to_json('selenium_google_serp.json', orient='records', indent=2, force_ascii= False)

query = "selenium"
scrap_serp(query)

