# 🚀 Gerenciador de downloads do Node.js Versões Antigas para ser usado com NVM - Python

Uma aplicação Python para download automático de versões específicas do Node.js.

## 📋 Pré-requisitos

### 🐍 **Python**

Esta aplicação requer Python 3.6 ou superior:

```bash
# Verificar se Python está instalado
python --version
# ou
py --version

# Se não estiver instalado, baixe em:
# https://www.python.org/downloads/
```

### 💻 **Sistema Operacional**

- ✅ **Windows 10/11** (testado e recomendado)
- ✅ **Windows 8.1/Server** (compatível)
- ❓ **Linux/macOS** (não testado, mas pode funcionar)

## 📥 Instalação

### 1. **Clone ou Baixe o Repositório**

```bash
# Opção 1: Clone via Git
git clone https://github.com/danivaldosousa/nodes-nvm-download.git
cd nodes-nvm-download

# Opção 2: Download direto
# Baixe o ZIP do GitHub e extraia
```

### 2. **Verificar Estrutura dos Arquivos**

Certifique-se que você tem os seguintes arquivos:

```
nodes-nvm-download/
├── 📄 node.py              # ⭐ Aplicação principal
├── 📄 .env.example         # ⭐ Modelo de configuração
├── 📄 .env.simple          # ⭐ Configuração simples
├── 📄 install_check.py     # 🔧 Verificação de instalação
├── 📄 README.md            # 📖 Documentação
├── 📄 requirements.txt     # 📦 Dependências (opcional)
├── 📄 config_examples.py   # 🔧 Exemplos de configuração
├── 📄 demo_funcionamento.py # 🎯 Demonstração
└── 📄 .gitignore           # 🚫 Arquivos ignorados
```

### 3. **Instalar Dependências (Opcional)**

A aplicação funciona apenas com bibliotecas padrão do Python, mas você pode instalar dependências extras para melhor experiência:

```bash
# Opcional: Para barra de progresso avançada
pip install -r requirements.txt

# Ou instalação manual:
pip install requests tqdm
```

**⚠️ Nota:** Se você estiver em uma rede corporativa e não conseguir instalar via pip, a aplicação funcionará normalmente sem essas dependências.

### 4. **Verificar Instalação**

```bash
# Teste automatizado - verifica tudo de uma vez
py install_check.py

# Ou testes manuais:
py node.py --help
py demo_funcionamento.py
```

## ⚡ Início Rápido

### 🏠 **Para Uso Doméstico (Sem Proxy)**

Se você está em casa ou em uma rede sem proxy:

```bash
# Download direto - sem configuração necessária
py node.py 18.17.0
```

O Node.js será instalado em: `d:/nvm/v18.17.0/`

### 🏢 **Para Ambiente Corporativo (Com Proxy)**

Se você está em uma empresa com proxy:

1. **Configure o arquivo .env:**
```bash
copy .env.example .env
# Edite o .env com suas credenciais de proxy
```

2. **Use normalmente:**
```bash
py node.py 18.17.0
```

## ✅ Testando a Instalação

Após a instalação, teste se tudo está funcionando:

### 🧪 **Teste Básico**

```bash
# 1. Verifique se a aplicação responde
py node.py --help

# 2. Execute a demonstração offline (sem internet)
py demo_funcionamento.py

# 3. Veja exemplos de configuração
py config_examples.py
```

### 🌐 **Teste com Download Real**

```bash
# Para redes sem proxy
py node.py 18.17.0

# Para redes com proxy (configure .env primeiro)
copy .env.example .env
# Edite o .env, depois:
py node.py 18.17.0
```

### 📁 **Verificar Resultado**

Se tudo funcionou, você deve ter:

```
d:/nvm/v18.17.0/
├── 📄 node.exe
├── 📄 npm.cmd
├── 📁 node_modules/
└── 📄 outros arquivos...
```

### 🚨 **Se algo der errado:**

1. **Verifique a seção "Problemas de Instalação" abaixo**
2. **Execute a demonstração offline:** `py demo_funcionamento.py`
3. **Consulte os exemplos:** `py config_examples.py`

---

## ✨ Funcionalidades

- ✅ **Download automático** de qualquer versão do Node.js
- ✅ **Suporte completo a proxy** com autenticação
- ✅ **Detecção automática** do arquivo correto para Windows x64
- ✅ **Parsing inteligente** da página de release do Node.js
- ✅ **Extração automática** e organização limpa dos arquivos
- ✅ **Configuração via arquivo .env** (seguro para credenciais)
- ✅ **Diretório configurável** para instalação
- ✅ **Interface de linha de comando** amigável

## 📁 Estrutura de Saída

