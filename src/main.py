import os
import requests
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_TOKEN_CLIENT = os.getenv("ZAPI_TOKEN_CLIENT")


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    try:
        response = supabase.table("contatos").select("*").execute()
        contatos = response.data
        if not contatos:
            print("Nenhum contato encontrado no banco.")
            return []
        return contatos[:3]
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []

def enviar_mensagem(numero, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": numero,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    headers = {
        "Client-Token": ZAPI_TOKEN_CLIENT,
        "Content-Type": "application/json"
    }
    try:
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code == 200:
            print(f"Mensagem enviada para {nome} ({numero})")
        else:
            print(f"Erro ao enviar para {numero}: {r.text}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

if __name__ == "__main__":
    contatos = buscar_contatos()
    for contato in contatos:
        enviar_mensagem(contato["numero"], contato["nome"])