import logging
from typing import Any
from telethon import events
from smartbot.utils.handler import ClientHandler

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/help'))
async def handle_help(event: Any):
    """
    Handles the `/help` command by sending a greeting message.

    :param event: The event triggered by the `/help` command.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Help Handler Triggered by User ID: {sender_id}")
    logging.info(f"Event Client Instance: {event.client}")

    help_message = (
        "ℹ️ **Ajuda do PyPixBot**\n\n"
        "Olá! Aqui estão algumas informações úteis para você começar a usar o PyPixBot:\n\n"
        "1. **Gerar QR Code PIX**: \n"
        "Use o comando **/create_pix** para gerar um código PIX. "
        "Você pode especificar o valor ou deixá-lo aberto.\n\n"
        "2. **Menu Principal**: \n"
        "Use o comando **/start** para acessar o menu principal do bot, "
        "onde você encontrará todas as opções disponíveis.\n\n"
        "3. **Suporte**: \n"
        "Se você tiver alguma dúvida ou precisar de ajuda, "
        "não hesite em entrar em contato com nosso [suporte](https://t.me/CleitonLC).\n\n"
    )

    await event.respond(
        message=help_message,
        buttons=None
    )
