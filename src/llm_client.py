import os
from ollama import Client
from google.colab import userdata

def setup_ambiente():
    try:
        os.environ['OLLAMA_API_KEY'] = userdata.get('OLLAMA_API_KEY')
    except:
        pass
    
    api_key = os.getenv('OLLAMA_API_KEY')
    return Client(
        host="https://ollama.com",
        headers={'Authorization': f'Bearer {api_key}'}
    )

MODEL_NAME = "llama3.2:3B"
