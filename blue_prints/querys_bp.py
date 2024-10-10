from flask import Blueprint, jsonify, request
from service.search_accidents import get_accidents_by_beat_and_date_range, order_accident_by_prim
from datetime import timedelta, datetime

query_bp = Blueprint('query', __name__)


@query_bp.route('<beat>', methods=['GET'])
def get_accidents_by_beat(beat):

    day = request.args.get('day')
    week_start_day = request.args.get('week')
    month_start_day = request.args.get('month')

    if day:
        day = datetime.strptime(day, "%d-%m-%Y")
        res = get_accidents_by_beat_and_date_range(beat, day)
        return jsonify({'beat': beat, 'res': res})
    elif week_start_day:
        start_date = datetime.strptime(week_start_day, "%d-%m-%Y")
        end_date = start_date + timedelta(weeks=1)
        res = get_accidents_by_beat_and_date_range(beat, start_date, end_date)
        return jsonify({'beat': beat, 'res': res})
    elif month_start_day:
        start_date = datetime.strptime(month_start_day, "%d-%m-%Y")
        end_date = start_date + timedelta(days=30)
        res = get_accidents_by_beat_and_date_range(beat, start_date, end_date)
        return jsonify({'beat': beat, 'res': res})
    else:
        res = get_accidents_by_beat_and_date_range(beat)
        return jsonify({'beat': beat, 'res': res})

@query_bp.route('cause/<beat>', methods=['GET'])
def get_accidents_by_cause(beat):
    order_accident_by_prim(beat)
    return jsonify({"cause" : 1})

@query_bp.route('statistic', methods=['GET'])
def get_injury_statistics ():
    return jsonify({"statistic": 1})
