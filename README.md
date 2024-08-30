Real-Time Face Recognition
This Python script performs real-time face recognition using the face_recognition library and OpenCV. It captures video from a webcam, compares detected faces to a database of known faces, and displays the recognized faces with labels.

Features
Real-Time Face Recognition: Identifies and labels faces from the webcam feed.
Dynamic Face Matching: Compares detected faces against a collection of known faces.
Efficient Processing: Processes every other frame to speed up the recognition.

Requirements
Python 3.x
face_recognition library
OpenCV library
NumPy library
Install the required libraries using pip:
pip install face_recognition opencv-python numpy

Usage
Prepare Known Faces:

Place images of known individuals in subfolders under outputphoto directory.
Each subfolder should be named after the person, and contain their face images.
Run the Script
Webcam Access: Ensure your webcam is connected and accessible.

Recognition:

The script will open a window displaying the live webcam feed.
Detected faces will be compared against the known faces, and recognized faces will be labeled with names.
Exit:

Press the 'q' key to stop the script and close the video feed window.
Code Overview
Load Known Faces: Reads face images from a specified directory and encodes them for comparison.
Video Capture: Captures frames from the webcam.
Face Detection and Recognition: Finds faces in the frame, encodes them, and matches them to known faces.
Display Results: Draws rectangles and labels around recognized faces in the video feed.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests for enhancements or bug fixes.

This README provides a detailed overview of how to set up, use, and understand the face recognition script. It includes information on dependencies, preparation steps, and how to run and exit the script.








