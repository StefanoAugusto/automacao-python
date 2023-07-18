import pandas as pd
import os
import kaggle
import zipfile
from functions import fazContagem, enviarEmail

kaggle.api.authenticate()

dataSet = 'olistbr/brazilian-ecommerce'
fileName = 'olist_customers_dataset.csv'
kaggle.api.dataset_download_file(dataSet, fileName)

with zipfile.ZipFile(fileName + '.zip', 'r') as zipRef:
    zipRef.extractall()

df = pd.read_csv(os.path.join(fileName))    

diretorioSaida = './saida/'
os.makedirs(diretorioSaida, exist_ok=True)

uf = sorted(df['customer_state'].unique())
os.remove(fileName + '.zip')
fazContagem(df, uf, diretorioSaida)
enviarEmail(uf)