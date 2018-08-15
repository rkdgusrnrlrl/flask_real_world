from app import create_app
from settings import ProdConfig, DevConfig
from flask.helpers import get_debug_flag

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)