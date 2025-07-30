# 🐍 PyPixBot

<p align="center">
  <a href="https://github.com/cleitonleonel/PyPixBot">
    <img src="src/media/logo.png" alt="PyPixBot logo" width="45%" height="auto">
  </a>
</p>

<p align="center">
  <i>Um bot para criar qrcodes do Pix no Telegram.</i>
</p>

<p align="center">
<a href="https://github.com/cleitonleonel/PyPixBot">
  <img src="https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-green" alt="Supported Python Versions"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
  <img src="https://img.shields.io/github/stars/cleitonleonel/PyPixBot" alt="GitHub Stars"/>
</a>
</p>

---

# 📋 Documentação do PyPixBot

## 📖 Visão Geral

O **PyPixBot** é um bot para Telegram desenvolvido em Python que oferece funcionalidades para geração de códigos QR de pagamentos PIX. O bot permite criar QR codes estáticos e dinâmicos com diferentes opções de personalização.

### 🎯 Objetivo
Facilitar a criação de códigos de pagamento PIX através de uma interface amigável no Telegram, permitindo que usuários gerem QR codes para receber pagamentos de forma rápida e eficiente.

## 🔧 Arquitetura do Projeto

### 📁 Estrutura de Diretórios

```
PyPixBot/
├── 📄 main.py                    # Arquivo principal de execução
├── 📄 constants.py               # Constantes e comandos do bot
├── 📄 config_dev.toml           # Configurações de desenvolvimento
├── 📄 pyproject.toml            # Configurações do Poetry
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 LICENSE                   # Licença MIT
├── 📄 README.md                 # Documentação inicial
├── 📄 .gitignore               # Arquivos ignorados pelo Git
├── 📂 pypixbot/                # Pacote principal
│   ├── 📂 plugins/             # Plugins e handlers
│   │   └── 📂 commands/        # Comandos do bot
│   │       ├── start_handler.py
│   │       ├── help_handler.py
│   │       ├── qrcode_handler.py
│   │       └── restart_handler.py
│   └── 📂 services/            # Serviços e utilitários
└── 📂 src/                     # Recursos e mídia
    └── 📂 media/               # Imagens e arquivos de mídia
```


### 🏗️ Componentes Principais

#### 1. **Main.py** - Arquivo Principal
- Configuração do cliente Telegram
- Definição dos estados de conversação
- Configuração de plugins e comandos
- Inicialização do serviço

#### 2. **Constants.py** - Comandos do Bot
- `ADMIN_COMMANDS`: Comandos administrativos
- `DEFAULT_COMMANDS`: Comandos padrão para usuários

#### 3. **Handlers** - Manipuladores de Comandos
- **start_handler.py**: Gerencia o comando `/start`
- **help_handler.py**: Gerencia o comando `/help`
- **qrcode_handler.py**: Gerencia a criação de QR codes PIX
- **restart_handler.py**: Gerencia o comando `/restart`

#### 4. **Services** - Serviços de Negócio
- **pix_service.py**: Lógica de criação de códigos PIX
- **converter.py**: Conversão de formatos de mídia

## 🛠️ Tecnologias Utilizadas

### 📚 Dependências Principais
- **Telethon**: Cliente para API do Telegram
- **PyPix**: Biblioteca para geração de códigos PIX
- **SmartBot**: Framework para bots Telegram
- **ImageIO**: Processamento de imagens
- **Schedule**: Agendamento de tarefas
- **TOML**: Manipulação de arquivos de configuração

### 🐍 Versão Python
- **Python 3.12+** (recomendado)
- Compatível com Poetry para gerenciamento de dependências

## ⚙️ Configuração

### 📋 Arquivo de Configuração (config_dev.toml)

```toml
[API]
ID = 123456                    # ID da API do Telegram
HASH = "API Hash Telegram"     # Hash da API
BOT_TOKEN = "Token do Bot"     # Token do BotFather

[ADMIN]
IDS = [2222222222]             # IDs dos administradores

[APPLICATION]
APP_NAME = "SmartBot"
APP_AUTHOR = "Cleiton Leonel Creton"
APP_VERSION = "0.1.0"
DEVICE_MODEL = "Telegram Desktop 5.1.7 Snap"
SYSTEM_VERSION = "Linux Ubuntu GNOME"
```


### 🔑 Estados de Conversação

```python
class ConversationState(Enum):
    IDLE = "idle"                    # Estado inativo
    WAITING_PIX_KEY = "waiting_pix_key"   # Aguardando chave PIX
    WAITING_AMOUNT = "waiting_amount"      # Aguardando valor
    WAITING_YES_NO = "waiting_yes_no"      # Aguardando confirmação
    WAITING_LOGO = "waiting_logo"          # Aguardando logo
    IN_MENU = "in_menu"                    # No menu
    PROCESSING = "processing"              # Processando
```

## 🚀 Funcionalidades

- ✅ Criação de QR Codes do Pix
- ✅ Geração de códigos estáticos e dinâmicos
- ✅ Suporte a múltiplas chaves Pix
- 🔄 Checar se foi pago (em desenvolvimento para nubank)
- 📈 Dashboard para visualização de transações (planejada)
- 📊 Exportação de transações para CSV (planejada)
- 📅 Agendamento de pagamentos (planejado)
- 🔔 Notificações de transações (planejada)

### 📱 Comandos Disponíveis

