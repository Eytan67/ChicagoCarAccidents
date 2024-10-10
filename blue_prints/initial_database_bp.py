from flask import Blueprint, jsonify


initdb_bp = Blueprint('init', __name__)


@initdb_bp.route('/', methods=['POST'])
def initialize():
    return jsonify({'success': True, '______________________________________': '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'}), 200
