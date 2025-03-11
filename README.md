# Phishing-website-detection-using-machine-learning

The URL Classifier Chrome extension allows users to classify URLs as Legitimate or Phishing by analyzing various features of the URL. This extension communicates with a backend server built using Flask, which uses a pre-trained machine learning model to classify the URLs.



## Features

- Classify URLs: Classifies a URL as Phishing or Legitimate based on the URL's structure and characteristics.
- Real-time Classification: Enter a URL and get immediate feedback within the browser popup.
- Machine Learning Powered: The classification is powered by a trained Random Forest model.

## Technologies Used 

- Frontend:

  - HTML, CSS, and JavaScript for the extension popup.
  - Fetch API for communicating with the backend.

- Backend:

  - Flask (Python) to serve the classification model.
  - Scikit-learn for building and training the Random Forest model.
  - Joblib for saving and loading the trained model.
 
- Chrome Extension:

  - Manifest V3 for Chrome extensions.
  - Event listeners and background scripts for extension functionality.

## Installation

Clone the repository:

git clone <repository-url>

This will clone all the folders and files to your device's current working directory

## Setting Up the Backend

- Install required Python libraries:

  pip install -r requirements.txt

- Start the Flask server:

  python app.py
  This will run the Flask backend locally on http://127.0.0.1:5000.

## Setting Up the Chrome Extension
- Open Google Chrome and navigate to chrome://extensions/.
- Enable Developer Mode (top right).
- Click on Load unpacked and select the extension's directory (where manifest.json is located).
- The extension icon will appear in your toolbar, ready to use!

  
