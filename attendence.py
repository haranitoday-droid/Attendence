import datetime

# Student database stored as a list of tuples
students = [] # Format: [(student_id, student_name)]
attendance_log = [] # Format: [(student_id, student_name, timestamp, status)]

# Function to add a new student
def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        student_name = input("Enter student name: ").strip()
        
        # Check if the student ID already exists
        if any(student[0] == student_id for student in students):
            print("Student ID already exists. Try again.")
        else:
            students.append((student_id, student_name))
            print(f"Student {student_name} with ID {student_id} added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical student ID.")

# Function to mark attendance
def mark_attendance():
    try:
        student_id = int(input("Enter student ID to mark attendance: "))
        student = next((s for s in students if s[0] == student_id), None)
        
        if student:
            timestamp = datetime.datetime.now()
            attendance_log.append((student[0], student[1], timestamp, "Present"))
            print(f"Attendance marked for {student[1]} at {timestamp}.")
        else:
            print(f"Student ID {student_id} not found. Please add the student first.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical student ID.")

# Function to generate attendance report
def generate_report():
    print("\n--- Attendance Report ---")
    if not attendance_log:
        print("No attendance records available.")
    else:
        for record in attendance_log:
            print(f"ID: {record[0]}, Name: {record[1]}, Time: {record[2]}, Status: {record[3]}")
    print("--------------------------\n")

# Main function to run the system
def attendance_monitoring_system():
    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance")
        print("3. Generate Attendance Report")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
attendance_monitoring_system()


