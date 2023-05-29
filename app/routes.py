from flask import render_template, redirect, flash, url_for, request
from app import app
from datetime import datetime

@app.route('/')
def index():
          # return render_template('index.html')
          return "Hello World"