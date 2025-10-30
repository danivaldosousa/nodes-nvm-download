#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Node.js Downloader - Versão Manual para Ambientes Corporativos

Esta versão ajuda você a baixar manualmente as versões do Node.js
quando há problemas de proxy/firewall corporativo.
"""

import os
import sys
from pathlib import Path

def show_manual_instructions(version):
    """Mostra instruções para download manual"""
    
    print("🏢 AMBIENTE CORPORATIVO DETECTADO")
    print("=" * 60)
    print(f"Não foi possível baixar automaticamente a versão {version}")
    print("devido a restrições de rede corporativa.")
    print()
    
    # Garante que a versão comece com 'v'
    if not version.startswith('v'):
        version_formatted = f'v{version}'
    else:
        version_formatted = version
    
    # URLs e instruções
    page_url = f"https://nodejs.org/download/release/{version_formatted}/"
    file_pattern = f"node-{version_formatted}-win-x64.zip"
    
    print("📋 INSTRUÇÕES PARA DOWNLOAD MANUAL:")
    print()
    print("1️⃣ ACESSE A PÁGINA:")
    print(f"   {page_url}")
    print()
    print("2️⃣ PROCURE E BAIXE O ARQUIVO:")
    print(f"   📁 {file_pattern}")
    print()
    print("3️⃣ SALVE O ARQUIVO EM:")
    base_dir = "d:/nvm"
    version_dir = f"node-v{version}"
    full_path = os.path.join(base_dir, version_dir)
    print(f"   📂 {full_path}/")
    print()
    print("4️⃣ EXECUTE O EXTRATOR:")
    print(f"   py node_extract.py \"{full_path}\\{file_pattern}\"")
    print()
    
    # Cria o diretório
    os.makedirs(full_path, exist_ok=True)
    print(f"✅ Diretório criado: {full_path}")
    print()
    
    print("🌐 ALTERNATIVAS DE DOWNLOAD:")
    print("• Use seu navegador web (geralmente funciona)")
    print("• Use um gerenciador de download (IDM, etc.)")
    print("• Peça para o TI liberar o acesso ao nodejs.org")
    print("• Use uma conexão pessoal (hotspot do celular)")
    print()
    
    return full_path

def main():
    """Função principal"""
    print("Node.js Downloader - Versão Manual")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        version = input("Digite a versão do Node.js (ex: 14.15.4): ").strip()
    else:
        version = sys.argv[1].strip()
    
    if not version:
        print("❌ Versão não informada")
        return
    
    show_manual_instructions(version)

if __name__ == "__main__":
    main()