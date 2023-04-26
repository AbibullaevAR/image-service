import uuid

from flask.cli import AppGroup
from flask_jwt_extended import create_access_token

cli_group = AppGroup('auth')

@cli_group.command('create-token')
def create_token():
    """
        Create auth token for other service
    """

    token = create_access_token(uuid.uuid4())
    print('Access token: ' + token)
