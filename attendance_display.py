import pandas as pd

def display_attendance():
    attendance_register_filename = "attendance_register.csv"

    # Read the CSV file using pandas
    df = pd.read_csv(attendance_register_filename)

    # Display the details in a formatted table
    print("\nAttendance Register")
    print("-------------------")
    print(df.to_string(index=False, justify='center', col_space=15))


