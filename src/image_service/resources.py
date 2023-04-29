import os
import json

from flask_restful import Resource, abort, request
from flask_jwt_extended import jwt_required
from flask import send_from_directory

from image_service.helpers import generate_token, check_token, TokenNotValid

class UploadLinkResource(Resource):
    @jwt_required()
    def get(self, name: str):
        token = generate_token(name, 330)

        from image_service.bp import api_bp

        uploadURL = request.host_url[:-1] + api_bp.url_for(UploadFileResource, token=token)

        return {'href': uploadURL}


class UploadFileResource(Resource):

    def put(self, token):

        try:
            file_name = check_token(token)
        except TokenNotValid:
            abort(400, message='Token not valid')

        from setup import app

        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

        return {'test': file_name}


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
        return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)