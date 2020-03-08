from flask import Flask, render_template

app=Flask(__name__)

@app.route('')
def index():
    return "<h1> heelo </h1>"

app.run()