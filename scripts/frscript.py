import cv2
import csv
import os
import face_recognition
import datetime

known_faces = []
known_names = []

for filename in os.listdir('faces'):
    image = face_recognition.load_image_file(os.path.join('faces',filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splittext(filename)[0])

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame_face_locations)

    recognized_names = []
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces,face_encoding)
        name = 'Unknown'

        if True in matches:
            matched_indices = [i for i, match in enumerate(matches) if match]
            for index in matched_indices:
                name = known_names[index]
                recognized_names.append(name)


    cv2.imshow('Camera', frame)

    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)