from decimal import Decimal
from telethon import events
from telethon.tl.custom.message import Message
from telethon.tl.types import (
    MessageMediaPhoto,
    MessageMediaDocument,
    DocumentAttributeVideo
)
from smartbot.utils.handler import ClientHandler
from pypixbot.services.pix_service import create_qrcode_pix
from pypixbot.services.converter import webm_to_gif
import os
import re
import uuid
import logging
import mimetypes

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern=r"^/create_pix"))
async def handle_create_pix(event):
    """ Handles the `/create_pix` command to create a Pix QR code.
    This function checks the command arguments, prompts for a logo if requested,
    and generates a Pix QR code with the provided key and amount.
    :param event: The event triggered by the `/create_pix` command.
    """
    sender_id = event.sender_id
    pattern = r"^/create_pix\s+(\S+)\s+([\d.]+)(?:\s+(\S+))?"
    match = re.match(pattern, event.raw_text)
    if match:
        pix_key = match.group(1)
        amount = match.group(2)
        wants_logo = match.group(3) if match.group(3) else None
    else:
        event.client.set_user_state(sender_id, event.client.conversation_state.WAITING_PIX_KEY)
        return await event.respond("Digite uma chave Pix válida.")

    if not pix_key or not amount:
        message_str = (
            "ℹ️ Uso: `/create_pix <chave_pix> <valor> [logo_opcional]`\n"
            "Exemplo: `/create_pix email@pix.com 12.34 sim`"
        )
        return await event.respond(message_str, parse_mode='Markdown')

    event.client.set_user_data(sender_id, 'pix_key', pix_key)
    event.client.set_user_data(sender_id, 'amount', amount)

    try:
        amount = Decimal(amount)
    except ValueError:
        logging.error(f"Invalid amount: {amount} for user {sender_id}")
        return await event.respond("❌ Valor inválido. Use um número como `12.34`.")

    if wants_logo:
        event.client.set_user_state(sender_id, event.client.conversation_state.WAITING_LOGO)
        return await event.respond("📎 Envie agora a imagem que será usada como logo no QR Code.")
    else:
        await generate_pix_qr(event, pix_key, amount)

    event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)

    return None


