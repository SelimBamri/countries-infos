import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.jetpunk.com/user-quizzes/29612/capitales-du-monde")
start_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/button")
start_button.click()
time.sleep(2)
stop_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]/button")
stop_button.click()
time.sleep(1)
countries = []
for i in range(2, 47):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Europe"
    }
    countries.append(country)

for i in range(49, 72):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Amérique du nord"
    }
    countries.append(country)

for i in range(2, 50):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Asie"
    }
    countries.append(country)

for i in range(52, 66):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[2]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Océanie"
    }
    countries.append(country)

for i in range(2, 14):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Amérique du sud"
    }
    countries.append(country)

for i in range(16, 70):
    country_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[1]/div")
    capital_name = driver.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[11]/div/table/tbody/tr/td[3]/table/tbody/tr[{i}]/td[2]")
    country = {
        "Nom": country_name.text.replace("\n", ""),
        "Capitale": capital_name.text.replace("\n", ""),
        "Continent": "Afrique"
    }
    countries.append(country)

print(len(countries))
print(countries)
time.sleep(5)

