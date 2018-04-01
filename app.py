from flask import Flask
from flask_cors import CORS
import json
import schedule

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return json.dumps(schedule.Schedule().generate_schedule())


@app.route("/generate/<int:weeks>")
def generate10(weeks):
    return json.dumps(schedule.Schedule().generate_schedule(weeks))


if __name__ == "__main__":
    app.run()
