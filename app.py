from flask import Flask, render_template, request

import database as db

app = Flask(__name__)

db.create_table()

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/add_activity", methods=["POST"])
def add_activity():
    data = request.get_json()
    name = data.get("name")
    if name:
        activity_id = db.insert_activity(name)
        return {
            "id": activity_id,
            "name": name
        }, 200
    else:
        return {"message": "Activity name is required."}, 400
    
@app.route("/activities", methods=["GET"])
def activities():
    activities = db.get_activities()
    return [
        {"id": activity[0], "name": activity[1]}
        for activity in activities
    ]   
    
@app.route("/delete_activity/<int:activity_id>", methods=["DELETE"])
def delete_activity(activity_id):
    db.delete_activity(activity_id)
    
    return {"message": "Activity deleted successfully."}, 200

@app.route("/save_trip", methods=["POST"])
def save_trip():
    data = request.get_json()
    destination = data.get("destination")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if destination and start_date and end_date:
        db.save_trip(destination, start_date, end_date)
        return {"message": "Trip saved successfully."}, 200
    else:
        return {"message": "Destination, start date, and end date are required."}, 400

@app.route("/trip")
def get_trip():
    trip = db.get_trip()

    if trip:
        return {
            "destination": trip[0],
            "start_date": trip[1],
            "end_date": trip[2]
        }

    return {}