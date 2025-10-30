#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Node.js Version Manager (NVM) - Python (Versão Simplificada)

Versão demonstrativa usando apenas bibliotecas padrão do Python.
Para a versão completa com barra de progresso, instale as dependências:
pip install requests tqdm

Autor: Assistant
Data: 2025-10-30
"""

import os
import sys
import re
import zipfile
from pathlib import Path
from urllib.request import urlopen, Request, build_opener, ProxyHandler, HTTPSHandler
from urllib.error import URLError, HTTPError
import ssl


def load_env_file(file_path=".env"):
    """
    Carrega variáveis de ambiente de um arquivo .env
    
    Args:
        file_path (str): Caminho do arquivo .env
    """
    env_path = Path(file_path)
    if not env_path.exists():
        return
    
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Ignora comentários e linhas vazias
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        # Remove aspas se existirem
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        os.environ[key] = value
    except Exception as e:
        print(f"⚠️  Erro ao ler arquivo .env: {e}")


def get_proxy_from_env():
    """
    Constrói URL do proxy a partir das variáveis de ambiente
    
    Returns:
        str: URL do proxy ou None
    """
    host = os.environ.get('PROXY_HOST')
    port = os.environ.get('PROXY_PORT')
    user = os.environ.get('PROXY_USER')
    password = os.environ.get('PROXY_PASS')
    
    if not host or not port:
        return None
    
    if user and password:
        return f"http://{user}:{password}@{host}:{port}"
    else:
        return f"http://{host}:{port}"


class NodeDownloader:
    """Classe responsável pelo download e gerenciamento de versões do Node.js"""
    
    def __init__(self, base_dir=None, proxy_url=None, ignore_ssl=False):
        """
        Inicializa o downloader com o diretório base
        
        Args:
            base_dir (str): Diretório base onde as versões serão salvas
            proxy_url (str): URL do proxy (ex: "http://proxy.empresa.com:8080")
            ignore_ssl (bool): Ignorar verificações SSL (apenas para desenvolvimento)
        """
        # Define diretório base: parâmetro > variável de ambiente > padrão
        if base_dir:
            self.base_dir = Path(base_dir)
        elif os.environ.get('NVM_DIR'):
            self.base_dir = Path(os.environ.get('NVM_DIR'))
        else:
            self.base_dir = Path("d:/nvm")
            
        self.base_url = "https://nodejs.org/download/release/"
        
        # Configuração de proxy e SSL
        self.opener = None
        if proxy_url or ignore_ssl:
            handlers = []
            
            # Configurar proxy se fornecido
            if proxy_url:
                proxy_handler = ProxyHandler({'http': proxy_url, 'https': proxy_url})
                handlers.append(proxy_handler)
                print(f"🌐 Usando proxy: {proxy_url}")
            
            # Configurar SSL se necessário
            if ignore_ssl:
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                https_handler = HTTPSHandler(context=ssl_context)
                handlers.append(https_handler)
                print("⚠️  Verificação SSL desabilitada (apenas para desenvolvimento)")
            
            if handlers:
                self.opener = build_opener(*handlers)
    
    def _open_url(self, url, timeout=10):
        """
        Abre uma URL usando as configurações de proxy/SSL
        
        Args:
            url (str): URL para abrir
            timeout (int): Timeout em segundos
            
        Returns:
            Response object
        """
        if self.opener:
            return self.opener.open(url, timeout=timeout)
        else:
            return urlopen(url, timeout=timeout)
        
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
        version_dir = self.base_dir / f"v{version}"
        version_dir.mkdir(parents=True, exist_ok=True)
        return version_dir
    
    def get_download_url(self, version):
        """
        Encontra a URL de download correta para a versão especificada
        
        Args:
            version (str): Versão do Node.js
            
        Returns:
            tuple: (URL completa para download, nome do arquivo)
        """
        # Garante que a versão comece com 'v'
        if not version.startswith('v'):
            version = f'v{version}'
        
        # URL da página da versão
        version_url = f"{self.base_url}{version}/"
        
        try:
            print(f"Verificando versão em: {version_url}")
            with self._open_url(version_url, timeout=10) as response:
                html_content = response.read().decode('utf-8')
                
            # Procura por links de arquivos ZIP para Windows x64
            zip_pattern = r'href="(node-v[\d.]+.*?-win-x64\.zip)"'
            zip_matches = re.findall(zip_pattern, html_content)
            
            if zip_matches:
                filename = zip_matches[0]
                # Verifica se o filename já contém caminho completo ou relativo
                if filename.startswith('http'):
                    # É uma URL completa
                    full_url = filename
                elif filename.startswith('/'):
                    # É um caminho absoluto do site
                    full_url = f"https://nodejs.org{filename}"
                else:
                    # É um arquivo relativo à página atual
                    full_url = version_url + filename
                return full_url, filename.split('/')[-1]  # Retorna apenas o nome do arquivo
            else:
                # Fallback: procura qualquer arquivo ZIP que contenha "win" e "x64"
                general_pattern = r'href="(.*?win.*?x64.*?\.zip)"'
                general_matches = re.findall(general_pattern, html_content)
                if general_matches:
                    filename = general_matches[0]
                    # Mesmo tratamento para o fallback
                    if filename.startswith('http'):
                        full_url = filename
                    elif filename.startswith('/'):
                        full_url = f"https://nodejs.org{filename}"
                    else:
                        full_url = version_url + filename
                    return full_url, filename.split('/')[-1]
                else:
                    raise Exception(f"Arquivo ZIP para Windows x64 não encontrado para a versão {version}")
                    
        except HTTPError as e:
            if e.code == 404:
                raise Exception(f"Versão {version} não encontrada no site do Node.js")
            else:
                raise Exception(f"Erro HTTP {e.code}: {e.reason}")
        except URLError as e:
            raise Exception(f"Erro de conexão: {e.reason}")
    
    def check_version_exists(self, version):
        """
        Verifica se a versão existe no servidor
        
        Args:
            version (str): Versão do Node.js
            
        Returns:
            bool: True se existe, False caso contrário
        """
        try:
            url, filename = self.get_download_url(version)
            # Faz uma requisição HEAD para verificar se o arquivo existe
            req = Request(url, method='HEAD')
            if self.opener:
                with self.opener.open(req, timeout=10) as response:
                    return response.status == 200
            else:
                with urlopen(req, timeout=10) as response:
                    return response.status == 200
        except Exception:
            return False
    
    def download_file(self, url, destination):
        """
        Faz o download de um arquivo usando urllib
        
        Args:
            url (str): URL para download
            destination (Path): Caminho de destino
            
        Returns:
            bool: True se sucesso, False caso contrário
        """
        try:
            print(f"Iniciando download de: {url}")
            
            with self._open_url(url, timeout=30) as response:
                # Obtém o tamanho total do arquivo
                content_length = response.headers.get('Content-Length')
                total_size = int(content_length) if content_length else 0
                
                # Lê e escreve o arquivo em chunks
                with open(destination, 'wb') as f:
                    downloaded = 0
                    chunk_size = 8192
                    
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        # Mostra progresso simples
                        if total_size > 0:
                            percentage = (downloaded / total_size) * 100
                            print(f"\rProgresso: {percentage:.1f}% ({downloaded // 1024 // 1024} MB)", end='', flush=True)
                        else:
                            print(f"\rBaixado: {downloaded // 1024 // 1024} MB", end='', flush=True)
                
                print()  # Nova linha após o progresso
            return True
            
        except (URLError, HTTPError) as e:
            print(f"\nErro durante o download: {e}")
            return False
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            return False
    
    def extract_zip(self, zip_path, extract_to):
        """
        Extrai um arquivo ZIP e organiza os arquivos
        
        Args:
            zip_path (Path): Caminho do arquivo ZIP
            extract_to (Path): Diretório de destino final
            
        Returns:
            bool: True se sucesso, False caso contrário
        """
        import shutil
        import tempfile
        
        try:
            print(f"Extraindo arquivo: {zip_path}")
            
            # Cria um diretório temporário para extração
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                
                # Extrai o ZIP no diretório temporário
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_path)
                
                # Procura pela pasta extraída (normalmente node-v{version}-win-x64)
                extracted_folders = [d for d in temp_path.iterdir() if d.is_dir()]
                
                if not extracted_folders:
                    print("Erro: Nenhuma pasta encontrada no arquivo ZIP")
                    return False
                
                source_folder = extracted_folders[0]  # Primeira (e geralmente única) pasta
                print(f"Movendo conteúdo de: {source_folder.name}")
                
                # Move todos os arquivos da pasta extraída para o destino final
                for item in source_folder.iterdir():
                    dest_item = extract_to / item.name
                    
                    if item.is_dir():
                        if dest_item.exists():
                            shutil.rmtree(dest_item)
                        shutil.copytree(item, dest_item)
                    else:
                        if dest_item.exists():
                            dest_item.unlink()
                        shutil.copy2(item, dest_item)
                
                print(f"Arquivos organizados em: {extract_to}")
            
            # Remove o arquivo ZIP após extração bem-sucedida
            try:
                zip_path.unlink()
                print(f"Arquivo ZIP removido: {zip_path}")
            except Exception as e:
                print(f"Aviso: Não foi possível remover o ZIP: {e}")
            
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
        import tempfile
        
        # Valida a versão
        if not self.validate_version(version):
            print(f"Erro: Versão '{version}' inválida. Use o formato: X.Y.Z (ex: 18.17.0)")
            return False
        
        # Verifica se a versão existe e obtém URL
        print(f"Verificando se a versão {version} existe...")
        try:
            url, filename = self.get_download_url(version)
        except Exception as e:
            print(f"Erro: {e}")
            print("Versões populares: 18.17.0, 20.9.0, 22.0.0")
            return False
        
        # Cria o diretório final
        version_dir = self.create_directory(version)
        print(f"Diretório de destino: {version_dir}")
        
        # Verifica se já foi instalado
        if any(version_dir.iterdir()):
            print(f"Versão já existe em: {version_dir}")
            node_exe = version_dir / "node.exe"
            if node_exe.exists():
                print("✅ Node.js já está instalado nesta versão")
                return True
        
        # Cria arquivo temporário para o ZIP
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_file:
            temp_zip_path = Path(temp_file.name)
        
        try:
            # Faz o download
            print(f"Baixando Node.js v{version}...")
            
            if not self.download_file(url, temp_zip_path):
                return False
            
            print(f"Download concluído!")
            
            # Extrai o arquivo se solicitado
            if extract:
                success = self.extract_zip(temp_zip_path, version_dir)
                if success:
                    print(f"✅ Node.js v{version} instalado com sucesso em: {version_dir}")
                    print(f"📁 Estrutura final:")
                    print(f"   {version_dir}/")
                    print(f"   ├── node.exe")
                    print(f"   ├── npm")
                    print(f"   └── node_modules/")
                return success
            
            return True
            
        finally:
            # Garante que o arquivo temporário seja removido
            try:
                if temp_zip_path.exists():
                    temp_zip_path.unlink()
            except:
                pass


def main():
    """Função principal da aplicação"""
    print("=" * 60)
    print("Node.js Version Manager (NVM) - Python")
    print("=" * 60)
    print("NOTA: Esta é uma versão simplificada.")
    print("Para barra de progresso avançada, instale: pip install requests tqdm")
    print()
    
    # Carrega configurações do arquivo .env
    load_env_file()
    
    # Configurações de proxy/SSL
    proxy_url = get_proxy_from_env()  # Primeiro tenta do .env
    ignore_ssl = os.environ.get('IGNORE_SSL', '').lower() == 'true'
    version = None
    
    # Parse de argumentos da linha de comando (sobrescreve .env se fornecido)
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg.startswith('--proxy='):
            proxy_url = arg.split('=', 1)[1]
        elif arg == '--ignore-ssl':
            ignore_ssl = True
        elif not arg.startswith('--'):
            version = arg
    
    # Mostra configurações carregadas
    if proxy_url:
        # Oculta senha na exibição
        display_proxy = proxy_url
        if '@' in proxy_url:
            parts = proxy_url.split('@')
            if ':' in parts[0]:
                user_pass = parts[0].split(':')
                if len(user_pass) >= 3:  # http://user:pass
                    display_proxy = f"{user_pass[0]}://{user_pass[1]}:***@{parts[1]}"
        print(f"🌐 Proxy configurado: {display_proxy}")
    
    if ignore_ssl:
        print("⚠️  Verificação SSL desabilitada")
    
    print()
    
    # Cria o downloader com configurações
    downloader = NodeDownloader(proxy_url=proxy_url, ignore_ssl=ignore_ssl)
    
    # Garante que o diretório base existe
    downloader.base_dir.mkdir(parents=True, exist_ok=True)
    print(f"Diretório base: {downloader.base_dir}")
    print()
    
    # Verifica se foi passada uma versão como argumento
    if version:
        print(f"Versão especificada via linha de comando: {version}")
        print()
        
        try:
            success = downloader.download_version(version)
            if success:
                print(f"✅ Versão {version} baixada com sucesso!")
            else:
                print(f"❌ Falha ao baixar a versão {version}")
        except Exception as e:
            print(f"Erro: {e}")
        return
    
    # Modo interativo
    print("💡 Configuração de Proxy:")
    print("   1. Crie um arquivo .env com suas credenciais")
    print("   2. Ou use: py node.py --proxy=http://user:pass@proxy:port versao")
    print("   3. Para ignorar SSL: py node.py --ignore-ssl versao")
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
                if not proxy_url:
                    print("💡 Configure o proxy no arquivo .env ou use --proxy")
            
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            print("Tente novamente.")


if __name__ == "__main__":
    main()