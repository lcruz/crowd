from flask import Flask
from flask import render_template, redirect
app = Flask("crowd")

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