```
📂 Seu Diretório Configurado (ex: d:/nvm/)
├── 📁 v8.17.0/
│   ├── 📄 node.exe
│   ├── 📄 npm.cmd
│   └── 📁 node_modules/
├── 📁 v14.15.4/
│   ├── 📄 node.exe
│   ├── 📄 npm.cmd
│   └── 📁 node_modules/
└── 📁 v18.17.0/
    ├── 📄 node.exe
    ├── 📄 npm.cmd
    └── 📁 node_modules/
```

## ⚙️ Instalação e Configuração

### 1. 📥 Download dos Arquivos

Baixe ou clone este repositório:
```bash
git clone <url-do-repositorio>
cd nodes-nvm
```

### 2. 🔧 Configuração do Ambiente

#### Opção A: Arquivo .env (Recomendado)

1. **Copie o arquivo de exemplo:**
```bash
copy .env.example .env
```

2. **Edite o arquivo `.env`** com suas configurações:

##### 🏠 **Para Uso Doméstico (SEM Proxy):**
```env
# Configuração simples - apenas o diretório
NVM_DIR=d:/nodejs
```

##### 🏢 **Para Ambiente Corporativo (COM Proxy):**
```env
# Configurações de Proxy
PROXY_HOST=proxy.empresa.com
PROXY_PORT=8080
PROXY_USER=seu_usuario
PROXY_PASS=sua_senha

# Diretório de instalação
NVM_DIR=d:/nodejs
```

##### 🔧 **Para Desenvolvimento:**
```env
# Desenvolvimento local
NVM_DIR=./nodejs
IGNORE_SSL=true
```

#### Opção B: Variáveis de Ambiente do Sistema

##### 🏠 **Uso Doméstico:**
```bash
# Windows PowerShell - apenas diretório
$env:NVM_DIR = "d:/nodejs"
```

##### 🏢 **Ambiente Corporativo:**
```bash
# Windows PowerShell - com proxy
$env:NVM_DIR = "d:/nodejs"
$env:PROXY_HOST = "proxy.empresa.com"
$env:PROXY_PORT = "8080"
$env:PROXY_USER = "seu_usuario"
$env:PROXY_PASS = "sua_senha"
```

#### ⚡ **Configuração Rápida (Sem Arquivo .env)**

Se você não quer criar arquivo `.env`, pode usar diretamente:

```bash
# Uso simples (sem proxy)
py node.py 18.17.0

# Com diretório personalizado
py node.py --dir=c:/nodejs 18.17.0

# Com proxy (linha de comando)
py node.py --proxy=http://usuario:senha@proxy.com:8080 18.17.0
```

## 🚀 Como Usar

### 📋 Sintaxe Básica

```bash
py node.py [opções] <versão>
```

### ⚡ **Uso Rápido (Sem Configuração)**

Se você não precisa de proxy, pode usar diretamente:

```bash
# Download simples - usa diretório padrão (d:/nvm)
py node.py 18.17.0

# Com diretório personalizado
py node.py --dir=c:/nodejs 18.17.0

# Modo interativo
py node.py
```

### 🔧 **Uso Avançado (Com Configuração)**

Para uso frequente, configure o arquivo `.env` uma vez:

1. **Crie o .env:**
```bash
copy .env.example .env
```

2. **Configure conforme sua necessidade:**
```env
# Configuração mínima (sem proxy)
NVM_DIR=d:/nodejs

# OU configuração completa (com proxy)
PROXY_HOST=proxy.empresa.com
PROXY_PORT=8080
PROXY_USER=seu_usuario
PROXY_PASS=sua_senha
NVM_DIR=d:/nodejs
```

3. **Use normalmente:**
```bash
py node.py 18.17.0
```

### 🎯 Exemplos Práticos

#### 1. 🏠 **Uso Doméstico (Sem Proxy)**
```bash
# Download simples - funciona na maioria das redes domésticas
py node.py 18.17.0
```

#### 2. 🏢 **Ambiente Corporativo (Com Proxy)**
```bash
# Configure o .env primeiro, depois:
py node.py 18.17.0

# Ou use proxy na linha de comando:
py node.py --proxy=http://usuario:senha@proxy.com:8080 18.17.0
```

#### 3. 🔧 **Download com Opções Específicas**
```bash
# Ignorando SSL (para redes com certificados corporativos)
py node.py --ignore-ssl 18.17.0

# Combinando proxy e SSL
py node.py --proxy=http://user:pass@proxy:8080 --ignore-ssl 18.17.0
```

#### 4. 💻 **Modo Interativo**
```bash
# A aplicação pergunta a versão
py node.py
# Digite a versão quando solicitado
```

#### 5. 📁 **Diretório Personalizado via Linha de Comando**
```bash
# Especificar diretório sem usar .env
py node.py --dir=c:/meus-nodejs 18.17.0
```

### 📋 Versões Populares

