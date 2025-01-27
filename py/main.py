import requests

TENON_API_BASE_URL = 'https://tenon.symthoptic.com'
api_key = None

def configure(config):
    global api_key
    api_key = config.get('apiKey')

def chat(model, history):
    try:
        response = requests.post(
            f"{TENON_API_BASE_URL}/chat",
            json={"model": model, "history": history},
            headers={"key": api_key}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            raise Exception(error.response.json())
        else:
            raise Exception(str(error))

def create(model, message):
    try:
        response = requests.post(
            f"{TENON_API_BASE_URL}/create",
            json={"model": model, "message": message},
            headers={"key": api_key}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            raise Exception(error.response.json())
        else:
            raise Exception(str(error))
