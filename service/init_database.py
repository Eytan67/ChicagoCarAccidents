from datetime import datetime
from flask import jsonify, current_app
from repository.accident_repository import AccidentRepository
from repository.beats_repository import BeatsRepository
from repository.csv_repository import read_csv
from repository.database import Database


def safe_int(value):
    """Attempts to convert a value to int, returns 0 on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

def parse_date(date_str: str):
    """Parses a date string into a datetime object."""
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def load_traffic_crashes_data(beats_repo: BeatsRepository, accident_repo:AccidentRepository):
    beats_repo.drop_collection()
    accident_repo.drop_collection()

    try:
        for row in read_csv(r'C:\Users\eytan zichel\PycharmProjects\mongodb\ChicagoCarAccidents\data\Traffic_Crashes_Crashes_20k.csv'):
            injuries = {
                'INJURIES_TOTAL': safe_int(row['INJURIES_TOTAL']),
                'INJURIES_FATAL': safe_int(row['INJURIES_FATAL']),
            }

            accident = {
                'PRIM_CONTRIBUTORY_CAUSE': row['PRIM_CONTRIBUTORY_CAUSE'],
                'CRASH_DATE': parse_date(row['CRASH_DATE']),
                'injury': injuries
            }

            accident_id = accident_repo.add(accident)

            beat = row['BEAT_OF_OCCURRENCE']
            beats_repo.add_accident(beat, accident_id)

        return jsonify({"success": True, "message": "Data initialized successfully!"})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def init_database():
    db = Database(app=current_app)

    beats_collection = db.get_collection('beats')
    accident_collection = db.get_collection('accidents')

    beats_repository = BeatsRepository(beats_collection)
    accidents_repository = AccidentRepository(accident_collection)

    response = load_traffic_crashes_data(beats_repository, accidents_repository)

    db.close_connection()
    return response





