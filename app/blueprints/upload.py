import io
from flask import Blueprint, request, jsonify
from PIL import Image

upload = Blueprint("upload", __name__)

@upload.route('/upload', methods=["POST"])
def post_metadata():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'})
    
    # get the file from the request
    file = request.files['file']
    
    # check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'no selected file'})
    
    # read the image data
    img_data = file.read()
    
    # create an image object from the data
    img = Image.open(io.BytesIO(img_data))
    
    # get the metadata
    metadata = {
        'filename': file.filename,
        'width': img.width,
        'height': img.height,
        'format': img.format,
        'mode': img.mode
    }
    
    # return the metadata as JSON
    return jsonify(metadata)
