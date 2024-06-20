from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"hello": "jkuffor"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)