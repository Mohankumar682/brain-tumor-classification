# NeuroScan - Brain Tumor Detection Web App

This is a Django web application for brain tumor detection using MRI images and a deep learning model.

## Setup Instructions

### 1. Clone the Repository
Clone or download the project files to your local machine.

### 2. Create a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```
If `requirements.txt` is missing, install manually:
```
pip install django keras pillow numpy
```

### 4. Apply Migrations
```
python manage.py migrate
```

### 5. Run the Development Server
```
python manage.py runserver
```

### 6. Access the Application
Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 7. Upload MRI Images
- Use the web interface to upload an MRI image and get instant analysis.

## Notes
- Uploaded images are stored in the `media/` folder.
- The Keras model file should be present at `predictor/brain_tumor.keras`.
- For production, set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`.

## Troubleshooting
- If you see errors about missing packages, install them with `pip` as shown above.
- If images do not display, ensure `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py` and media serving is enabled in `urls.py` (already configured for development).

---

**Disclaimer:** This tool is for informational purposes only and not a substitute for medical advice.
