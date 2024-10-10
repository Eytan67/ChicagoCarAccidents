from flask import Blueprint, jsonify, current_app

from repository.database import Database
from service.init_database import init_database

initdb_bp = Blueprint('init', __name__)


@initdb_bp.route('/', methods=['POST'])
def initialize():
    db = Database(app=current_app)
    return init_database(db), 200
