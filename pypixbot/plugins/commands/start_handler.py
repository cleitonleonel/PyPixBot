import logging
from typing import Any
from telethon import events, Button
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import (
    with_stack_and_cleanup,
    MENU_KEY,
    DELETE_KEY
)

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/start'))
@with_stack_and_cleanup()
async def handle_start(event: Any):
    """
    Handles the `/start` command by sending a greeting message.

    :param event: The event triggered by the `/start` command.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Start Handler Triggered by User ID: {sender_id}")
    logging.info(f"Event Client Instance: {event.client}")
    event.client.drivers[sender_id][MENU_KEY].clear()

    welcome_message = (
        "💳 **Bem-vindo ao PyPixBot!**\n\n"
        "Olá! Eu sou seu assistente virtual para gerar códigos PIX de forma rápida e fácil.\n\n"
        "Através deste bot você pode:\n"
        "• Gerar QR Code PIX para receber pagamentos\n"
        "• Criar PIX com valor fixo ou aberto\n"
        "• Personalizar suas chaves PIX\n"
        "• Compartilhar códigos de pagamento instantaneamente\n\n"
        "Para começar, clique no botão abaixo para acessar o menu principal."
    )

    welcome_msg = await event.respond(welcome_message)
    event.client.drivers[sender_id][DELETE_KEY].append(welcome_msg.id)
