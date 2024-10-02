from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from flask_pymongo import PyMongo
import re

matplotlib.use('Agg')

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/szkolenia_db"
mongo = PyMongo(app)


@app.route("/")
def index():

    x = ["Zakończone", "W trakcie", "Odrzucono"]
    y = [2, 12, 7]
    plt.bar(x, y)
    plt.xlabel("Statusy")
    plt.ylabel("Liczby")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    img_url = base64.b64encode(img.getvalue()).decode()

    firstname = "Jan"
    lastname = "Kowalski"

    return render_template(
        "index.html",
        firstname=firstname,
        lastname=lastname,
        img_url=img_url
    )


@app.route('/sklep')
def shop_page():
    courses = list(mongo.db.courses.find({}))
    return render_template("shop.html", items=courses)


@app.route('/sklep/<prod>')
def product_page(prod):

    try:
        id = re.match(r"^[^-]+", prod).group()
        course = mongo.db.courses.find_one({'serviceId': id})
        return render_template("product.html", course=course)
    except:
        return "<p>Wystąpił bląd</p>"
