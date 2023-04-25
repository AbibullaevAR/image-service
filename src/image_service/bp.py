from flask import Blueprint

image_service_bp = Blueprint('image_service', __name__, url_prefix='/image-service/api/v1')