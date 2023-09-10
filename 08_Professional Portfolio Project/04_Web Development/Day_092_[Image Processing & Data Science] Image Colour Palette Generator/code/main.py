from flask import Flask, render_template, send_from_directory, url_for, request
from flask_uploads import UploadSet, IMAGES, configure_uploads  # pip install Flask-Uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

import numpy as np
from PIL import Image


# refer to the tutorial below for image-uploading web app:
# https://www.youtube.com/watch?v=dP-2NVUgh50


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KINWAESWD6F3XDS1'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'  # The name should be the same as the folder you created.

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')


# Got this from ChatGPT
def get_top_10_most_common_rgb(rgb_array):
    # Reshape the image array to a 3D array (pixels x 1 x channels)
    reshaped_array = rgb_array.reshape(-1, 1, 3)

    # Get unique RGB values and their counts
    unique_values, counts = np.unique(reshaped_array, axis=0, return_counts=True)

    # Sort the unique values based on their counts in descending order
    sorted_indices = np.argsort(counts)[::-1]

    # Get the top 10 most common RGB values
    top_10_rgb_values = unique_values[sorted_indices[:10]]

    # Return the top 10 most common RGB values
    return top_10_rgb_values


# Got this from ChatGPT
def rgb_to_hex(rgb_array):
    hex_array = []
    for row in rgb_array:
        hex_row = []
        for pixel in row:
            hex_value = '#{:02X}{:02X}{:02X}'.format(pixel[0], pixel[1], pixel[2])
            hex_row.append(hex_value)
        hex_array.append(hex_row)
    return np.array(hex_array)


def get_top_10_most_common_hexes(uploaded_photo):
    # Convert the uploaded photo to a PIL Image object
    image = Image.open(uploaded_photo)

    # Convert the image to a NumPy array
    rgb_array = np.array(image)

    # Get the top 10 most common RGB values
    top_10_rgb_array = get_top_10_most_common_rgb(rgb_array)

    # Convert RGB array to hex array
    top_10_hex_array = rgb_to_hex(top_10_rgb_array)

    # Got this from ChatGPT
    # Flatten the nested list
    top_10_hex_flat = top_10_hex_array.flatten()

    return top_10_hex_flat


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)

        # Access the uploaded photo
        uploaded_photo = request.files['photo']

        top_10_hex_flat = get_top_10_most_common_hexes(uploaded_photo)
        # print(top_10_hex_flat)

    else:
        file_url = None
        top_10_hex_flat = None

    return render_template('index.html', form=form, file_url=file_url, top_10_hex_flat=top_10_hex_flat)


if __name__ == '__main__':
    app.run(debug=True)
