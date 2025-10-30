#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de configuração e uso da aplicação Node.js Downloader
"""

import os
from pathlib import Path

def show_configuration_examples():
    """Mostra exemplos de configuração"""
    
    print("🔧 NODE.JS VERSION MANAGER - Exemplos de Configuração")
    print("=" * 60)
    print()
    
    print("📋 1. ARQUIVO .env BÁSICO")
    print("-" * 30)
    print("""# Para uso doméstico
NVM_DIR=d:/nodejs""")
    print()
    
    print("📋 2. ARQUIVO .env CORPORATIVO")
    print("-" * 30)
    print("""# Para ambiente corporativo
PROXY_HOST=proxy.empresa.com.br
PROXY_PORT=8080
PROXY_USER=seu.usuario
PROXY_PASS=SuaSenha123
NVM_DIR=c:/ferramentas/nodejs""")
    print()
    
    print("📋 3. ARQUIVO .env DESENVOLVIMENTO")
    print("-" * 30)
    print("""# Para desenvolvimento local
NVM_DIR=./local_nodejs
IGNORE_SSL=true""")
    print()
    
    print("🚀 4. COMANDOS DE EXEMPLO")
    print("-" * 30)
    print("# Download simples:")
    print("py node.py 18.17.0")
    print()
    print("# Com proxy na linha de comando:")
    print("py node.py --proxy=http://user:pass@proxy:8080 18.17.0")
    print()
    print("# Ignorando SSL:")
    print("py node.py --ignore-ssl 18.17.0")
    print()
    print("# Modo interativo:")
    print("py node.py")
    print()
    
    print("📁 5. ESTRUTURAS DE DIRETÓRIO")
    print("-" * 30)
    print("Padrão (d:/nvm):")
    print("d:/nvm/")
    print("├── v18.17.0/")
    print("│   ├── node.exe")
    print("│   └── npm.cmd")
    print("└── v20.9.0/")
    print("    ├── node.exe")
    print("    └── npm.cmd")
    print()
    
    print("Personalizado (NVM_DIR=c:/nodejs):")
    print("c:/nodejs/")
    print("├── v16.20.0/")
    print("│   ├── node.exe")
    print("│   └── npm.cmd")
    print("└── v18.17.0/")
    print("    ├── node.exe")
    print("    └── npm.cmd")
    print()
    
    print("💡 6. DICAS DE USO")
    print("-" * 30)
    print("• Use versões LTS para produção: 18.17.0, 20.9.0")
    print("• Configure o .env uma vez e reutilize")
    print("• Em redes corporativas, configure o proxy")
    print("• Use --ignore-ssl apenas se necessário")
    print("• O diretório é criado automaticamente")
    print()

def show_current_config():
    """Mostra a configuração atual"""
    
    print("⚙️  CONFIGURAÇÃO ATUAL")
    print("-" * 30)
    
    # Carrega o .env se existir
    env_file = Path(".env")
    if env_file.exists():
        print("✅ Arquivo .env encontrado")
        
        # Simula carregamento do .env
        config = {}
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
        except:
            pass
        
        print(f"📂 Diretório: {config.get('NVM_DIR', 'd:/nvm')}")
        print(f"🌐 Proxy: {'Configurado' if config.get('PROXY_HOST') else 'Não configurado'}")
        print(f"🔒 SSL: {'Ignorado' if config.get('IGNORE_SSL') == 'true' else 'Verificado'}")
    else:
        print("⚠️  Arquivo .env não encontrado")
        print("📂 Diretório padrão: d:/nvm")
        print("🌐 Proxy: Não configurado")
    
    print()

if __name__ == "__main__":
    show_current_config()
    show_configuration_examples()