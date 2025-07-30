import logging
from typing import Any
from telethon import events
from smartbot.utils.handler import ClientHandler

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/restart'))
async def handle_restart(event: Any):
    """
    Handles the `/restart` command by sending a greeting message.

    :param event: The event triggered by the `/restart` command.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Restart Handler Triggered by User ID: {sender_id}")
    logging.info(f"Event Client Instance: {event.client}")

    for user_id, session in event.client.user_sessions.items():
        event.client.reset_user_session(user_id)

    event.client.user_sessions.clear()

    logging.info(f"All user sessions have been reset.")
    await event.respond(
        message='🔄 **Reinicialização Completa!**\n\n',
        buttons=None
    )
