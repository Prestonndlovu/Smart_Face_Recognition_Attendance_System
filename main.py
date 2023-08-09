import csv
import capture_details
import check_camera
import recognize
import os
import attendance_display


def title_bar():
    os.system('cls')  # for windows

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


def main():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture user Details")
    print("[3] Recognize & Mark Attendance")
    print("[4] Display Register")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                check_camera.check_camera()
                break
            elif choice == 2:
                capture_details.capture_details()
                break
            elif choice == 3:
                recognize.read_user()
            elif choice == 4:
                attendance_display.display_attendance()

        except ValueError:
            print("Invalid option try again!")
            main()

if __name__ == "__main__":
    main()
