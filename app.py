from flask import Flask, request, redirect, url_for, send_file, render_template, make_response,flash
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    with open('scrape_experiment/data.json') as json_data:
        jobs = json.load(json_data)
    resp = make_response(render_template('index.html', data = jobs, title='Home'))
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
