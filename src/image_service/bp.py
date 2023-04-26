from flask import Blueprint
from flask_restful import Api

from image_service.commands import cli_group
from image_service.resources import DownloadLinkResource

image_service_bp = Blueprint('image_service', __name__, url_prefix='/image-service/api/v1/')

image_service_bp.cli.add_command(cli_group)

api_bp = Api(image_service_bp)

api_bp.add_resource(DownloadLinkResource, 'download_link')