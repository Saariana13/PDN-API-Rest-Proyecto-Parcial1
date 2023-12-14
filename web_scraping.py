import requests
from bs4 import BeautifulSoup
import pandas as pd

nombres = list()
apellidos = list()
emails = list()
especialidades = list()

url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)
print(html_doc)
soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table')
filas = tabla.find_all('tr')

for fila in filas:
    celdas = fila.find_all('td')
    print(celdas)
    if len(celdas)>0:
        nombres.append(celdas[0].string)
        apellidos.append(celdas[1].string)
        emails.append(celdas[2].string)
        especialidades.append(celdas[3].string)

print(apellidos)
print(nombres)
print(emails)
print(especialidades)

df = pd.DataFrame({'Nombre':nombres,'Apellido':apellidos,'Email':emails,'Especialidad':especialidades})
df.to_csv('medicos.csv', index=False, encoding='UTF-8-sig')
