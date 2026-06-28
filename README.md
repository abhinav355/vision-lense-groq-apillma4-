# VisionLense

VisionLense is a simple desktop app that lets you use AI to understand what your camera sees.

Just start your camera, click **Analyze Scene**, and the AI will describe everything it can see in the image. It uses Groq's fast AI models to analyze the captured frame and generate a detailed description.

---

## What Can It Do?

* View your webcam feed
* Capture an image from the camera
* Send the image to AI for analysis
* Describe objects, people, colors, lighting, and the overall scene
* Run as a desktop application using Python

---

## How to Use

### Step 1: Get a Groq API Key

VisionLense uses Groq's AI models, so you'll need a free API key.

1. Go to https://console.groq.com
2. Create an account
3. Open the API Keys section
4. Generate a new API key
5. Copy the key

---

### Step 2: Start the App

Install the required packages:

```bash
pip install groq pywebview
```

Then run:

```bash
python main.py
```

---

### Step 3: Enter Your API Key

When the app opens:

1. Paste your Groq API key into the input box.
2. Click **Save API Key**.

You should see:

```text
API key saved ✔
```

---

### Step 4: Start Your Camera

Click:

```text
Start Camera
```

Allow camera permissions if your system asks.

Your webcam feed should now appear on the left side of the window.

---

### Step 5: Analyze the Scene

Click:

```text
Analyze Scene
```

VisionLense will:

1. Capture the current camera frame.
2. Send it to Groq's AI model.
3. Receive an AI-generated description.
4. Display the result in the right panel.

Example output:

```text
The image shows a desk with a laptop and a keyboard. The room appears dimly lit. A monitor is visible in the background...
```

---

## Project Files

```text
VisionLense/
│
├── main.py      # Python backend
├── UI.html      # User interface
└── README.md
```

---

## Technologies Used

### Backend

* Python
* Groq API
* PyWebView

### Frontend

* HTML
* CSS
* JavaScript

### AI Model

* meta-llama/llama-4-scout-17b-16e-instruct

---

## Requirements

* Python 3.9 or newer
* Webcam
* Internet connection
* Groq API key

---

## Known Limitations

* Requires an internet connection.
* Analysis quality depends on image quality.
* Very dark or blurry images may produce inaccurate descriptions.
* Groq API rate limits may apply on free accounts.

---

## Why I Made This

I built VisionLense to learn how AI vision models work and how Python can communicate with a modern web interface. The project combines webcam access, desktop app development, and AI image understanding into a simple application that anyone can use.

---

Made with ❤️ using Python, Groq, HTML, CSS, and JavaScript.

---

##New upd

ok so i just changed the promt of groq in index.py basicly now it will search for products and find data about it i guess its cool
