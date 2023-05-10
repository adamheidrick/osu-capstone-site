from flask import Flask, render_template

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
