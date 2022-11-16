import requests

requisicao = requests.get("http://localhost:5000/certificados")

print(requisicao)