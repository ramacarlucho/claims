import os

import uvicorn

from evmoswallet.converter import eth_to_evmos
from evmoswallet.converter import evmos_to_eth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import db

MY_HOST = os.getenv('ALLOWED_HOST', '*')

# Config
ALLOWED_HOSTS = [MY_HOST]

app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class Address(BaseModel):
    address: str

class ClaimResponse(BaseModel):
    address: str
    claimable: float
    error: str

def verify_address(address):
    try:
        if address.startswith('evmos'):
            return eth_to_evmos(evmos_to_eth(address)) == address
        if address.startswith('0x'):
            return evmos_to_eth(eth_to_evmos(address)).lower() == address.lower()
    except Exception as e:
        return False
    return False


@app.post('/getclaimable/', response_model=ClaimResponse)
def get_claimable(address: Address):
    if not verify_address(address.address):
        return {'address': None, "claimable": None, 'error': 'Invalid Address'}

    addr = address.address
    if address.address.startswith('0x'):
        addr = eth_to_evmos(address.address)
 
    claimable = db.get_claimable(addr)

    return {'address': addr, 'claimable': claimable, 'error': ""}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=6000, log_level='info')