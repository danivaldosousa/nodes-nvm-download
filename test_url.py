#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste da construção de URL
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from node import NodeDownloader

def test_url_construction():
    """Testa a construção da URL"""
    
    # Carrega configurações do .env
    from node import load_env_file, get_proxy_from_env
    load_env_file()
    
    proxy_url = get_proxy_from_env()
    ignore_ssl = os.environ.get('IGNORE_SSL', '').lower() == 'true'
    
    print("🔧 Testando construção de URL...")
    print(f"Proxy: {proxy_url}")
    print(f"Ignore SSL: {ignore_ssl}")
    print()
    
    downloader = NodeDownloader(proxy_url=proxy_url, ignore_ssl=ignore_ssl)
    
    try:
        url, filename = downloader.get_download_url("14.15.4")
        print(f"✅ URL construída: {url}")
        print(f"✅ Nome do arquivo: {filename}")
        print()
        print("🎯 URL esperada: https://nodejs.org/download/release/v14.15.4/node-v14.15.4-win-x64.zip")
        
        if url == "https://nodejs.org/download/release/v14.15.4/node-v14.15.4-win-x64.zip":
            print("✅ URL CORRETA!")
        else:
            print("❌ URL incorreta")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    test_url_construction()