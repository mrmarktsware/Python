import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())  # This will print the formatted HTML