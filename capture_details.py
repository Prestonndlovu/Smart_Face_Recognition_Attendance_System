import csv
import os
import cv2

def capture_details():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    id_number = input("Enter your ID number: ")

    csv_file = create_csv()

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, id_number])

    print("Details saved in CSV file.")

    capture_picture(name)
    print("Picture captured.")

def create_csv():
    csv_file = "Student_details.csv"

    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Surname", "ID"])

    return csv_file

def capture_picture(name):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not found or unable to access.")
        return

    print("Press 'c' to capture picture...")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        cv2.imshow("Capture Picture", frame)

        key = cv2.waitKey(1)
        if key == ord('c'):
            picture_filename = os.path.join("known",f"{name}.jpg")
            cv2.imwrite(picture_filename, frame)
            print(f"Picture captured and saved as {picture_filename}")
            break

    cap.release()
    cv2.destroyAllWindows()
