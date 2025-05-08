"""
Explora cómo realizar peticiones HTTP a APIs con Python.

Este script demuestra dos enfoques principales:
1. Usando el módulo incorporado `urllib.request`.
2. Usando la popular biblioteca externa `requests`.

Conceptos cubiertos:
- ¿Qué es una API (Application Programming Interface)?
- Métodos HTTP comunes: GET, POST, PUT, DELETE.
- Formato de datos JSON (JavaScript Object Notation).
- Realizar peticiones GET para obtener datos.
- Realizar peticiones POST para enviar datos (crear recursos).
- Realizar peticiones PUT para actualizar datos (reemplazar recursos).
- Realizar peticiones DELETE para eliminar recursos.
- Manejo básico de respuestas: códigos de estado y contenido JSON.
- Envío de encabezados (Headers) como 'Content-Type' y 'Authorization'.
- Interacción con APIs reales (JSONPlaceholder, OpenAI, DeepSeek).
- Importancia de la seguridad con las API Keys.

Funciones 're' utilizadas:
- No se usa 're' directamente aquí, pero las APIs a menudo devuelven datos
  que podrían procesarse con expresiones regulares si fuera necesario.

Bibliotecas externas:
- requests: Una biblioteca estándar de facto para hacer peticiones HTTP en Python.
  (Necesita instalación: `pip install requests`)
"""

# --- Importaciones ---
import urllib.request
import urllib.error
import json
import requests # Necesita instalación: pip install requests
import os

# --- Limpieza de Consola (Opcional) ---
# Detecta automáticamente el sistema operativo
os.system('cls' if os.name == 'nt' else 'clear')


print("\n--- Realizando Peticiones HTTP a APIs con Python ---")

# --- ¿Qué es una API? ---
# Una API (Application Programming Interface) es un conjunto de reglas y protocolos
# que permite que diferentes aplicaciones de software se comuniquen entre sí.
# Las APIs web, comúnmente, usan HTTP para intercambiar datos, a menudo en formato JSON.

# --- Métodos HTTP Comunes ---
# - GET: Solicita datos de un recurso específico. Es seguro e idempotente.
# - POST: Envía datos para crear un nuevo recurso. No es seguro ni idempotente.
# - PUT: Envía datos para reemplazar completamente un recurso existente. Es idempotente.
# - DELETE: Elimina un recurso específico. Es idempotente.
# - PATCH: Envía datos para aplicar modificaciones parciales a un recurso.

# --- Formato JSON ---
# JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos,
# fácil de leer para humanos y fácil de interpretar para las máquinas.
# Es el formato más común para las respuestas de las APIs web.

# --- 1. Sin Dependencias Externas: Usando `urllib.request` ---
# Python incluye módulos para realizar peticiones web, pero pueden ser más verbosos.
print("\n--- 1. Usando urllib.request (Módulo Incorporado) ---")

# URL de ejemplo de la API JSONPlaceholder (una API falsa para pruebas)
api_posts_urllib = "https://jsonplaceholder.typicode.com/posts/1" # Obtener un post específico

print(f"Realizando GET a: {api_posts_urllib}")
try:
    # Abre la conexión a la URL
    response_urllib = urllib.request.urlopen(api_posts_urllib)

    # Lee el contenido de la respuesta (en bytes)
    data_bytes = response_urllib.read()

    # Decodifica los bytes a una cadena de texto (usualmente utf-8)
    data_string = data_bytes.decode('utf-8')

    # Convierte la cadena JSON en un objeto Python (diccionario o lista)
    json_data_urllib = json.loads(data_string)

    print("Respuesta (JSON):")
    # Imprime el JSON formateado para legibilidad
    print(json.dumps(json_data_urllib, indent=2))

    # Es buena práctica cerrar la respuesta
    response_urllib.close()

except urllib.error.URLError as e:
    # Manejo básico de errores de conexión o URL
    print(f"Error en la solicitud con urllib: {e}")
except json.JSONDecodeError as e:
    # Manejo de errores si la respuesta no es JSON válido
    print(f"Error al decodificar JSON: {e}")

# Nota: Hacer POST, PUT, etc., con urllib.request es más complejo y requiere
# construir el objeto Request manualmente, manejar headers, codificar datos, etc.

# --- 2. Con la Biblioteca `requests` (Recomendado) ---
# La biblioteca `requests` simplifica enormemente el proceso de hacer peticiones HTTP.
# ¡Necesita instalación! -> pip install requests
print("\n--- 2. Usando la biblioteca `requests` (Recomendado) ---")

