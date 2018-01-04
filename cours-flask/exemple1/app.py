from flask import Flask

app = Flask("Application")

@app.route("/")
def index():
    return "Hello world !"

app.run()
