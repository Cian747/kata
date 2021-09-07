from flask import render_template
from app import app
from .request import main


@app.route('/')
def index():
    jobs = main()
    # for job in jobs:
    #     print(f'{job}')
    title = 'Welcome'
    return render_template('index.html',title = title, jobs = jobs)