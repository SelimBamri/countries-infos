import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

# Getting country names and their capitals
driver.get("https://www.jetpunk.com/user-quizzes/29612/capitales-du-monde")
start_button = driver.find_element(By.XPATH,
                                   "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/button")
start_button.click()
time.sleep(2)
stop_button = driver.find_element(By.XPATH,
                                  "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]/button")
stop_button.click()
time.sleep(1)
countries = []
for i in range(2, 47):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Europe"
    }
    countries.append(country)

for i in range(49, 72):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Amérique du nord"
    }
    countries.append(country)

for i in range(2, 50):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Asie"
    }
    countries.append(country)

for i in range(52, 66):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Océanie"
    }
    countries.append(country)

for i in range(2, 14):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Amérique du sud"
    }
    countries.append(country)

for i in range(16, 70):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Afrique"
    }
    countries.append(country)
time.sleep(5)

# Getting countries currencies
driver.get("https://www.jetpunk.com/user-quizzes/1584524/devises-monetaires-par-pays")
start_button = driver.find_element(By.XPATH,
                                   "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/button")
start_button.click()
time.sleep(2)
stop_button = driver.find_element(By.XPATH,
                                  "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]/button")
stop_button.click()
time.sleep(1)
countries_currencies = []
for i in range(2, 68):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]/div")
    country_currency = driver.find_element(By.XPATH,
                                           f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Devise": country_currency.text.replace("\n", ""),
    }
    countries_currencies.append(country)

for i in range(2, 68):
    if i == 60:
        continue
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Devise": capital_name.text.replace("\n", ""),
    }
    countries_currencies.append(country)

for i in range(2, 67):
    country_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Devise": capital_name.text.replace("\n", ""),
    }
    countries_currencies.append(country)

# Getting country flags
driver.get("https://www.jetpunk.com/user-quizzes/176134/drapeaux-du-monde")
start_button = driver.find_element(By.XPATH,
                                   "//html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/button")
start_button.click()
time.sleep(2)
stop_button = driver.find_element(By.XPATH,
                                  "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]/button")
stop_button.click()
time.sleep(5)
countries_flags = []
for i in range(1, 40):
    for j in range(1, 6):
        country_name = driver.find_element(By.XPATH,
                                           f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/table[{i}]/tbody/tr[2]/td[{j}]/div")
        country_flag = driver.find_element(By.XPATH,
                                           f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/table[{i}]/tbody/tr[1]/td[{j}]/div/img")
        country = {
            "Nom": country_name.text.replace("\n", ""),
            "Drapeau": country_flag.get_attribute("src")
        }
        countries_flags.append(country)
countries_flags.append({
    "Nom": "Gambie",
    "Drapeau": "https://jetpunk.b-cdn.net/img/user-photo-library/08/08c6fc6253-450.png"
})

# Getting list of the maps
driver.get("https://www.jetpunk.com/user-quizzes/6121/chaque-formes-de-pays")
start_button = driver.find_element(By.XPATH,
                                   "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/button")
start_button.click()
time.sleep(2)
stop_button = driver.find_element(By.XPATH,
                                  "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]/button")
stop_button.click()
time.sleep(5)
countries_maps = []
for i in range(1, 40):
    for j in range(1, 6):
        country_name = driver.find_element(By.XPATH,
                                           f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/table[{i}]/tbody/tr[2]/td[{j}]/div")
        country_map = driver.find_element(By.XPATH,
                                          f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/table[{i}]/tbody/tr[1]/td[{j}]/div/img")
        country = {
            "Nom": country_name.text.replace("\n", ""),
            "Drapeau": country_map.get_attribute("src")
        }
        countries_maps.append(country)
countries_maps.append({
    "Nom": "Îles Marshall",
    "Drapeau": "https://jetpunk.b-cdn.net/img/user-photo-library/f3/f3158861d3-450.png"
})

# Printing the lists
print(countries)
print('--------------------')
print(countries_currencies)
print('--------------------')
print(countries_flags)
print('--------------------')
print(countries_maps)

# Manually correcting the inconsistencies
for i in range(196):
    if countries[i].get('Nom') == 'RépubliqueTchèque':
        countries[i]['Nom'] = 'République Tchèque'
    elif countries[i].get('Nom') == 'RépubliqueDominicaine':
        countries[i]['Nom'] = 'République Dominicaine'
    elif countries[i].get('Nom') == 'États Fédérésde Micronésie':
        countries[i]['Nom'] = 'Micronésie'
    elif countries[i].get('Nom') == 'GuinéeÉquatoriale':
        countries[i]['Nom'] = 'Guinée Équatoriale'
    elif countries[i].get('Nom') == 'RépubliqueCentrafricaine':
        countries[i]['Nom'] = 'République Centrafricaine'
    elif countries[i].get('Nom') == 'Rép. Dém.du Congo':
        countries[i]['Nom'] = 'République démocratique du Congo'
    elif countries[i].get('Nom') == 'Rép du Congo':
        countries[i]['Nom'] = 'République du Congo'
    if countries_flags[i].get('Nom') == 'Etats-Unis':
        countries_flags[i]['Nom'] = 'États-Unis'
    elif countries_flags[i].get('Nom') == 'Saint-Christophe- et-Niévès':
        countries_flags[i]['Nom'] = 'Saint-Christophe-et-Niévès'
    elif countries_flags[i].get('Nom') == 'Saint-Vincent-et-les- Grenadines':
        countries_flags[i]['Nom'] = 'Saint-Vincent-et-les-Grenadines'
    elif countries_flags[i].get('Nom') == 'Salomon':
        countries_flags[i]['Nom'] = 'Îles Salomon'
    elif countries_flags[i].get('Nom') == 'Papouasie-Nouvelle- Guinée':
        countries_flags[i]['Nom'] = 'Papouasie-Nouvelle-Guinée'
    elif countries_flags[i].get('Nom') == 'Île Maurice':
        countries_flags[i]['Nom'] = 'Maurice'
    if countries_maps[i].get('Nom') == 'Etats-Unis':
        countries_maps[i]['Nom'] = 'États-Unis'
    elif countries_maps[i].get('Nom') == 'Saint-Christophe- et-Niévès':
        countries_maps[i]['Nom'] = 'Saint-Christophe-et-Niévès'
    elif countries_maps[i].get('Nom') == 'Saint-Vincent-et-les- Grenadines':
        countries_maps[i]['Nom'] = 'Saint-Vincent-et-les-Grenadines'
    elif countries_maps[i].get('Nom') == 'Salomon':
        countries_maps[i]['Nom'] = 'Îles Salomon'
    elif countries_maps[i].get('Nom') == 'Papouasie-Nouvelle- Guinée':
        countries_maps[i]['Nom'] = 'Papouasie-Nouvelle-Guinée'
    elif countries_maps[i].get('Nom') == 'Île Maurice':
        countries_maps[i]['Nom'] = 'Maurice'

