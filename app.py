from flask import Flask
from flask_cors import CORS
import schedule

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return str(schedule.Schedule().generate_schedule())

@app.route("/generate/<int:weeks>")
def generate10(weeks):
    return str(schedule.Schedule().generate_schedule(weeks))

if __name__ == "__main__":
    app.run()
