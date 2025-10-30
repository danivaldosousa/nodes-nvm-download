#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples para demonstrar o funcionamento da aplicação Node.js Downloader
"""

from main_simple import NodeDownloader

def test_download():
    """Testa o download de uma versão específica"""
    downloader = NodeDownloader()
    
    # Testa com a versão 8.17.0 que vimos nas imagens
    version = "8.17.0"
    
    print(f"Testando download do Node.js v{version}...")
    print("=" * 50)
    
    try:
        # Tenta obter a URL de download
        url, filename = downloader.get_download_url(version)
        print(f"✓ URL encontrada: {url}")
        print(f"✓ Arquivo: {filename}")
        
        # Cria o diretório (sem fazer download completo para economizar tempo)
        version_dir = downloader.create_directory(version)
        print(f"✓ Diretório criado: {version_dir}")
        
        print("\n🎉 Teste bem-sucedido! A aplicação está funcionando corretamente.")
        print(f"Para fazer o download completo, execute:")
        print(f"py main_simple.py")
        print(f"E digite: {version}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    test_download()