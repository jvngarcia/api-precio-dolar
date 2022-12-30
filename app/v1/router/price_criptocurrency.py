from fastapi import APIRouter
import pandas as pd



router = APIRouter( prefix = "/api/v1/price-criptocurrency" )


@router.get("/btc/")
def get_btc():

    URL = "https://coinmarketcap.com/"
    
    dfs = pd.read_html(URL)

    # Obtener la primera tabla                                                                                                      
    df = dfs[0]

    # Extraer las columnas                                                                                                           
    df2 = df[['Name','Price']]

    nombre = df2['Name'].iloc[0].rstrip('1BTC')
    precio = df2['Price'].iloc[0].lstrip('$')
    moneda = df2['Price'].iloc[0][0:1]

    return {
        'name' : nombre,
        'price' : precio,
        'currency' : moneda,
    }