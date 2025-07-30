# 🐍 PyPixBot

<p align="center">
  <a href="https://github.com/cleitonleonel/PyPixBot">
    <img src="src/media/logo.png" alt="PyPixBot logo" width="45%" height="auto">
  </a>
</p>

<p align="center">
  <i>Um bot de Python para criar qrcodes do Pix.</i>
</p>

<p align="center">
<a href="https://github.com/cleitonleonel/PyPixBot">
  <img src="https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-green" alt="Supported Python Versions"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
  <img src="https://img.shields.io/github/stars/cleitonleonel/PyPixBot" alt="GitHub Stars"/>
</a>
</p>

---

**PyPixBot** é um bot de Python para criar QR Codes do Pix, permitindo a geração de códigos estáticos e dinâmicos, além de suportar múltiplas chaves Pix. Este projeto é ideal para quem deseja integrar pagamentos via Pix em seus bots.

## 📖 Sobre
O PyPixBot é um bot simples e eficiente para gerar QR Codes do Pix, facilitando a criação de pagamentos digitais. Ele suporta tanto códigos estáticos quanto dinâmicos, permitindo que você personalize suas transações. O bot é projetado para ser fácil de usar e configurar, com uma interface amigável.

## Acesso ao Bot
Você pode acessar o bot no Telegram através do seguinte link: [PyPixBot](https://t.me/PyPixBot).

## 🚀 Funcionalidades

- ✅ Criação de QR Codes do Pix
- ✅ Geração de códigos estáticos e dinâmicos
- ✅ Suporte a múltiplas chaves Pix
- 🔄 Checar se foi pago (em desenvolvimento para nubank)
- 📈 Dashboard para visualização de transações (planejada)
- 📊 Exportação de transações para CSV (planejada)
- 📅 Agendamento de pagamentos (planejado)
- 🔔 Notificações de transações (planejada)

## 📦 Instalação

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/cleitonleonel/PyPixBot.git
cd PyPixBot
```

### 2️⃣ Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # 🐧 Linux/Mac
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```
ou

### 3️⃣ Instale as dependências com Poetry
Certifique-se de ter o Poetry instalado. Se não tiver, instale com:

```bash
poetry install
```

## 💻 Uso
Para iniciar o bot, execute o seguinte comando:

```bash
python main.py
```

# 🔧 Configuração
Para configurar o bot, edite o arquivo `config.toml` com as configurações necessárias.

## 📁 Estrutura do Projeto

```plaintext
📦 projeto/
├── 📂 src/
│   ├── 📄 __init__.py
│   └── 📄 main.py
├── 📂 tests/
│   └── 📄 test_main.py
├── 📂 docs/
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 LICENSE
└── 📄 setup.py
```

### Executar testes:
```bash
pytest tests/
```

### Formatação de código:
```bash
black src/
```

### Linting:
```bash
flake8 src/
```

## 🤝 Contribuição

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
5. 🔄 Abra um Pull Request

## 📋 Requisitos

- 🐍 Python 3.8+
- 📚 Dependências listadas em `requirements.txt`

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Cleiton Leonel**
- 🐙 GitHub: [@cleitonleonel](https://github.com/cleitonleonel)
- 📧 Email: [Cleiton Leonel](about:cleiton.leonel@gmail.com)

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