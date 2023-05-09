import os
import json
from io import BytesIO

from flask_restful import Resource, abort, request
from flask_jwt_extended import jwt_required
from flask import send_from_directory, make_response
from werkzeug.datastructures import FileStorage

from image_service.helpers import generate_token, check_token, TokenNotValid
from image_service.services import validate_image, optimize_image, ImgNotValid

class UploadLinkResource(Resource):
    @jwt_required()
    def get(self, name: str):
        token = generate_token(name, 330)

        from image_service.bp import api_bp
        from setup import app

        uploadURL = app.config['BASE_DOWNLOAD_HOST'] + api_bp.url_for(UploadFileResource, token=token)

        return {'href': uploadURL}


class UploadFileResource(Resource):

    def put(self, token):

        try:
            file_name = check_token(token)
        except TokenNotValid:
            abort(400, message='Token not valid')

        from setup import app

        try:
            img = validate_image(BytesIO(request.data))
        except ImgNotValid as e:
            abort(400, message = e.message)

        img.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{file_name}.webp'), format='webp', quality=80)

        return make_response({}, 201)


class DownloadLinkResource(Resource):
    @jwt_required()
    def get(self, name: str):
        token = generate_token(name, 330)

        from image_service.bp import api_bp
        from setup import app

        downloadURL = app.config['BASE_DOWNLOAD_HOST'] + api_bp.url_for(DownloadFileResource, token=token)

        return {'href': downloadURL}
    

class DownloadFileResource(Resource):

    def get(self, token):

        try:
            file_name = check_token(token)
        except TokenNotValid:
            abort(400, message='Token not valid')

        from setup import app
        return send_from_directory(app.config['UPLOAD_FOLDER'], f'{file_name}.webp')


class DeleteFileResource(Resource):

    @jwt_required()
    def delete(self, name):

        from setup import app

        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f'{name}.webp'))
        except FileNotFoundError:
            abort(404, message='FileNotFoundError')

        return make_response({}, 204)