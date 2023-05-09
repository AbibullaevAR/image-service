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