# --- 2.1. Petición GET ---
# GET: Obtener recursos.
print("\n--- 2.1. GET ---")
api_posts_requests = "https://jsonplaceholder.typicode.com/posts/"
print(f"Realizando GET a: {api_posts_requests}")

try:
    # Realiza la petición GET
    response_get = requests.get(api_posts_requests)

    # Verificar el código de estado HTTP
    # 200 OK: La solicitud fue exitosa.
    # 4xx: Errores del cliente (ej. 404 Not Found, 401 Unauthorized).
    # 5xx: Errores del servidor.
    print(f"Código de Estado: {response_get.status_code}")

    # Lanzar una excepción para códigos de error (4xx o 5xx)
    response_get.raise_for_status()

    # Obtener la respuesta como JSON (requests lo decodifica automáticamente)
    response_json_get = response_get.json()

    print("Respuesta GET (primeros 3 posts):")
    # Imprime solo los primeros 3 elementos para brevedad, formateados
    print(json.dumps(response_json_get[:3], indent=2))

    # También puedes acceder a los encabezados de la respuesta
    # print("\nEncabezados de la respuesta GET:")
    # print(response_get.headers)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud GET con requests: {e}")
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON de la respuesta GET: {e}")


# --- 2.2. Petición POST ---
# POST: Crear un nuevo recurso.
print("\n--- 2.2. POST ---")
url_post = "https://jsonplaceholder.typicode.com/posts"
# Datos a enviar en el cuerpo de la petición (como diccionario Python)
nuevo_post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
print(f"Realizando POST a: {url_post}")
print(f"Datos enviados: {nuevo_post_data}")

