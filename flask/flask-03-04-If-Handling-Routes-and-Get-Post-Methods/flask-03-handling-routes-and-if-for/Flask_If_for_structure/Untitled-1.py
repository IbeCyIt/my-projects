from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def head():
    first = "If you fail, just try again"
    return render_template("index.html", message = first)

@app.route("/ibe")
def header():
    names =["Ibrahimu", "Elif", "Fatih"]
    return render_template("body.html", object = names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

    