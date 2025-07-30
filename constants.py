from telethon.tl.types import BotCommand

ADMIN_COMMANDS = [
    BotCommand(
        command="restart",
        description='Limpar cache de usuários e reiniciar o bot.'
    )
]

DEFAULT_COMMANDS = [
    BotCommand(
        command="start",
        description='Iniciar ou reiniciar uma conversa com o bot.'
    ),
    BotCommand(
        command="create_pix",
        description='Gerar um novo qrcode.'
    ),
    BotCommand(
        command="help",
        description='Exibir informações sobre os comandos disponíveis.'
    ),
]
