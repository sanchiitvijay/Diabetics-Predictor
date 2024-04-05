# from flask import Flask, render_template, request
# from image_processing import process_image

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get image data from the request
#     image_data = request.form['image_data']
    
#     # Process the image using imported function
#     result = process_image(image_data)
    
#     # Return the result
#     return result

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Set your Kaggle API key
KAGGLE_API_KEY = 'kaggle kernels pull suhas1901/final-stage-1-diacure'

# Endpoint to handle image upload and fetch text from Kaggle API
@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # Ensure file has a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save the uploaded image temporarily
    temp_image_path = 'temp_image.jpg'
    file.save(temp_image_path)

    
    # Prepare headers for Kaggle API request
    headers = {"Authorization": f"Bearer {KAGGLE_API_KEY}"}
    
    # Prepare data for Kaggle API request
    files = {'file': open(temp_image_path, 'rb')}
    
    # Make request to Kaggle API to extract text from image
    response = requests.post('https://suhas1901/final-stage-1-diacure', headers=headers, files=files)
    print("hi")
    
    # Check if request was successful
    if response.status_code == 200:
        extracted_text = response.json()
        os.remove(temp_image_path)  # Remove temporary image file
        return jsonify({'text': extracted_text}), 200
    else:
        os.remove(temp_image_path)  # Remove temporary image file
        return jsonify({'error': 'Failed to extract text from image'}), 500

if __name__ == '__main__':
    app.run(debug=True)
