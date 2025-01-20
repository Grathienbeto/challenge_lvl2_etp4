import pandas as pd # type: ignore
import requests # type: ignore

df = pd.read_csv('./data.csv')
url = 'https://postman-library-api.glitch.me/books'
headers = {
  'Content-Type': 'application/json',
}

for i, row in df.iterrows():
  body = {
    "title" : row['title'],
    "author" : row['author'],
    "genre" : row['genre'],
    "yearPublished": int(row['yearPublished'])
  }
  
  try:
    response = requests.post(url, headers=headers, json=body)
    print(f'Solicitud {i+1}: Enviada con exito')
    print(response.status_code)
    print(response.json(), end='\n\n')
        
  except Exception:
    print(f'Solicitud {i+1}: Tuvo errores')