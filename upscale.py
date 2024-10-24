from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
import cv2
from cv2 import dnn_superres
import os

import numpy as np

app = Flask(__name__)

# initialize super resolution object
sr = dnn_superres.DnnSuperResImpl_create()

# read the model
path = 'models/EDSR_x4.pb'
sr.readModel(path)

# set the model and scale
sr.setModel('edsr', 4)

# function to upscale the image
def upscale_image(image):
    try:
        # upsample the image
        upscaled = sr.upsample(image)
        return upscaled, None
    except Exception as e:
        return None, "An error occurred while upscaling the image: " + str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            try:
                # read the image
                nparr = np.frombuffer(file.read(), np.uint8)
                image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                # upscale the image
                upscaled_image, error_message = upscale_image(image)

                if upscaled_image is not None:
                    # save the upscaled image
                    output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'upscaled_image.png')
                    cv2.imwrite(output_file_path, upscaled_image)
                    return jsonify({'success': True, 'output_file': url_for('uploaded_file', filename='upscaled_image.png')})
                else:
                    return jsonify({'error': error_message})
                

            except Exception as e:
                return jsonify({'error': 'An error occurred: ' + str(e)})

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