#### Para Usuários Comuns:
- `/start` - Iniciar conversa com o bot
- `/create_pix` - Gerar novo QR code PIX
- `/help` - Exibir ajuda e informações

#### Para Administradores:
- `/restart` - Limpar cache e reiniciar o bot

### 🎨 Personalização de QR Codes
- **Estilos de Marcadores**: Quarter Circle
- **Bordas**: Arredondadas
- **Gradientes**: Modo normal com cores personalizáveis
- **Frames**: Scan Me Purple
- **Logos**: Suporte a PNG e GIF

## 🔄 Fluxo de Funcionamento

### 1. **Inicialização**
```python
# O bot é iniciado através do main.py
client = Client(
    bot_token=BOT_TOKEN,
    session=SESSION_PATH,
    # ... outras configurações
)
client.start_service()
```


### 2. **Processamento de Comandos**
- Usuário envia comando
- Handler apropriado é acionado
- Estado da conversação é atualizado
- Resposta é enviada ao usuário

### 3. **Geração de QR Code PIX**
```python
def create_qrcode_pix(config: dict) -> tuple:
    # Configura dados do PIX
    pix.set_name_receiver(config.get("receiver"))
    pix.set_key(config.get("key"))
    # ... outras configurações
    
    # Gera QR code estilizado
    base64qr = pix.save_qrcode(
        data=br_code,
        output=qrcode_path,
        # ... estilos personalizados
    )
    
    return br_code, qrcode_path
```


## 📝 Instalação e Execução

### 1. **Clonagem do Repositório**
```shell script
git clone https://github.com/cleitonleonel/PyPixBot.git
cd PyPixBot
```


### 2. **Instalação com Poetry**
```shell script
poetry install
```


### 3. **Configuração**
- Editar `config_dev.toml` com suas credenciais
- Obter API ID e Hash do Telegram
- Criar bot via BotFather

### 4. **Execução**
```shell script
python main.py
```


## 🔒 Segurança

### 🛡️ Práticas Implementadas
- Validação de IDs de administradores
- Gerenciamento seguro de sessões de usuário
- Logs de atividades para auditoria
- Tratamento de exceções

### 🔐 Configurações Sensíveis
- Tokens e chaves mantidos em arquivos de configuração
- Arquivos de configuração no `.gitignore`
- Separação entre ambiente de desenvolvimento e produção

## 📊 Monitoramento e Logs

### 📋 Sistema de Logging
```python
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exemplo de log
logging.info(f"Start Handler Triggered by User ID: {sender_id}")
```


### 🔍 Tipos de Logs
- **INFO**: Eventos normais do sistema
- **ERROR**: Erros de processamento
- **WARNING**: Situações de atenção

## 🤝 Contribuição

### 📝 Guidelines

1. 🍴 Faça um fork do projeto
2. 🌟 Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. ✍️ Commit suas mudanças:
   ```bash
   git commit -am '✨ Adiciona nova feature'
   ```
4. 📤 Push para a branch:
   ```bash
   git push origin feature/nova-feature
   ```
5. 🔄 Faça testes unitários e verifique a formatação do código:
   ```bash
   pytest tests/
   black src/
   flake8 src/
   ```
6. 🔁 Abra um Pull Request no GitHub
   - Acesse o seu repositório: https://github.com/seu_usuario/PyPixBot

   - Você verá uma notificação com:
"Compare & pull request" — clique nela.
Ou vá em "Pull requests" > "New pull request".

   - Selecione a branch base (ex: main) e compare com o projeto PyPixBot.

   - Preencha o título e a descrição (exemplo abaixo).

   - Clique em "Create Pull Request".

7. 📝 Atualize a documentação, se necessário.

## 📦 Testes

### 🧪 Testes Unitários
- Utiliza `pytest` para testes unitários
- Estrutura de testes em `tests/`
- Exemplo de teste:

```python
def test_create_qrcode_pix():
    config = {
        "receiver": "Test Receiver",
        "key": "test_key",
        "amount": 100.0,
        "message": "Test Message",
        "logo": "test_logo.png"
    }
    br_code, qrcode_path = create_qrcode_pix(config)
    assert br_code is not None
    assert os.path.exists(qrcode_path)
```

### 📂 Estrutura de Testes
```tests/
├── 📄 __init__.py
├── 📄 test_main.py
├── 📄 test_handlers.py
└── 📄 test_services.py
```

### 🧪 Execução de Testes
```bash
pytest tests/
```

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Cleiton Leonel Creton**
- GitHub: [@cleitonleonel](https://github.com/cleitonleonel)
- Email: cleiton.leonel@gmail.com

---

📞 **Suporte**: Para dúvidas ou problemas, entre em contato através do [Telegram](https://t.me/CleitonLC).

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!

## 📊 Status do Projeto

![GitHub last commit](https://img.shields.io/github/last-commit/cleitonleonel/PyPixBot)
![GitHub contributors](https://img.shields.io/github/contributors/cleitonleonel/PyPixBot)
![GitHub forks](https://img.shields.io/github/forks/cleitonleonel/PyPixBot)
![GitHub stars](https://img.shields.io/github/stars/cleitonleonel/PyPixBot)
![GitHub license](https://img.shields.io/github/license/cleitonleonel/PyPixBot)
![GitHub issues](https://img.shields.io/github/issues/cleitonleonel/PyPixBot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/cleitonleonel/PyPixBot)
```