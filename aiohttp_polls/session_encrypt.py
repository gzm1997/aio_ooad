from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

def setup_session_support(app):
    setup(app, EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))
    return app