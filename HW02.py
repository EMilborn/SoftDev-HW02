from flask import Flask

app = Flask(__name__)

@app.route("/")
def page():
    return __name__ + "<br>test pages /d and /w"

@app.route("/d")
def pageD():
    return "Dyrland"

@app.route("/w")
def pageW():
    return "Weaver"

app.run()
