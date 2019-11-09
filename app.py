from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Index page."


@app.route('/registerFC', methods=["POST"])
def register():
    return jsonify(request.json), 201


if __name__ == '__main__':
    app.run()
