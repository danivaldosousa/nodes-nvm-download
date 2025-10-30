#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Verificação e Configuração do Node.js Downloader

Este script verifica se tudo está configurado corretamente e ajuda
na configuração inicial da aplicação.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python():
    """Verifica se Python está funcionando"""
    print("🐍 Verificando Python...")
    
    try:
        version = sys.version_info
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} encontrado")
        
        if version.major < 3 or (version.major == 3 and version.minor < 6):
            print("   ⚠️  Aviso: Python 3.6+ recomendado")
        else:
            print("   ✅ Versão compatível")
        return True
    except:
        print("   ❌ Erro ao verificar Python")
        return False

def check_files():
    """Verifica se os arquivos necessários existem"""
    print("\n📁 Verificando arquivos...")
    
    required_files = [
        "node.py",
        ".env.example",
        "README.md"
    ]
    
    optional_files = [
        ".env.simple",
        "demo_funcionamento.py",
        "config_examples.py",
        "requirements.txt"
    ]
    
    all_good = True
    
    for file in required_files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} (OBRIGATÓRIO)")
            all_good = False
    
    for file in optional_files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            print(f"   ⚠️  {file} (opcional)")
    
    return all_good

def check_env_config():
    """Verifica configuração do .env"""
    print("\n⚙️  Verificando configuração...")
    
    if Path(".env").exists():
        print("   ✅ Arquivo .env encontrado")
        
        # Lê configurações básicas
        try:
            with open(".env", "r", encoding="utf-8") as f:
                content = f.read()
                
            if "NVM_DIR=" in content and not content.split("NVM_DIR=")[1].split("\n")[0].strip().startswith("#"):
                print("   ✅ Diretório configurado")
            else:
                print("   ⚠️  Diretório não configurado (usará d:/nvm)")
                
            if "PROXY_HOST=" in content and not content.split("PROXY_HOST=")[1].split("\n")[0].strip().startswith("#"):
                print("   ✅ Proxy configurado")
            else:
                print("   ℹ️  Proxy não configurado (ok se não precisar)")
                
        except Exception as e:
            print(f"   ⚠️  Erro ao ler .env: {e}")
    else:
        print("   ⚠️  Arquivo .env não encontrado")
        print("   💡 Para criar: copy .env.example .env")

def test_basic_functionality():
    """Testa funcionalidade básica"""
    print("\n🧪 Testando funcionalidade básica...")
    
    try:
        # Importa o módulo principal
        sys.path.insert(0, ".")
        from node import NodeDownloader
        
        print("   ✅ Módulo node.py importado com sucesso")
        
        # Testa criação do downloader
        downloader = NodeDownloader()
        print(f"   ✅ NodeDownloader criado (diretório: {downloader.base_dir})")
        
        # Testa validação de versão
        if downloader.validate_version("18.17.0"):
            print("   ✅ Validação de versão funcionando")
        else:
            print("   ❌ Problema na validação de versão")
            
        return True
        
    except ImportError as e:
        print(f"   ❌ Erro ao importar módulo: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Erro inesperado: {e}")
        return False

def suggest_next_steps():
    """Sugere próximos passos"""
    print("\n🚀 Próximos Passos:")
    
    if not Path(".env").exists():
        print("\n1. 📋 Configure o ambiente:")
        print("   # Para uso simples:")
        print("   copy .env.simple .env")
        print("   # Para uso corporativo:")
        print("   copy .env.example .env")
        print("   # Depois edite o .env conforme necessário")
    
    print("\n2. 🧪 Teste a aplicação:")
    print("   # Demonstração offline:")
    print("   py demo_funcionamento.py")
    print("   ")
    print("   # Download real (versão pequena para teste):")
    print("   py node.py 8.17.0")
    
    print("\n3. 📖 Consulte a documentação:")
    print("   # Veja exemplos de configuração:")
    print("   py config_examples.py")
    print("   ")
    print("   # Leia o README.md para mais detalhes")
    
    print("\n4. 🎯 Uso normal:")
    print("   py node.py 18.17.0  # Para versão LTS")
    print("   py node.py 20.9.0   # Para versão mais recente")

def main():
    """Função principal"""
    print("🔧 VERIFICAÇÃO DE INSTALAÇÃO - Node.js Downloader")
    print("=" * 60)
    
    # Verificações
    python_ok = check_python()
    files_ok = check_files()
    
    if python_ok and files_ok:
        check_env_config()
        functionality_ok = test_basic_functionality()
        
        if functionality_ok:
            print("\n🎉 INSTALAÇÃO VERIFICADA COM SUCESSO!")
            print("   Todos os componentes estão funcionando.")
        else:
            print("\n⚠️  PROBLEMAS DETECTADOS")
            print("   Verifique os erros acima.")
    else:
        print("\n❌ PROBLEMAS CRÍTICOS DETECTADOS")
        print("   Resolva os problemas de arquivos/Python primeiro.")
    
    suggest_next_steps()
    
    print("\n" + "=" * 60)
    print("💡 Para suporte, consulte o README.md")

if __name__ == "__main__":
    main()