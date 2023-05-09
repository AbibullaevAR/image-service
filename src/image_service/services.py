from PIL import Image
from io import BytesIO


class ImgNotValid(Exception):
    def __init__(self, message):
        self.message = message


def validate_image(file: BytesIO):

    # Проверяем, является ли файл изображением
    try:
        img = Image.open(file)
    except:
        raise ImgNotValid('Файл не является изображением')

    # Проверяем формат изображения
    if img.format not in ['JPEG', 'PNG', 'JPG']:
        raise ImgNotValid('Недопустимый формат изображения. Разрешены только JPEG, PNG, JPG')
    
    return img

def optimize_image(img: Image) -> Image:
    # Получаем ширину и высоту изображения
    width, height = img.size

    from setup import app
    # Устанавливаем максимальную ширину и высоту
    max_width = app.config['MAX_WIDTH_RESIZE']
    max_height = app.config['MAX_HEIGHT_RESIZE']

    # Не применяем сжатие если размеры меньше максимальных
    if width < max_width or height < max_height:
        return img

    # Расчет новых размеров с сохранением соотношения сторон
    if width < height:
        return img.resize((max_width, int((max_width / width) * height)), Image.LANCZOS)

    return img.resize((int((max_height / height) * width), max_height), Image.LANCZOS)
