import cv2
import dlib
import numpy as np
import face_recognition
import os

print("Initializing")
print("Loading Smile! Detection")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_81_face_landmarks.dat')

known_faces = []
known_names = []
authenticated = False
print('Loading recognition')

for filename in os.listdir('known_people'):
    image = face_recognition.load_image_file(os.path.join('known_people',filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])





face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
matched = False
smiling = False
print("Smile!")

video_capture = cv2.VideoCapture(0)

while True:
    
    ret, frame = video_capture.read()

    
    rgb_frame = frame[:, :, ::-1]

    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Convert the image to grayscale for smile detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        if True in matches:
            matched = True
            for rect in faces:
                shape = predictor(gray, rect)               
                left = (shape.part(48).x, shape.part(48).y)
                right = (shape.part(54).x, shape.part(54).y)
                distance = np.sqrt((right[0] - left[0]) ** 2 + (right[1] - left[1]) ** 2)
                print(distance)
                
                if distance > 68:  
                    smiling = True
                    print("Face recognized and person is smiling")
                    authenticated = True
                else:
                    smiling = False
                    print("Face recognized but person is not smiling")

        else:
            matched = False
            print("Face not recognized")

    process_this_frame = not process_this_frame
    
    cv2.imshow('Video', frame)
    if authenticated == True:
        print("Nice smile! Your payment has been sent!")
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
