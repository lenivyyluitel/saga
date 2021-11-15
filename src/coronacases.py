import requests
from bs4 import BeautifulSoup

def corona(country):
    url = requests.get(f'https://www.worldometers.info/coronavirus/country/{country}/')
    soup = BeautifulSoup(url.content, features='lxml')

    cases = soup.find_all('div', class_='maincounter-number')
    lists = []
    for i in cases:
        lists.append(i.text.replace('\n',''))

    x = f"""
Cases: {lists[0]}
Deaths: {lists[1]}
Recovered: {lists[2]}
"""
    return x

#? made a new function cuz .../coronavirus/country/{NONE} is not a valid link

def total():
    url = requests.get(f'https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(url.content, features='lxml')

    cases = soup.find_all('div', class_='maincounter-number')
    lists = []
    for i in cases:
        lists.append(i.text.replace('\n',''))

    x = f"""
Total Cases: {lists[0]}
Total Deaths: {lists[1]}
Total Recovered: {lists[2]}
"""
    return x