try:
    # Realiza la petición POST, enviando los datos como JSON
    response_post = requests.post(url_post, json=nuevo_post_data)

    # Código esperado para creación exitosa: 201 Created
    print(f"Código de Estado POST: {response_post.status_code}")
    response_post.raise_for_status() # Verificar errores

    # La respuesta a menudo contiene el recurso creado (con su nuevo ID)
    respuesta_post_json = response_post.json()
    print("Respuesta POST (recurso creado):")
    print(json.dumps(respuesta_post_json, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud POST con requests: {e}")


# --- 2.3. Petición PUT ---
# PUT: Actualizar/Reemplazar un recurso existente.
print("\n--- 2.3. PUT ---")
# URL del recurso a actualizar (post con ID 1)
url_put = "https://jsonplaceholder.typicode.com/posts/1"
# Nuevos datos para el recurso (reemplaza completamente el existente)
datos_actualizados_put = {
    "id": 1, # A menudo se incluye el ID en el cuerpo para PUT
    "title": "titulo actualizado",
    "body": "cuerpo actualizado",
    "userId": 1,
}
print(f"Realizando PUT a: {url_put}")
print(f"Datos enviados: {datos_actualizados_put}")

try:
    # Realiza la petición PUT, enviando los datos como JSON
    response_put = requests.put(url_put, json=datos_actualizados_put)

    # Código esperado para actualización exitosa: 200 OK
    print(f"Código de Estado PUT: {response_put.status_code}")
    response_put.raise_for_status()

    # La respuesta suele contener el recurso actualizado
    respuesta_put_json = response_put.json()
    print("Respuesta PUT (recurso actualizado):")
    print(json.dumps(respuesta_put_json, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud PUT con requests: {e}")

# --- 2.4. Petición DELETE ---
# DELETE: Eliminar un recurso existente.
print("\n--- 2.4. DELETE ---")
# URL del recurso a eliminar (post con ID 1)
url_delete = "https://jsonplaceholder.typicode.com/posts/1"
print(f"Realizando DELETE a: {url_delete}")

try:
    # Realiza la petición DELETE
    response_delete = requests.delete(url_delete)

    # Código esperado para eliminación exitosa: 200 OK (a veces 204 No Content)
    print(f"Código de Estado DELETE: {response_delete.status_code}")
    response_delete.raise_for_status()

    # La respuesta a DELETE suele estar vacía o contener un mensaje de éxito
    print("Respuesta DELETE: Recurso eliminado (o marcado como tal en la API de prueba).")
    # print(response_delete.text) # Podría haber texto, o estar vacío

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud DELETE con requests: {e}")


# --- 3. Ejemplos con APIs Reales (OpenAI y DeepSeek) ---
# Estas APIs requieren autenticación mediante una API Key.
print("\n--- 3. Ejemplos con APIs Reales (Requieren API Key) ---")

# --- ¡¡¡ADVERTENCIA DE SEGURIDAD IMPORTANTE!!! ---
# NUNCA guardes tus API Keys directamente en el código fuente,
# especialmente si vas a compartirlo o subirlo a un repositorio (como Git).
# Es una mala práctica de seguridad muy grave.
# Alternativas seguras:
# 1. Variables de Entorno: Guarda la clave en una variable de entorno del sistema
#    y léela en tu script usando `os.environ.get('NOMBRE_DE_LA_VARIABLE')`.
# 2. Archivos de Configuración: Guarda la clave en un archivo (ej. .env, config.json)
#    que NO se incluya en el control de versiones (añádelo a .gitignore).
# 3. Gestores de Secretos: Para aplicaciones más complejas, usa servicios
#    especializados en gestión de secretos (AWS Secrets Manager, Google Secret Manager, HashiCorp Vault).
#
# Los siguientes ejemplos usan claves directamente por simplicidad didáctica,
# ¡PERO NO LO HAGAS EN PROYECTOS REALES!
# ---

# Claves de API (Reemplazar con las tuyas si pruebas, pero ¡CUIDADO!)
# Se dejan como en el original para seguir la clase, pero con la advertencia.
OPENAI_API_KEY = "sk-proj-..." # ¡NO SUBIR ESTO A GIT! Usa variables de entorno.
DEEPSEEK_API_KEY = "xxx"       # ¡NO SUBIR ESTO A GIT! Usa variables de entorno.

# --- 3.1. Llamada a OpenAI GPT ---
# Ref: https://platform.openai.com/docs/api-reference/chat/create
print("\n--- 3.1. Llamada a OpenAI GPT ---")

def call_openai_gpt(api_key, prompt):
    """Realiza una llamada a la API de Chat Completions de OpenAI."""
    url = "https://api.openai.com/v1/chat/completions"
    # Encabezados necesarios: Tipo de contenido y Autorización (Bearer Token)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}" # Así se envían las API Keys normalmente
    }
    # Datos de la petición: modelo a usar y mensajes (conversación)
    data = {
        "model": "gpt-4o-mini", # Modelo específico
        "messages": [{"role": "user", "content": prompt}] # Prompt del usuario
    }

    print("Enviando petición a OpenAI...")
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status() # Verificar errores HTTP
        print("Respuesta recibida de OpenAI.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a OpenAI: {e}")
        # Podrías querer ver más detalles del error si la API lo proporciona
        if hasattr(e, 'response') and e.response is not None:
             try:
                 print("Detalle del error API:", e.response.json())
             except json.JSONDecodeError:
                 print("Detalle del error API (no JSON):", e.response.text)
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON de OpenAI: {e}")
        return None

# Realizar la llamada (solo si tienes una clave válida y quieres gastar créditos)
# api_response_openai = call_openai_gpt(OPENAI_API_KEY, "Escribe un breve poema sobre la programación")
#
# if api_response_openai and "choices" in api_response_openai and api_response_openai["choices"]:
#     # Extraer el contenido del mensaje de la respuesta
#     print("\nRespuesta de OpenAI:")
#     print(api_response_openai["choices"][0]["message"]["content"])
#     # print("\nRespuesta completa OpenAI (JSON):")
#     # print(json.dumps(api_response_openai, indent=2))
# else:
#     print("No se pudo obtener una respuesta válida de OpenAI.")

# --- 3.2. Llamada a DeepSeek ---
print("\n--- 3.2. Llamada a DeepSeek ---")

def call_deepseek(api_key, prompt):
    """Realiza una llamada a la API de Chat Completions de DeepSeek."""
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "deepseek-chat", # Modelo específico de DeepSeek
        "messages": [{"role": "user", "content": prompt}]
    }

    print("Enviando petición a DeepSeek...")
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print("Respuesta recibida de DeepSeek.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a DeepSeek: {e}")
        if hasattr(e, 'response') and e.response is not None:
             try:
                 print("Detalle del error API:", e.response.json())
             except json.JSONDecodeError:
                 print("Detalle del error API (no JSON):", e.response.text)
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON de DeepSeek: {e}")
        return None

# Realizar la llamada (solo si tienes una clave válida)
# api_response_deepseek = call_deepseek(DEEPSEEK_API_KEY, "Explica qué es una API REST en 3 frases.")
#
# if api_response_deepseek and "choices" in api_response_deepseek and api_response_deepseek["choices"]:
#     print("\nRespuesta de DeepSeek:")
#     print(api_response_deepseek["choices"][0]["message"]["content"])
#     # print("\nRespuesta completa DeepSeek (JSON):")
#     # print(json.dumps(api_response_deepseek, indent=2))
# else:
#     print("No se pudo obtener una respuesta válida de DeepSeek.")


###
# EJERCICIOS (requests)
# Pon en práctica lo aprendido haciendo peticiones HTTP.
# Descomenta las soluciones para verificar tus respuestas.
###

print("\n--- EJERCICIOS ---")

# Ejercicio 1: Obtener datos de un Pokémon
# Usa la PokéAPI (https://pokeapi.co/) para obtener información sobre Pikachu.
# Realiza una petición GET a "https://pokeapi.co/api/v2/pokemon/pikachu".
# Imprime el nombre del Pokémon y su tipo principal extraídos de la respuesta JSON.
print("\nEjercicio 1: Datos de Pikachu")
# url_pokeapi = "https://pokeapi.co/api/v2/pokemon/pikachu"
# try:
#     response_poke = requests.get(url_pokeapi)
#     response_poke.raise_for_status() # Verificar errores
#     data_poke = response_poke.json()
#     nombre_pokemon = data_poke.get("name", "Nombre no encontrado")
#     # Los tipos están en una lista de diccionarios
#     tipos = data_poke.get("types", [])
#     tipo_principal = "Tipo no encontrado"
#     if tipos:
#         # El tipo principal suele ser el primero en la lista
#         tipo_principal = tipos[0].get("type", {}).get("name", "Tipo no encontrado")
#
#     print(f"Nombre: {nombre_pokemon.capitalize()}")
#     print(f"Tipo Principal: {tipo_principal.capitalize()}")
#
# except requests.exceptions.RequestException as e:
#     print(f"Error al obtener datos de PokéAPI: {e}")
# except (KeyError, IndexError, AttributeError) as e:
#     print(f"Error al procesar los datos del Pokémon: {e}")

# Ejercicio 2: Crear un usuario falso
# Usa la API reqres.in (https://reqres.in/) para simular la creación de un usuario.
# Realiza una petición POST a "https://reqres.in/api/users" con los siguientes datos JSON:
#   { "name": "morpheus", "job": "leader" }
# Imprime el código de estado de la respuesta y el cuerpo de la respuesta JSON.
print("\nEjercicio 2: Crear usuario en ReqRes")
# url_reqres_post = "https://reqres.in/api/users"
# datos_usuario = { "name": "morpheus", "job": "leader" }
# try:
#     response_reqres = requests.post(url_reqres_post, json=datos_usuario)
#     print(f"Código de Estado POST ReqRes: {response_reqres.status_code}")
#     response_reqres.raise_for_status()
#     print("Respuesta POST ReqRes (JSON):")
#     print(json.dumps(response_reqres.json(), indent=2))
# except requests.exceptions.RequestException as e:
#     print(f"Error al crear usuario en ReqRes: {e}")

# Ejercicio 3: Manejar un error 404
# Intenta obtener datos de una URL que no existe en JSONPlaceholder, por ejemplo:
# "https://jsonplaceholder.typicode.com/posts/99999999"
# Usa un bloque try...except para capturar la excepción `requests.exceptions.HTTPError`
# e imprime un mensaje indicando que el recurso no fue encontrado (basado en el status_code).
print("\nEjercicio 3: Manejar Error 404")
# url_not_found = "https://jsonplaceholder.typicode.com/posts/99999999"
# try:
#     response_404 = requests.get(url_not_found)
#     print(f"Código de Estado: {response_404.status_code}")
#     response_404.raise_for_status() # Esto lanzará HTTPError si status_code es 4xx o 5xx
#     print("Recurso encontrado (inesperado).") # No debería llegar aquí
# except requests.exceptions.HTTPError as e:
#     if e.response.status_code == 404:
#         print(f"Error esperado: Recurso no encontrado (404). URL: {url_not_found}")
#     else:
#         print(f"Error HTTP inesperado: {e}")
# except requests.exceptions.RequestException as e:
#     print(f"Error de conexión o solicitud: {e}")
