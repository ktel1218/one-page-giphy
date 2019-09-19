import time
import requests

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # user inputs
        first = request.form.get('first')
        second = request.form.get('second')
        # api call
        now = time.ctime(int(time.time()))
        # response = requests.get(url)
        # print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        # return json
        return jsonify(response.json())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
