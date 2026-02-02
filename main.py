import json
import os
from flask import Flask, request, abort

app = Flask(__name__)

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def deliver_content():
    conf = load_config()
    client_ip = request.remote_addr
    
    # Validação da Key (Filtro de IP)
    if conf["key"].lower() != "none":
        if client_ip != conf["key"]:
            print(f"⚠️ Acesso bloqueado para o IP: {client_ip}")
            abort(403) # Erro de Proibido
    
    print(f"✅ Conteúdo entregue para: {client_ip}")
    return conf["content"]

if __name__ == "__main__":
    conf = load_config()
    print("-" * 30)
    print("🚀 NDJ-LIB: SERVIDOR INICIADO")
    print(f"📡 Porta: {conf['local']}")
    print(f"🔑 Filtro de IP: {conf['key']}")
    print("-" * 30)
    
    # Roda o servidor na porta definida
    app.run(host='0.0.0.0', port=int(conf["local"]))
  
