#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do Node.js Downloader

Este script demonstra como usar a classe NodeDownloader
sem interação do usuário.
"""

from main_simple import NodeDownloader

def test_download():
    """Função de teste para demonstrar o funcionamento"""
    downloader = NodeDownloader()
    
    print("=" * 60)
    print("TESTE - Node.js Version Manager (NVM) - Python")
    print("=" * 60)
    print()
    
    # Teste com versão válida
    test_version = "18.17.0"
    print(f"Testando download da versão {test_version}...")
    
    # Verifica se a versão existe
    if downloader.check_version_exists(test_version):
        print(f"✅ Versão {test_version} encontrada no servidor!")
        print(f"URL de download: {downloader.get_download_url(test_version)}")
        
        # Cria apenas o diretório (sem fazer download real)
        version_dir = downloader.create_directory(test_version)
        print(f"✅ Diretório criado: {version_dir}")
        
        print(f"📁 Para fazer o download real, execute:")
        print(f"   downloader.download_version('{test_version}')")
        
    else:
        print(f"❌ Versão {test_version} não encontrada")
    
    print()
    print("=" * 60)
    print("TESTE CONCLUÍDO")
    print("=" * 60)

if __name__ == "__main__":
    test_download()