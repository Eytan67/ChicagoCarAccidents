from bson import ObjectId
from flask import current_app
from repository.accident_repository import AccidentRepository
from repository.beats_repository import BeatsRepository
from repository.database import Database


def get_accidents_by_beat_and_date_range(beat, start_date = None, end_date = None):
    db = Database(app=current_app)
    beats_collection = db.get_collection('beats')
    beats_repository = BeatsRepository(beats_collection)

    accident_ids = beats_repository.get_by_beat(beat)

    if start_date and end_date:
        date_filter = {
            "$gte": start_date,
            "$lte": end_date
           }
    elif start_date:
        date_filter = {
            "$eq": start_date
        }
    else:
        db.close_connection()
        return len(accident_ids)

    accident_collection = db.get_collection('accidents')
    accident_repository = AccidentRepository(accident_collection)

    query = {
        "_id": {"$in": [ObjectId(accident_id) for accident_id in accident_ids]},
        "CRASH_DATE": date_filter
    }
    accidents = accident_repository.find_by_query(query)
    db.close_connection()

    return len(accidents)

def order_accident_by_prim(beat):
    db = Database(app=current_app)
    beats_collection = db.get_collection('beats')
    beats_repository = BeatsRepository(beats_collection)

    accident_ids = beats_repository.get_by_beat(beat)

    query = [
        {
            "$match": {
                "$in": [ObjectId(accident_id) for accident_id in accident_ids]
            }
        },
        {
            "$group": {
                "_id": "$PRIM_CONTRIBUTORY_CAUSE",
                "count": {"$sum": 1}
            }
        }
    ]

    accident_collection = db.get_collection('accidents')
    accident_repository = AccidentRepository(accident_collection)

    accidents = accident_repository.grop_by_query(query)
    print("accidents:", accidents)