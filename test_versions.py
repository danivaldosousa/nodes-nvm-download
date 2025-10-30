#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do Node.js Downloader com versões populares

Este script testa várias versões populares do Node.js
"""

from main_simple import NodeDownloader

def test_multiple_versions():
    """Testa várias versões populares"""
    downloader = NodeDownloader()
    
    print("=" * 60)
    print("TESTE - Node.js Version Manager (NVM) - Python")
    print("=" * 60)
    print()
    
    # Versões para testar (do mais recente ao mais antigo)
    test_versions = [
        "24.11.0",  # LTS atual
        "22.11.0",  # LTS anterior
        "20.18.0",  # LTS anterior
        "18.20.0",  # LTS anterior
        "16.20.0",  # LTS anterior
    ]
    
    print(f"Testando versões: {', '.join(test_versions)}")
    print()
    
    for version in test_versions:
        print(f"🔍 Verificando versão {version}...")
        
        if downloader.check_version_exists(version):
            print(f"✅ Versão {version} ENCONTRADA!")
            print(f"   URL: {downloader.get_download_url(version)}")
            
            # Cria o diretório
            version_dir = downloader.create_directory(version)
            print(f"   Diretório: {version_dir}")
            
            print(f"   Para baixar execute: downloader.download_version('{version}')")
            print()
            break  # Para no primeiro que encontrar
            
        else:
            print(f"❌ Versão {version} não encontrada")
    
    print("=" * 60)
    print("TESTE CONCLUÍDO")
    print("=" * 60)

if __name__ == "__main__":
    test_multiple_versions()