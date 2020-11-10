# -*- coding: utf-8 -*-

import json

import requests
from flask import flash, request, redirect, render_template, current_app
from werkzeug.utils import secure_filename

from app.main import bp


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS_PHOTO']


@bp.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            url = current_app.config['PROCESSING_API']

            files = {
                'type_file': secure_filename(file.filename),
                'file': ("image.png", file.stream.read()),
            }

            response = requests.post(url, files=files)
            return response.json()


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', models=current_app.config['DETECT_FACES_URL_MODELS'])


@bp.route('/predict', methods=['POST'])
def predict():
    # TODO add asynchtonus
    results = {
        'age_model': None,
        'gender_model': None,
        'ethnicity_model': None
    }
    headers = {"content-type": "application/json"}

    data = json.dumps({"instances": request.json})

    for model, url in current_app.config['DETECT_FACES_URL_MODELS'].items():
        response = requests.post(url, data=data, headers=headers)
        results[model] = response.json()

    return json.dumps(results)
