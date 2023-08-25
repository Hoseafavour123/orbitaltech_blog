from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def error(e):
    return render_template("404.html")


@app.errorhandler(500)
def error500(e):
    return render_template("500.html")

@app.route("/")
def index():
    return render_template("index.html")

# Register blueprint
from auth import auth
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)