@client.on(events.NewMessage)
async def handle_logo_image(event):
    """Handles the image sent by the user for the logo in the Pix QR code."""

    if event.raw_text and event.raw_text.strip().startswith('/'):
        return

    sender_id = event.sender_id
    current_state = event.client.get_user_state(sender_id)

    logging.info(f"Logo Handler Triggered by User ID: {sender_id}")
    logging.info(f"Current User State: {current_state}")

    if current_state == event.client.conversation_state.WAITING_LOGO:
        logging.info(f"Processing logo for user {sender_id}")

        if not event.media:
            await event.respond("❌ Por favor, envie uma imagem válida (JPG, PNG) ou GIF.")
            return

        pix_key = event.client.get_user_data(sender_id, 'pix_key')
        amount = event.client.get_user_data(sender_id, 'amount')

        if not pix_key or not amount:
            logging.error(f"Missing Pix key or amount for user {sender_id}")
            await event.respond("❌ Chave Pix ou valor não encontrados. Tente novamente.")
            event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
            return

        amount = Decimal(amount)
        extension = '.png'
        base_path = f"src/media/logo_{sender_id}_{uuid.uuid4().hex}"

        try:
            if isinstance(event.media, MessageMediaPhoto):
                file_path = f'{base_path}.png'
                await event.download_media(file_path)
                logging.info(f"Downloaded photo: {file_path}")

            elif isinstance(event.media, MessageMediaDocument):
                document = event.media.document
                mime_type = document.mime_type
                attrs = getattr(document, "attributes", [])

                logging.info(f"Received document with MIME type: {mime_type}")

                if mime_type in ["image/jpeg", "image/jpg", "image/png", "image/gif", "image/webp"]:
                    extension = mimetypes.guess_extension(mime_type) or '.png'
                    file_path = f'{base_path}{extension}'
                    await event.download_media(file_path)
                    logging.info(f"Downloaded image document: {file_path}")

                elif mime_type == "video/webm":
                    video_attr = None
                    for attr in attrs:
                        if isinstance(attr, DocumentAttributeVideo):
                            video_attr = attr
                            break

                    if video_attr:
                        if getattr(video_attr, "nosound", False) and video_attr.duration <= 10:
                            extension = mimetypes.guess_extension(mime_type) or '.webm'
                            video_path = f'{base_path}{extension}'
                            await event.download_media(video_path)

                            try:
                                file_path = webm_to_gif(video_path, video_attr.duration)
                                os.remove(video_path)
                                logging.info(f"Converted WebM to GIF: {file_path}")
                            except Exception as e:
                                if os.path.exists(video_path):
                                    os.remove(video_path)
                                await event.respond(f"❌ Erro ao converter o vídeo: {str(e)}")
                                event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                                return
                        else:
                            await event.respond("❌ Apenas GIFs curtos (até 10 segundos) são aceitos.")
                            event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                            return
                    else:
                        await event.respond("❌ Formato de vídeo não suportado.")
                        event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                        return

                else:
                    await event.respond("❌ Formato não suportado. Envie uma imagem (JPG, PNG) ou GIF.")
                    event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                    return

            else:
                await event.respond("❌ Tipo de mídia não suportado. Envie uma imagem ou GIF.")
                event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                return

            if 'file_path' in locals() and file_path:
                event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                return await generate_pix_qr(event, pix_key, amount, file_path, extension)
            else:
                await event.respond("❌ Erro ao processar o arquivo. Tente novamente.")
                event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
                return

        except Exception as e:
            logging.error(f"Error processing media for user {sender_id}: {str(e)}")
            await event.respond("❌ Erro ao processar o arquivo. Tente novamente.")
            event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
            return
    elif current_state == event.client.conversation_state.WAITING_PIX_KEY:
        pix_key = event.raw_text.strip()
        event.client.set_user_data(sender_id, 'pix_key', pix_key)
        event.client.set_user_state(sender_id, event.client.conversation_state.WAITING_AMOUNT)
        return await event.respond("Digite o valor a ser incluído no QR Code (ex: `12.34`):")
    elif current_state == event.client.conversation_state.WAITING_AMOUNT:
        amount = event.raw_text.strip()
        try:
            amount = Decimal(amount)
            event.client.set_user_data(sender_id, 'amount', str(amount))
            event.client.set_user_state(sender_id, event.client.conversation_state.WAITING_YES_NO)
            return await event.respond(
                "✅ Valor recebido. Você gostaria de adicionar um logo ao QR Code? (sim/não)"
            )
        except ValueError:
            return await event.respond("❌ Valor inválido. Use um número como `12.34`.")
    elif current_state == event.client.conversation_state.WAITING_YES_NO:
        response = event.raw_text.strip().lower()
        if response in ['sim', 's', 'yes', 'y']:
            event.client.set_user_state(sender_id, event.client.conversation_state.WAITING_LOGO)
            return await event.respond("📎 Envie agora a imagem que será usada como logo no QR Code.")
        elif response in ['não', 'n', 'no']:
            pix_key = event.client.get_user_data(sender_id, 'pix_key')
            amount = event.client.get_user_data(sender_id, 'amount')
            if not pix_key or not amount:
                return await event.respond("❌ Chave Pix ou valor não encontrados. Tente novamente.")
            amount = Decimal(amount)
            await generate_pix_qr(event, pix_key, amount)
            event.client.set_user_state(sender_id, event.client.conversation_state.IDLE)
            return
        else:
            return await event.respond("❌ Resposta inválida. Responda com `sim` ou `não`.")

async def generate_pix_qr(
        event: Message,
        pix_key: str,
        amount: Decimal,
        logo_path: str | None = None,
        extension: str = '.png'
):
    """ Generates a Pix QR code and sends it to the user.

    :param pix_key: The Pix key to be used in the QR code.
    :param amount: The amount to be included in the QR code.
    :param logo_path: Optional path to a logo image to be included in the QR code.
    :param extension: The file extension of the logo image, if provided.
    :param event: The event that triggered this function.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Generate Pix Triggered by User ID: {sender_id}")

    if logo_path:
        await event.respond("🖼️ Logo recebida, processando...")

    user_fullname = (
        f"{sender.first_name} {sender.last_name}".strip()
        if sender.last_name else sender.first_name
    )

    config_dict = {
        "receiver": user_fullname or "Usuário",
        "city": "Brasília",
        "key": pix_key,
        "identification": f"PYPIX{uuid.uuid4().hex[:4]}",
        "zipcode": "70074-900",
        "description": "QR Code gerado pelo PyPixBot",
        "amount": amount,
        "logo": logo_path if logo_path else None,
        "filename": f"qrcode{extension}"
    }

    pix_string, pix_qrcode = create_qrcode_pix(config_dict)
    await event.respond("✅ QR Code gerado com sucesso!")

    await event.client.send_file(sender_id, file=pix_qrcode, caption=f'\n\n__{pix_string}__')

    if logo_path and os.path.exists(logo_path):
        os.remove(logo_path)

    os.remove(pix_qrcode)