```bash
# Versões LTS Recomendadas
py node.py 18.17.0    # Current LTS
py node.py 20.9.0     # Latest LTS
py node.py 16.20.2    # Previous LTS

# Versões Específicas
py node.py 14.15.4    # Legacy
py node.py 22.0.0     # Latest
py node.py 8.17.0     # Very Old
```

## 🌐 Configuração de Proxy

### Para Ambientes Corporativos

#### 1. 🔍 Descobrir Configurações de Proxy

**Método 1: Configurações do Windows**
- Configurações → Rede e Internet → Proxy
- Anote servidor e porta

**Método 2: Linha de Comando**
```bash
netsh winhttp show proxy
```

**Método 3: Internet Explorer**
- Ferramentas → Opções da Internet → Conexões → Configurações LAN

#### 2. 📝 Configurar no .env

```env
PROXY_HOST=proxy.suaempresa.com.br
PROXY_PORT=8080
PROXY_USER=seu.usuario
PROXY_PASS=SuaSenha123
```

#### 3. 🔒 Problemas Comuns

**Erro 407 Authentication Required:**
```bash
# Certifique-se que usuário e senha estão corretos
py node.py --proxy=http://usuario:senha@proxy:8080 18.17.0
```

**Erro SSL:**
```bash
# Use --ignore-ssl para contornar problemas de certificado
py node.py --ignore-ssl 18.17.0
```

## 🛠️ Opções da Linha de Comando

| Opção | Descrição | Exemplo |
|-------|-----------|---------|
| `--proxy=URL` | Configurar proxy | `--proxy=http://user:pass@proxy:8080` |
| `--ignore-ssl` | Ignorar verificação SSL | `--ignore-ssl` |
| `versão` | Versão do Node.js | `18.17.0` |

## 📖 Configurações do .env

| Variável | Descrição | Exemplo | Padrão |
|----------|-----------|---------|--------|
| `NVM_DIR` | Diretório de instalação | `d:/nodejs` | `d:/nvm` |
| `PROXY_HOST` | Servidor proxy | `proxy.empresa.com` | - |
| `PROXY_PORT` | Porta do proxy | `8080` | - |
| `PROXY_USER` | Usuário do proxy | `joao.silva` | - |
| `PROXY_PASS` | Senha do proxy | `MinhaSenh@123` | - |
| `IGNORE_SSL` | Ignorar verificação SSL | `true` | `false` |

## 🎯 Casos de Uso

### � **Uso Doméstico (Sem Proxy)**

**Configuração mínima:**
```env
# .env
NVM_DIR=d:/nodejs
```

**Uso:**
```bash
py node.py 18.17.0
```

**Resultado:** Node.js instalado em `d:/nodejs/v18.17.0/`

### �💼 **Ambiente Corporativo (Com Proxy)**

**Configuração completa:**
```env
# .env para empresa
PROXY_HOST=proxy.empresa.com.br
PROXY_PORT=8080
PROXY_USER=seu.usuario
PROXY_PASS=SuaSenha123
NVM_DIR=c:/ferramentas/nodejs
```

**Uso:**
```bash
py node.py 18.17.0
```

**Resultado:** Node.js instalado em `c:/ferramentas/nodejs/v18.17.0/`

### 🔧 **Desenvolvimento Local**

**Configuração para desenvolvimento:**
```env
# .env para desenvolvimento
NVM_DIR=./local_nodejs
IGNORE_SSL=true
```

**Uso:**
```bash
py node.py 22.0.0
```

**Resultado:** Node.js instalado em `./local_nodejs/v22.0.0/`

### ⚡ **Uso Sem Configuração**

**Sem arquivo .env:**
```bash
# Usa diretório padrão (d:/nvm)
py node.py 20.9.0

# Com diretório personalizado
py node.py --dir=c:/temp/node 20.9.0

# Com proxy (linha de comando)
py node.py --proxy=http://user:pass@proxy:8080 20.9.0
```

## �️ Problemas de Instalação

### ❌ **Python não encontrado**

**Erro:** `'python' is not recognized as an internal or external command`

**Soluções:**

1. **Instalar Python:**
   - Baixe em: https://www.python.org/downloads/
   - ✅ Marque "Add Python to PATH" durante instalação

2. **Verificar instalação:**
```bash
python --version
py --version
python3 --version
```

3. **Usar comando alternativo:**
```bash
# Se python não funcionar, tente:
py node.py 18.17.0
python3 node.py 18.17.0
```

### ❌ **Erro ao instalar dependências via pip**

**Erro:** `pip install failed` ou `proxy error`

**Soluções:**

1. **Usar sem dependências extras:**
```bash
# A aplicação funciona apenas com Python padrão
py node.py 18.17.0
```

2. **Configurar proxy para pip:**
```bash
pip install --proxy http://user:pass@proxy:8080 requests tqdm
```

