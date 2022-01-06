from flask import Flask, render_template, request, jsonify

from Chat import get_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index_get():
    return render_template("base.html")


@app.route("/predict", methods=[''])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return (message)


if __name__ == "__main__":
    app.run(debug=True)
