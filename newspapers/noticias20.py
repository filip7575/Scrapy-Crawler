import requests
import csv
import time
timestr = time.strftime("%Y%m%d")
dates = time.strftime("%Y-%m-%d")

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

from bs4 import BeautifulSoup

outfile = open('noticias20Minutos'+timestr+'.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["titulo", "detalle", "cuerpo", "fecha"])


url = "https://thetimes.cl/categoria/18/tecnologia"
url = "https://www.20minutos.es/nacional/2/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

tags = soup.find_all("h1")
substring = "contenido"
list_href = []

#print(tags)

for tag in tags:
  res=(tag.find('a')['href'])
  list_href.append(res)


list_href.pop(0)
#Quitar duplicados
list_href = list(dict.fromkeys(list_href))

for hrf in list_href:
 print(hrf)
 url = hrf
 req = requests.get(url, headers)
 soup = BeautifulSoup(req.content, 'html.parser')
 if soup.find("div", {"class":"article-text"}) != None:
  title = soup.find("div", {"class":"title"})
  cuerp = soup.find("div", {"class":"article-text"})
  encab = soup.find("div", {"id":"m35-34-36"})
  titulo=title.get_text()
  detalle=encab.get_text()
  cuerpo=cuerp.get_text()
  fecha = dates
  writer.writerow([titulo, detalle, cuerpo, dates])
