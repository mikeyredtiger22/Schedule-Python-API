from flask import Flask
import schedule

app = Flask(__name__)


@app.route("/")
def hello():
    return str(schedule.Schedule().generate_week_schedule())


if __name__ == "__main__":
    app.run()
