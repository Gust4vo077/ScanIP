import requests
import os
from dotenv import find_dotenv,load_dotenv

def verificarIp(ip):
  dotEnvPath=find_dotenv()
  load_dotenv(dotEnvPath)
  urlBase= os.getenv("UrlBase")

  headers= {
    "Accept":"aplication/json",
    "Key":os.getenv("Key")
  }

  params= {
    "ipAddress":ip,
  }
 
  response = requests.get(urlBase, headers=headers, params=params)

  return response