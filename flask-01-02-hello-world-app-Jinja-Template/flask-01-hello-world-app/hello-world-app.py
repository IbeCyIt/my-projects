from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World!</h1>"


@app.route("/second")
def second():
    return "<h3>no pain no gain</h3>"

@app.route("/third/subthird")
def third():
    return "<h5>Have what you love or love what you have</h5>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True)
    