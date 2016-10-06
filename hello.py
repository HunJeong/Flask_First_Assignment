from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)


@app.route("/")
def hello():
    whatColor = random.randrange(0, 4)
    size = random.randrange(1, 10)
    color = ["red", "blue", "yellow", "green", "orange"]
    try:
        count = int(request.cookies.get('count'))
        print("succeed")
    except Exception:
        count = 0
        print("false")

    resp = make_response(render_template('index.html', count=count, size=size, color=color[whatColor]))
    resp.set_cookie('count', str(count + 1))
    return resp


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
