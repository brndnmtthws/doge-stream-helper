from flask import Flask, render_template, request, jsonify, send_from_directory
app = Flask(__name__)
import json
import os

doge_data = os.environ.get('DOGE_DATA', 'data.json')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


def get_data():
    with open(doge_data, 'r') as infile:
        return json.load(infile)


def set_data(data):
    with open(doge_data, 'w') as outfile:
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
    return jsonify(get_data())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
