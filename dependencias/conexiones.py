from calendar import c
import json
from tokenize import String
from turtle import clear
from numpy import empty
import requests
import pandas as pd


data = []
variantSKU = []
idSeller = []


def variantSKU_Writter(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        
        # {Contenido}
        url = f"https://api.ripley.com/marketplace/ecommerce/search/v1/cl/products/by-sku/{newApiRequest}?code=false&filter=false"

        payload={}
        headers = {
        'Cookie': '__cf_bm=xmkvYQsiDNt3WrA3GcaHROHP_JNwnuc2e9gLmEZ93sY-1650080271-0-AV3GJQdulRGdnGopTca2N1OKlDJxQHeXZZ+hCaVsSNiS0yuL6p/vdDMtbbzH4bdq8FGNvmLzdCfwLR5ggkIkKd4='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)

        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['sku'])) 
                variantSKU.append(str(item['sku']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return variantSKU


def idSeller_Writter(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        
        # {Contenido}
        url = f"https://api.ripley.com/marketplace/ecommerce/search/v1/cl/products/by-sku/{newApiRequest}?code=false&filter=false"

        payload={}
        headers = {
        'Cookie': '__cf_bm=xmkvYQsiDNt3WrA3GcaHROHP_JNwnuc2e9gLmEZ93sY-1650080271-0-AV3GJQdulRGdnGopTca2N1OKlDJxQHeXZZ+hCaVsSNiS0yuL6p/vdDMtbbzH4bdq8FGNvmLzdCfwLR5ggkIkKd4='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)

        
        
        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['shop']['id']))
                idSeller.append(str(item['shop']['id']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return idSeller

