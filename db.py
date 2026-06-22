from pymongo import MongoClient
import os


def get_collection():
    client = MongoClient(
        os.getenv(
            "MONGODB_URI",
            "mongodb+srv://nemakalruthvika_db_user:6BFcrgEzcq8joDIW@cluster0.efswmah.mongodb.net"
        )
    )

    db = client[os.getenv("MONGODB_DATABASE", "student_db")]
    return db.students


def insert_student(data):
    collection = get_collection()

    document = {
        "name": data["name"],
        "roll": data["roll"],
        "marks": data["marks"],
        "total": data["total"],
        "average": data["average"],
        "percentage": data["percentage"],
        "grade": data["grade"],
        "status": data["status"]
    }

    result = collection.insert_one(document)

    return str(result.inserted_id)