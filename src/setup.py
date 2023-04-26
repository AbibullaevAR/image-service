from flask import Flask
from flask_jwt_extended import JWTManager

from image_service.bp import image_service_bp

app = Flask(__name__)

app.config.from_pyfile('config.py')

jwt = JWTManager(app)

app.register_blueprint(image_service_bp)

if __name__ == '__main__':
    app.run()