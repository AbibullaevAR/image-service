from PIL import Image
from io import BytesIO


class ImgNotValid(Exception):
    def __init__(self, message):
        self.message = message


def validate_image(file: BytesIO, file_name: str):

    available_formats = {
        'JPEG':'.jpg',
        'PNG': '.png'
    }

    # Проверяем, является ли файл изображением
    try:
        img = Image.open(file)
    except:
        raise ImgNotValid('Файл не является изображением')

    # Проверяем формат изображения
    if img.format not in ['JPEG', 'PNG']:
        raise ImgNotValid('Недопустимый формат изображения. Разрешены только JPEG, PNG')

    if not file_name.endswith(available_formats[img.format]):
        raise ImgNotValid('Формат изображения не совпадает с форматом в названии')
    
    return img

def optimize_image(img: Image) -> Image:
    # Получаем ширину и высоту изображения
    width, height = img.size

    # Устанавливаем максимальную ширину и высоту
    max_width = 550
    max_height = 470

    # Вычисляем новые размеры изображения
    if width > max_width or height > max_height:

        # Сжимаем изображение
        return img.resize((max_width, max_height), Image.LANCZOS)
    
    return img
