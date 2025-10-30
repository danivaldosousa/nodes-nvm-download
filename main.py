#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Node.js Version Manager (NVM) - Python

Aplicação para fazer download de versões específicas do Node.js
e salvá-las no diretório d:/nvm.

Autor: Assistant
Data: 2025-10-30
"""

import os
import sys
import re
import requests
import zipfile
from pathlib import Path
from urllib.parse import urljoin
from tqdm import tqdm


class NodeDownloader:
    """Classe responsável pelo download e gerenciamento de versões do Node.js"""
    
    def __init__(self, base_dir="d:/nvm"):
        """
        Inicializa o downloader com o diretório base
        
        Args:
            base_dir (str): Diretório base onde as versões serão salvas
        """
        self.base_dir = Path(base_dir)
        self.base_url = "https://nodejs.org/dist/"
        
    def validate_version(self, version):
        """
        Valida se a versão está no formato correto (ex: 18.17.0)
        
        Args:
            version (str): Versão a ser validada
            
        Returns:
            bool: True se válida, False caso contrário
        """
        # Padrão: números.números.números (ex: 18.17.0)
        pattern = r'^\d+\.\d+\.\d+$'
        return bool(re.match(pattern, version))
    
    def create_directory(self, version):
        """
        Cria o diretório para a versão específica
        
        Args:
            version (str): Versão do Node.js
            
        Returns:
            Path: Caminho do diretório criado
        """
        version_dir = self.base_dir / f"node-v{version}"
        version_dir.mkdir(parents=True, exist_ok=True)
        return version_dir
    
    def get_download_url(self, version):
        """
        Constrói a URL de download para a versão especificada
        
        Args:
            version (str): Versão do Node.js
            
        Returns:
            str: URL completa para download
        """
        filename = f"node-v{version}-win-x64.zip"
        return urljoin(self.base_url, f"v{version}/{filename}")
    
    def check_version_exists(self, version):
        """
        Verifica se a versão existe no servidor
        
        Args:
            version (str): Versão do Node.js
            
        Returns:
            bool: True se existe, False caso contrário
        """
        url = self.get_download_url(version)
        try:
            response = requests.head(url, timeout=10)
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def download_file(self, url, destination):
        """
        Faz o download de um arquivo com barra de progresso
        
        Args:
            url (str): URL para download
            destination (Path): Caminho de destino
            
        Returns:
            bool: True se sucesso, False caso contrário
        """
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Obtém o tamanho total do arquivo
            total_size = int(response.headers.get('content-length', 0))
            
            # Configura a barra de progresso
            with tqdm(
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc="Baixando"
            ) as pbar:
                
                with open(destination, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            
            return True
            
        except requests.RequestException as e:
            print(f"Erro durante o download: {e}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    
    def extract_zip(self, zip_path, extract_to):
        """
        Extrai um arquivo ZIP
        
        Args:
            zip_path (Path): Caminho do arquivo ZIP
            extract_to (Path): Diretório de destino
            
        Returns:
            bool: True se sucesso, False caso contrário
        """
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Arquivo extraído em: {extract_to}")
            return True
        except zipfile.BadZipFile:
            print("Erro: Arquivo ZIP corrompido")
            return False
        except Exception as e:
            print(f"Erro ao extrair arquivo: {e}")
            return False
    
    def download_version(self, version, extract=True):
        """
        Faz o download completo de uma versão do Node.js
        
        Args:
            version (str): Versão do Node.js
            extract (bool): Se deve extrair o arquivo ZIP
            
        Returns:
            bool: True se sucesso, False caso contrário
        """
        # Valida a versão
        if not self.validate_version(version):
            print(f"Erro: Versão '{version}' inválida. Use o formato: X.Y.Z (ex: 18.17.0)")
            return False
        
        # Verifica se a versão existe
        print(f"Verificando se a versão {version} existe...")
        if not self.check_version_exists(version):
            print(f"Erro: Versão {version} não encontrada no servidor")
            return False
        
        # Cria o diretório
        version_dir = self.create_directory(version)
        print(f"Diretório criado: {version_dir}")
        
        # Define caminhos
        filename = f"node-v{version}-win-x64.zip"
        zip_path = version_dir / filename
        
        # Verifica se já foi baixado
        if zip_path.exists():
            print(f"Arquivo já existe: {zip_path}")
            if extract:
                return self.extract_zip(zip_path, version_dir)
            return True
        
        # Faz o download
        url = self.get_download_url(version)
        print(f"Baixando Node.js v{version}...")
        print(f"URL: {url}")
        
        if not self.download_file(url, zip_path):
            return False
        
        print(f"Download concluído! Arquivo salvo em: {zip_path}")
        
        # Extrai o arquivo se solicitado
        if extract:
            return self.extract_zip(zip_path, version_dir)
        
        return True


def main():
    """Função principal da aplicação"""
    print("=" * 60)
    print("Node.js Version Manager (NVM) - Python")
    print("=" * 60)
    print()
    
    # Cria o downloader
    downloader = NodeDownloader()
    
    # Garante que o diretório base existe
    downloader.base_dir.mkdir(parents=True, exist_ok=True)
    print(f"Diretório base: {downloader.base_dir}")
    print()
    
    while True:
        try:
            # Solicita a versão
            version = input("Digite a versão do Node.js (ex: 18.17.0) ou 'quit' para sair: ").strip()
            
            if version.lower() in ['quit', 'q', 'exit', 'sair']:
                print("Saindo...")
                break
            
            if not version:
                print("Por favor, digite uma versão válida.")
                continue
            
            # Faz o download
            success = downloader.download_version(version)
            
            if success:
                print(f"✅ Versão {version} baixada com sucesso!")
            else:
                print(f"❌ Falha ao baixar a versão {version}")
            
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            print("Tente novamente.")


if __name__ == "__main__":
    main()