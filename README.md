# Face Recognition System with Firebase Integration 🤖

This project demonstrates a face recognition system that integrates with Firebase for storing images and related data. Using Python, OpenCV, and the `face_recognition` library, the system processes face images, generates encodings, and stores them in Firebase Realtime Database and Firebase Storage. The solution can be extended for real-time facial recognition in applications such as healthcare, security, and user authentication systems.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Image Processing and Upload](#1-image-processing-and-upload)
  - [Storing User Data](#2-storing-user-data)
  - [Encoding Faces](#3-encoding-faces)
- [Firebase Setup](#firebase-setup)
- [License](#license)

## Features 🌟
- **Facial Recognition:** Converts images into encodings for later use in facial recognition systems.
- **Firebase Storage Integration:** Stores processed images in Firebase Storage for secure and scalable access.
- **Realtime Database Integration:** Stores metadata like user details (name, age, last attendance) in Firebase Realtime Database.
- **Automated Data Upload:** Easily upload user data and images to Firebase with minimal configuration.
- **Local File Management:** Save facial encodings as pickle files for quick access.

## Technologies Used 🛠️
- **Python 3.x**: Primary language used for the scripts.
- **OpenCV**: For image processing.
- **face_recognition**: For generating face encodings.
- **Firebase Admin SDK**: For Firebase Realtime Database and Storage management.
- **Pickle**: For serializing and saving the face encodings locally.

## Prerequisites 📋
Ensure you have the following tools and libraries installed:
- Python 3.x
- Firebase account with a Realtime Database and Firebase Storage set up.
- The following Python libraries:
  ```bash
  pip install opencv-python face_recognition firebase-admin

## Usage 🚀

### 1. Image Processing and Upload
Run `first.py` to process images, generate face encodings, and upload images to Firebase Storage.
  ```bash
  python first.py
  ```
This script:

- Reads images from the faceapp/interface/ folder.
- Uploads the images to Firebase Storage.
- Prints the image paths and names.

### 2. Storing User Data
Run database.py to upload user data to Firebase Realtime Database.
  ```bash
  python database.py
  ```
This script:

- Uploads predefined user data (name, age, attendance) to Firebase under the Details node.

### 3. Encoding Faces
Run encode.py to generate facial encodings and save them locally in a pickle file.
  ```bash
  python encode.py
  ```
This script:

- Reads images from the img directory.
- Encodes the faces.
- Saves the encodings and corresponding image names in Encodings.p.

## Firebase Setup 🔧

### 1. Project Creation 
- Create a new project in [Firebase Console](https://console.firebase.google.com/).

### 2. Enable Realtime Database and Storage
- In your Firebase project, enable **Firebase Realtime Database** and **Firebase Storage** under the "Build" section.

### 3. Service Account Key
- Go to your Firebase project's settings.
- Under **Service Accounts**, generate a new private key and download the `serviceAccountKey.json` file.
- Place this file in the `faceapp/` folder.

### 4. Update Firebase Config
- Ensure that the `databaseURL` and `storageBucket` values in your Python scripts match your Firebase project settings. You can find these details in the Firebase Console under **Project Settings > General**.

## License 📜

**MIT License**

Copyright (c) 2024 Maha Sriee Prasenna

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please visit [GitHub: maha-sriee-prasenna](https://github.com/maha-sriee-prasenna).


