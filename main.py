import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
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
    capital_name = driver.find_element(By.XPATH,
                                       f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Devise": capital_name.text.replace("\n", ""),
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

print(countries)
print('--------------------')
print(countries_currencies)
print('--------------------')
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
correspondences = 0
is_okay = True
for c1 in countries:
    corr = False
    for c2 in countries_currencies:
        if c1.get('Nom').lower() == c2.get('Nom').lower():
            correspondences += 1
            corr = True
    if not corr:
        is_okay = False
        print(c1.get("Nom"))
if is_okay:
    print('Parfait')

for c in countries_currencies:
    for x in countries:
        if x["Nom"] == c["Nom"]:
            x["Devise"] = c["Devise"]

print(countries)


