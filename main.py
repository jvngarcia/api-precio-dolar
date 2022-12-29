from fastapi import FastAPI
import pandas as pd
import requests

app = FastAPI()

@app.get('/')
def home( ):

    return { 'Hello' : 'world' }