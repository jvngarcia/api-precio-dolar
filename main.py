from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests
import json

app = FastAPI()

@app.get('/')
def home( ):
    URL = "https://monitordolarvenezuela.com/"
    URL_BCV = 'https://www.bcv.org.ve/'

    req = requests.get(URL)

    status_code = req.status_code

    if status_code != 200:
        raise HTTPException( status_code = 404, detail = "Sitio web no encontrado" )

    soup = BeautifulSoup(req.text, 'lxml')

    contenedor_promedios = soup.find_all('div', class_="col-12 col-sm-4 col-md-2 col-lg-2")

    textos = {}

    for promedios in contenedor_promedios:
        textos[promedios.h4.string] = promedios.p.string

    bcv = textos['BCV (Oficial)'].lstrip('Bs = ')
    paralelo = textos['@EnParaleloVzla3'].lstrip('Bs = ')

    return {
        'BCV' : bcv,
        'En Paralelo' : paralelo
    }   