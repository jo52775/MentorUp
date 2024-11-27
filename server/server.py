from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def sendData():
    return "here is some data"


if __name__ == "__main__":
    app.run()

