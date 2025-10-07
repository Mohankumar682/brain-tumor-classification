# 🧠 Brain Tumor Detection Web App

A **Django-based web application** that detects **brain tumors from MRI images** using a **TensorFlow deep learning model**.  
This web app allows users to upload MRI scans and receive real-time tumor detection results.  
The model is saved in **TensorFlow SavedModel format** (instead of `.h5`).

---

## 🚀 Features
- Upload brain MRI images directly from the browser  
- Detect tumor presence using a TensorFlow model  
- Display uploaded image with prediction result  
- Built using Django + TensorFlow + Pillow  
- Model saved in modern **SavedModel** format for stability  

---

## 🏗️ Project Structure
```
BrainTumorApp/
├─ BrainTumorApp/
│ ├─ settings.py
│ ├─ urls.py
│ ├─ wsgi.py
├─ detection/
│ ├─ brain_model/ # SavedModel folder (exported from Colab)
│ ├─ templates/
│ │ └─ detection/
│ │ └─ index.html # Frontend UI
│ ├─ urls.py
│ ├─ views.py
│ ├─ apps.py
│ ├─ init.py
├─ manage.py
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/BrainTumorApp.git
cd BrainTumorApp
2️⃣ Create a virtual environment
python -m venv env
```
3️⃣ Activate the environment

Windows:
```
env\Scripts\activate
```

Mac/Linux:
```
source env/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt doesn’t exist yet, create one:

pip install django tensorflow pillow
pip freeze > requirements.txt
```
## 5️⃣ Add your trained model

Copy your exported SavedModel folder (from Google Colab) into:

detection/brain_model/

🧩 Export Model from Google Colab

In your Colab notebook, after training:

model.save("/content/brain_model")  # TensorFlow SavedModel format


Then download that folder and place it inside detection/brain_model/.

🖥️ Run the Django Server
python manage.py runserver


Then open your browser and go to:

http://127.0.0.1:8000/

## 🧪 How It Works

The user uploads an MRI image using the web form.

Django saves the uploaded image temporarily.

TensorFlow model loads and predicts the image.

The result (“Tumor Detected” / “No Tumor”) is shown with the uploaded image.

## 💡 Technologies Used

Python 3.x

Django – Web framework

TensorFlow – Deep learning model

Pillow (PIL) – Image processing

HTML/CSS – Frontend design

## 🛠️ Future Improvements

Add prediction confidence score

Add Grad-CAM visualization for tumor area

Enhance UI using Tailwind or Bootstrap

Add login system for saving prediction history
