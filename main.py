import os
from smartbot.bot import Client
from smartbot.paths import SESSIONS_DIR
from telethon.network import ConnectionTcpFull
from enum import Enum
from smartbot.config import (
    BOT_TOKEN,
    APP_NAME,
    DEVICE_MODEL,
    SYSTEM_VERSION,
    APP_VERSION,
    ADMIN_IDS,
    API_ID,
    API_HASH,
)

SESSION_PATH: str = os.path.join(
    SESSIONS_DIR,
    APP_NAME
)

from constants import (
    ADMIN_COMMANDS,
    DEFAULT_COMMANDS
)


class ConversationState(Enum):
    """Enum to represent the state of the conversation with the user.
    This is used to manage the flow of the conversation and determine what
    the user is expected to do next.
    """
    IDLE = "idle"
    WAITING_PIX_KEY = "waiting_pix_key"
    WAITING_AMOUNT = "waiting_amount"
    WAITING_YES_NO = "waiting_yes_no"
    WAITING_LOGO = "waiting_logo"
    IN_MENU = "in_menu"
    PROCESSING = "processing"


plugins: dict[str, str | list[str]] = dict(
    root="pypixbot.plugins",
    include=[
        "commands.start_handler",
        "commands.help_handler",
        "commands.qrcode_handler",
        "commands.restart_handler"
    ],
    exclude=["message"]
)
commands: dict[str, list[str]] = dict(
    admin_commands=ADMIN_COMMANDS,
    default_commands=DEFAULT_COMMANDS
)

profile: dict[str, str] = dict(
    name=APP_NAME,
    logo="src/media/logo.png",
    lang="pt",
    description=(
        "💠 Um bot para gerar QR Codes estáticos do Pix."
    ),
    about="💠 Bot não oficial para gerar QR Codes estáticos do Pix.",
    # force_update=True, # Force update the bot profile on startup
)

client: Client = Client(
    bot_token=BOT_TOKEN,
    session=SESSION_PATH,
    api_id=API_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpFull,
    device_model=DEVICE_MODEL,
    system_version=SYSTEM_VERSION,
    app_version=APP_VERSION,
    admin_ids=ADMIN_IDS,
    commands=commands,
    plugins=plugins,
    config=profile,
    conversation_state=ConversationState,
)

if __name__ == "__main__":
    client.start_service()
