import cv2
import dlib
import numpy as np
import face_recognition
import os

# Load face detector and shape predictor from dlib
print("Initializing")
print("Loading Smile! Detection")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_81_face_landmarks.dat')

known_faces = []
known_names = []

print('Loading recognition')
# Load images and learn how to recognize them.
for filename in os.listdir('known_people'):
    image = face_recognition.load_image_file(os.path.join('known_people',filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])




# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
matched = False
smiling = False
print("Smile!")
# Start the webcam feed
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Convert the image to grayscale for smile detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if this face is a match for the known face
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        if True in matches:
            matched = True
            for rect in faces:
                # Determine the facial landmarks for the face region
                shape = predictor(gray, rect)

                # Get the coordinates of the left and right corners of the mouth
                left = (shape.part(48).x, shape.part(48).y)
                right = (shape.part(54).x, shape.part(54).y)

                # Calculate the euclidean distance between the left and right corners of the mouth
                distance = np.sqrt((right[0] - left[0]) ** 2 + (right[1] - left[1]) ** 2)
                print(distance)
                # If the distance is above a certain threshold, consider it a smile
                if distance > 68:  # You may need to adjust this threshold
                    smiling = True
                    print("Face recognized and person is smiling")
                else:
                    smiling = False
                    print("Face recognized but person is not smiling")

        else:
            matched = False
            print("Face not recognized")

    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        
        if smiling and matched:
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
