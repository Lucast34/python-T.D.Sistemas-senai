from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellowolrd():
    return "<h1> Hello wolrd</h1>"