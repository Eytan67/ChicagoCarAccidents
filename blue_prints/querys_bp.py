from flask import Blueprint, jsonify, request


query_bp = Blueprint('query', __name__)


@query_bp.route('<beat>', methods=['GET'])
def get_accidents_by_beat(beat):

    day = request.args.get('day')
    week = request.args.get('week')
    month = request.args.get('month')
    if day:
        return jsonify({"day":day})
    elif week:
        return jsonify({"week":week})
    elif month:
        return jsonify({"month":month})
    else:
        return jsonify({'beat': beat})

@query_bp.route('cause', methods=['GET'])
def get_accidents_by_cause():
    return jsonify({"cause" : 1})

@query_bp.route('statistic', methods=['GET'])
def get_injury_statistics ():
    return jsonify({"statistic": 1})
