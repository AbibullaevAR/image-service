from flask import Flask

from image_service.bp import image_service_bp

app = Flask(__name__)


app.register_blueprint(image_service_bp)

if __name__ == '__main__':
    app.run()