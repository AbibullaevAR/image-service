from flask_restful import Resource, abort, request
from flask_jwt_extended import jwt_required
from flask.views import MethodView

from image_service.helpers import generate_token, check_token, TokenNotValid

class UploadLinkResource(Resource):
    @jwt_required()
    def get(self, name: str):
        token = generate_token(name, 330)
        return token


class UploadFileResource(Resource):

    def put(self, token):

        try:
            file_name = check_token(token)
        except TokenNotValid:
            abort(400, message='Token not valid')

        file = request.files['file']
        file.save(file_name)

        return {'test': file_name}
    