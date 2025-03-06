import requests
from bs4 import BeautifulSoup
import json

# Asosiy URL
base_url = 'https://demoblaze.com'

# Sahifani yuklab olish
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Noutbuklar ro'yxati
laptops = []

# Noutbuklar bo'limiga o'tish
laptops_section = soup.find('a', text='Laptops')
laptops_url = base_url + '/' + laptops_section['href']
response = requests.get(laptops_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Noutbuklar ma'lumotlarini yig'ish
items = soup.find_all('div', class_='card')
for item in items:
    name = item.find('h4', class_='card-title').text.strip()
    price = item.find('h5').text.strip()
    description = item.find('p', class_='card-text').text.strip()
    laptops.append({
        'name': name,
        'price': price,
        'description': description
    })

# Keyingi sahifaga o'tish
next_button = soup.find('button', id='next2')
if next_button:
    next_url = base_url + '/' + next_button['onclick'].split("'")[1]
    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='card')
    for item in items:
        name = item.find('h4', )