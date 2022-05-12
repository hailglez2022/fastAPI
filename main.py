from webbrowser import get
from fastapi import FastAPI
from requests import request
import json

app = FastAPI()

@app.get("/visa")
def visa(destinationCurrencyCode: str, sourceAmount: str, sourceCurrencyCode: str):
  url = "https://sandbox.api.visa.com/forexrates/v2/foreignexchangerates"

  payload = json.dumps({
  "acquirerDetails": {
    "bin": 411608,
    "settlement": {
      "currencyCode": sourceCurrencyCode
    }
  },
  "rateProductCode": "A",
  "markupRate": "0.00",
  "destinationCurrencyCode": destinationCurrencyCode,
  "sourceAmount": sourceAmount,
  "sourceCurrencyCode": sourceCurrencyCode
})
  headers = {
  'Content-Type': 'application/json'
}
  cert = ('C:/Users/Hail Gonzáles/Downloads/cert2.pem','C:/Users/Hail Gonzáles/Downloads/private_key.pem')
  auth = ('O9CESWYT0GKLWAMDDUOU21YQnPwgC88x3ICEDhfqS8RC8DRho', 'Pel5ccVTGh')

  response = request("POST", url, headers=headers, data=payload,  cert=cert, auth=auth)

  
  return(json.loads(response.content))
