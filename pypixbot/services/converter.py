import imageio
import os


def webm_to_gif(input_path: str, duration: float) -> str:
    """Converte um arquivo WebM para GIF.
    Args:
        input_path (str): Caminho do arquivo WebM de entrada.
        duration (float): Duração total do GIF em segundos.
    Returns:
        str: Caminho do arquivo GIF gerado.
    Raises:
        FileNotFoundError: Se o arquivo de entrada não for encontrado.
        ValueError: Se o vídeo não contiver frames visíveis.
    """

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

    reader = imageio.get_reader(input_path, format='webm')
    frames = [frame for frame in reader]
    reader.close()

    if not frames:
        raise ValueError("O vídeo não possui frames visíveis.")

    duration_per_frame = duration / len(frames)
    gif_path = os.path.splitext(input_path)[0] + ".gif"

    imageio.mimsave(gif_path, frames, duration=duration_per_frame)

    return gif_path
