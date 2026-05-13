import os
from ollama import Client
from google.colab import userdata

def setup_ambiente():
    try:
        os.environ['OLLAMA_API_KEY'] = userdata.get('OLLAMA_API_KEY')
    except Exception as e:
        print(f"⚠️ Erro ao carregar segredos: {e}")

    api_key = os.getenv('OLLAMA_API_KEY')
    client = Client(
        host="https://ollama.com",
        headers={'Authorization': f'Bearer {api_key}'}
    )
    return client

MODEL_NAME = "gpt-oss:120b"
