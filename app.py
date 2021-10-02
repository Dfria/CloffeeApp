# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("form.html")

