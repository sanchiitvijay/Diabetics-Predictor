from flask import Flask, render_template, request
from image_processing import process_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get image data from the request
    image_data = request.form['image_data']
    
    # Process the image using imported function
    result = process_image(image_data)
    
    # Return the result
    return result

if __name__ == '__main__':
    app.run(debug=True)
