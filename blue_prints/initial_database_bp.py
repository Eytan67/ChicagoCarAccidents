from flask import Blueprint
from service.init_database import init_database

initdb_bp = Blueprint('init', __name__)


@initdb_bp.route('/', methods=['POST'])
def initialize():
    return init_database(), 200
