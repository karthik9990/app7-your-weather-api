from flask import Flask, render_template
import pandas as ps

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def contact(station, date):
    # df = ps.read_csv()
    temperature = 23
    return {"station": station,
            "Date": date,
            "temperature": temperature}


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/store")
def store():
    return render_template("store.html")


if __name__ == "__main__":
    app.run(debug=True)
