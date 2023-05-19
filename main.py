import pyfiglet
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")
title = pyfiglet.figlet_format("TEXT BASED ADVENTURE")


@app.route("/", methods=['Get', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
