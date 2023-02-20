from flask import Flask, render_template, jsonify
from model import model

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_word():
    return render_template("index.html")

@app.route("/generate", methods = ['GET'])
def generate():
    name = model.generate_name()
    return jsonify(name=name)

if __name__ == "__main__":
    app.run(port = 3000, debug = True)