from dotenv import load_dotenv
import os
import requests

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter o file_id do .env
file_id = os.getenv('id')

# concatenar a url com id
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

session = requests.Session()
response = session.get(download_url, stream=True)


with open('ERP.json', 'wb') as f:
    for chunk in response.iter_content(chunk_size=32768):
        if chunk:
            f.write(chunk)
