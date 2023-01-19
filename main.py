from fastapi import FastAPI

# Importa las rutas del aplicativo
from app.v1.router import changing_table
from app.v1.router import price_criptocurrency

app = FastAPI()
app.include_router( changing_table.router )
app.include_router( price_criptocurrency.router )