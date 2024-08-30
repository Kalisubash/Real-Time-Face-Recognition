import face_recognition
import cv2
import os
import numpy as np

# Base directory where known faces are stored in subfolders
base_dir = r"C://Users//ransu//Documents//Python//outputphoto"

# Initialize lists to hold face encodings and their names
known_face_encodings = []
known_face_names = []

# Load the known faces and their encodings from subfolders
for person_name in os.listdir(base_dir):
    person_dir = os.path.join(base_dir, person_name)
    
    if os.path.isdir(person_dir):  # Check if it's a directory
        for filename in os.listdir(person_dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Load each image file
                image_path = os.path.join(person_dir, filename)
                image = face_recognition.load_image_file(image_path)
                
                # Encode the face(s) in the image
                face_encodings = face_recognition.face_encodings(image)
                
                if len(face_encodings) > 0:  # Ensure that at least one face was found
                    known_face_encodings.append(face_encodings[0])
                    known_face_names.append(person_name)  # Use the folder name as the person's name
                else:
                    print(f"No faces found in {filename} (in {person_name} folder). Skipping this file.")

# Initialize variables for real-time face recognition
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Start video capture from the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a single frame from the webcam
    ret, frame = video_capture.read()
    
    # Resize the frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # Convert the image from BGR color (OpenCV format) to RGB color (face_recognition format)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for any known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame was resized to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Hit 'q' on the keyboard to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
video_capture.release()
cv2.destroyAllWindows()
