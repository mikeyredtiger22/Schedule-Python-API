from flask import Flask
from flask_cors import CORS
import schedule

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return str(schedule.Schedule().generate_week_schedule())


if __name__ == "__main__":
    app.run()
