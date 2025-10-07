from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
import numpy as np
from PIL import Image
import os

# Load model once when the server starts
MODEL_PATH = os.path.join(os.path.dirname(__file__), "brain_tumor.keras")
model = load_model(MODEL_PATH, compile=False)  # compile=False to skip optimizer warnings

# Define the class names (use your actual labels)
CLASS_NAMES = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

# Image size used during training
IMAGE_SIZE = (128, 128)  # change if your model uses a different size

def home(request):
    result = None
    uploaded_image_url = None

    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_image_url = fs.url(filename)
        filepath = fs.path(filename)

        try:
            # Load and preprocess the image
            img = Image.open(filepath).convert("RGB")
            img = img.resize(IMAGE_SIZE)
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

            # Make prediction
            predictions = model.predict(img_array)
            predicted_index = np.argmax(predictions[0])
            result = CLASS_NAMES[predicted_index]

        except Exception as e:
            result = f"Error processing image: {e}"

    return render(request, "home.html", {"result": result, "uploaded_image_url": uploaded_image_url})