3. **Instalar apenas para o usuário:**
```bash
pip install --user requests tqdm
```

### ❌ **Permissão negada ao executar**

**Erro:** `Permission denied` ou `Access is denied`

**Soluções:**

1. **Executar como administrador:**
   - Clique direito no PowerShell → "Executar como administrador"

2. **Usar diretório com permissão:**
```bash
# Configure no .env um diretório acessível
NVM_DIR=c:/temp/nodejs
```

3. **Verificar antivírus:**
   - Adicione o diretório do projeto às exceções

### ❌ **Arquivo node.py não encontrado**

**Erro:** `can't open file 'node.py': [Errno 2] No such file or directory`

**Soluções:**

1. **Verificar diretório atual:**
```bash
# Certifique-se que está na pasta do projeto
cd path/to/nodes-nvm-download
dir  # Deve mostrar node.py
```

2. **Usar caminho completo:**
```bash
py c:/caminho/completo/para/node.py 18.17.0
```

## �🔍 Resolução de Problemas

### ❌ Erro: "Tunnel connection failed: 407 authenticationrequired"

**Causa:** Proxy com autenticação não configurado
**Solução:**
```bash
# Configure o proxy no .env ou use linha de comando
py node.py --proxy=http://usuario:senha@proxy:8080 18.17.0
```

### ❌ Erro: "SSL verification failed"

**Causa:** Problemas de certificado SSL
**Solução:**
```bash
py node.py --ignore-ssl 18.17.0
```

### ❌ Erro: "Versão não encontrada"

**Causa:** Versão inexistente ou mal formatada
**Solução:**
```bash
# Use formato X.Y.Z (sem 'v')
py node.py 18.17.0  # ✅ Correto
py node.py v18.17.0 # ❌ Incorreto
```

### ❌ Erro: "Permission denied"

**Causa:** Falta de permissão no diretório
**Solução:**
```bash
# Execute como administrador ou mude o diretório
# No .env:
NVM_DIR=c:/temp/nodejs
```

## � Estrutura do Projeto

```
nodes-nvm/
├── 📄 node.py              # Aplicação principal
├── 📄 .env                 # Configurações (crie a partir do exemplo)
├── 📄 .env.example         # Exemplo de configuração
├── 📄 README.md            # Este arquivo
├── 📄 requirements.txt     # Dependências (opcional)
├── 📄 demo_funcionamento.py # Demonstração offline
└── 📄 test_*.py           # Arquivos de teste
```

## 🔒 Segurança

### ⚠️ Importante para Credenciais

1. **Nunca commite o arquivo `.env`** em repositórios
2. **Use permissions restritas** no arquivo `.env`
3. **Considere usar variáveis de ambiente** do sistema para produção

```bash
# Windows - definir permissões do arquivo .env
icacls .env /inheritance:r /grant:r "%USERNAME%":F
```

## 🚀 Uso Avançado

### 📝 Como Módulo Python

```python
from node import NodeDownloader

# Configuração básica
downloader = NodeDownloader(base_dir="c:/nodejs")

# Com proxy
downloader = NodeDownloader(
    base_dir="c:/nodejs",
    proxy_url="http://user:pass@proxy:8080",
    ignore_ssl=True
)

# Download
success = downloader.download_version("18.17.0")
if success:
    print("✅ Node.js instalado com sucesso!")
```

### � Automação

```bash
# Script para instalar múltiplas versões
for version in 16.20.2 18.17.0 20.9.0; do
    py node.py $version
done
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## 🆘 Suporte

- 📧 **Issues**: Use o sistema de issues do GitHub
- 📚 **Documentação**: Este README
- 🔧 **Debug**: Use `py node.py --help` para ajuda

---

**Desenvolvido com ❤️ para facilitar o gerenciamento de versões do Node.js em ambientes corporativos**

O script irá:
- Solicitar a versão do Node.js (ex: 18.17.0, 20.9.0)
- Fazer o download do arquivo ZIP para Windows x64
- Salvar no diretório `d:/nvm/node-v{versão}/`
- Extrair o arquivo automaticamente

## Estrutura de diretórios

```
d:/nvm/
├── node-v18.17.0/
│   └── node-v18.17.0-win-x64.zip
├── node-v20.9.0/
│   └── node-v20.9.0-win-x64.zip
└── ...
```

## Dependências

- `requests`: Para fazer downloads HTTP
- `tqdm`: Para mostrar progresso do download

## Exemplo de uso

```
Digite a versão do Node.js (ex: 18.17.0): 20.9.0
Baixando Node.js v20.9.0...
100%|██████████| 28.1MB/28.1MB [00:15<00:00, 1.87MB/s]
Download concluído! Arquivo salvo em: d:/nvm/node-v20.9.0/
```