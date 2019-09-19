import time
import requests

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
        embed_url = response.json().get("data")[0].get("embed_url")
        # print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        # return json
        return jsonify(embed_url)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
