import cv2
import face_recognition
import os
import csv
from datetime import datetime

def read_user():
    # Create "known" folder if it doesn't exist
    known_folder = "known"
    if not os.path.exists(known_folder):
        os.makedirs(known_folder)

    # Initialize webcam capture
    cap = cv2.VideoCapture(0)

    captured_image = None

    while True:
        ret, frame = cap.read()

        # Show the live webcam feed
        cv2.imshow('Live Feed', frame)

        # Capture image using the 'c' key
        if cv2.waitKey(1) & 0xFF == ord('c'):
            captured_image = frame
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

    if captured_image is not None:
        # Save the captured image in the "images" folder
        images_folder = "images"
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)

        image_filename = os.path.join(images_folder, "captured_image.jpg")
        cv2.imwrite(image_filename, captured_image)

        # Load captured image and perform face recognition
        captured_face_image = face_recognition.load_image_file(image_filename)
        captured_face_encoding = face_recognition.face_encodings(captured_face_image)[0]

        # Load known face encodings and names from the "known" folder
        known_face_encodings = []
        known_face_names = []

        for filename in os.listdir(known_folder):
            if filename.endswith(".jpg"):
                image = face_recognition.load_image_file(os.path.join(known_folder, filename))
                encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(os.path.splitext(filename)[0])

        # Compare captured face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, captured_face_encoding)
        recognized_name = "Unknown"
        attendance = False

        if True in matches:
            matched_index = matches.index(True)
            recognized_name = known_face_names[matched_index]
            attendance = True
            store_attendance(recognized_name, attendance)

        print("Recognized Name:", recognized_name)
    else:
        print("No image captured.")

def store_attendance(student_name, attendance_status):
    attendance_register_filename = "attendance_register.csv"

     # Create or append the attendance register CSV file with specified headings

    with open(attendance_register_filename, 'w', newline='') as file:
         writer = csv.writer(file)
         writer.writerow(["Name", "Attendance Status", "Timestamp"])


    # Append attendance details to the attendance register CSV file
    with open(attendance_register_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([student_name, attendance_status, timestamp])


