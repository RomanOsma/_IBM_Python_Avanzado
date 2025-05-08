import requests  # <- ¡Esto es obligatorio!
import json

# 1. Hacer una petición GET
print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)

# 2. Obtener el JSON
response_json = response.json()

# 3. Mostrar parte del contenido
print(json.dumps(response_json[:3], indent=2))  # Solo los 3 primeros
