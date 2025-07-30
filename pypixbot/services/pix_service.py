import os
from pypix.pix import Pix
from pypix.core.utils.pix_parser import parse_br_code
from pypix.core.styles.qr_styler import GradientMode
from pypix.core.styles.marker_styles import MarkerStyle
from pypix.core.styles.border_styles import BorderStyle
from pypix.core.styles.line_styles import LineStyle
from pypix.core.styles.frame_styles import FrameStyle
import logging
import json

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO, format="%(pastime)s - %(levelness)s - %(message)s"
)
logger = logging.getLogger(__name__)

pix = Pix()


def normal_static(config: dict = None):
    """PIX Estático com valor fixo (Testado com Nubank, Inter, Caixa, MercadoPago)"""
    pix.set_name_receiver(config.get("receiver"))
    pix.set_city_receiver(config.get('city'))
    pix.set_key(config.get("key"))
    pix.set_identification(config.get('identification'))
    pix.set_zipcode_receiver(config.get('zipcode'))
    pix.set_description(config.get('description'))
    pix.set_amount(config.get('amount'))

    logger.info(
        f'Doação com valor definido - PYPIX >>>> {pix.get_br_code()}\n'
    )


def create_qrcode_pix(config: dict) -> tuple:
    normal_static(config=config)

    br_code = pix.get_br_code()
    decoded_data = parse_br_code(br_code)
    print(json.dumps(decoded_data, indent=4, ensure_ascii=False))

    qrcode_path = os.path.join(os.getcwd(), f'src/media/{config.get("filename")}')

    # Gera e salva QR code estilizado com ou sem logo
    base64qr = pix.save_qrcode(
        data=br_code,
        output=qrcode_path,  # Caminho para salvar o QR code
        box_size=7,
        border=1,
        custom_logo=config.get('logo'), # Pode ser PNG ou GIF
        marker_style=MarkerStyle.QUARTER_CIRCLE,
        border_style=BorderStyle.ROUNDED,
        line_style=LineStyle.ROUNDED,
        gradient_color="purple",
        gradient_mode=GradientMode.NORMAL,
        frame_style=FrameStyle.SCAN_ME_PURPLE,
        style_mode="Full"
    )

    if base64qr:
        logger.info("QR Code salvo com sucesso!")
        # print(base64qr)  # Base64 do QR code (caso necessário)
        # pix.qr_ascii()  # Imprime QR Code no terminal
    else:
        logger.error("Erro ao salvar o QR Code.")

    return br_code, qrcode_path