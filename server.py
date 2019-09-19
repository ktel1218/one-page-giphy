import time
import requests
from pprint import pprint

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

URL="http://api.giphy.com/v1/gifs/search?q={}&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # user inputs
        search_term = request.form.get('search_term')
        # api call
        now = time.ctime(int(time.time()))
        response = requests.get(URL.format(search_term))
        pprint(response.json().get("data")[0])
        src_url = response.json().get("data")[0].get("images").get("fixed_width").get("url")
        # print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        # return json
        return jsonify(src_url)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
