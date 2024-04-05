import base64
from io import BytesIO
from PIL import Image
import numpy as np
import pickle

diagnosis_dict_binary = {
    0: 'No_DR',
    1: 'DR',
    2: 'DR',
    3: 'DR',
    4: 'DR'
}

diagnosis_dict = {
    0: 'No_DR',
    1: 'Mild',
    2: 'Moderate',
    3: 'Severe',
    4: 'Proliferate_DR',
}

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == '__main__':
            if name == 'diagnosis_dict_binary':
                return diagnosis_dict_binary
        return super().find_class(module, name)

# Load the .pkl file using CustomUnpickler
with open('dd.pkl', 'rb') as f:
    loaded_model = CustomUnpickler(f).load()


# with open('dd.pkl', 'rb') as f:
#     loaded_model = pickle.load(f)

def preprocess_image(image):
    # Resize, normalize, etc.
    image = image.resize((224, 224))  # Assuming input size of the model is 224x224
    image = np.array(image) / 255.0  # Normalize pixel values
    return image


def process_image(image_data):
    preprocessed_image = preprocess_image(image_data)
    # Use the model to get the output
    output_text = loaded_model.predict(preprocessed_image)  # Example; adjust based on your model
    return output_text
