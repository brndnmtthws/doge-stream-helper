from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import json


def get_data():
    with open('data.json', 'r') as infile:
        return json.load(infile)


def set_data(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


@app.route('/toggleboggle')
def toggle():
    return render_template('toggle.html')


@app.route('/togglestate')
def get_togglestate():
    return jsonify(get_data())


@app.route('/togglestate', methods=["PUT"])
def set_togglestate():
    set_data(json.loads(request.data))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
