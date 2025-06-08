# Hospital-Management-System

## 1. Project Overview

This is a Python-based hospital appointment management system with a graphical user interface (GUI) built using Tkinter. It allows users to enter patient details, schedule appointments, and store the data securely in a MySQL database.
The system is intended to help hospitals or clinics manage basic appointment-related tasks more efficiently.

## 2. Features

1. Connects to a MySQL database to create and manage tables.
2. Stores patient details such as ID, name, age, gender, phone number, and blood group.
3. Allows appointment scheduling with a specific doctor and date.
4. Uses a GUI for user input and display using Tkinter.
5. Generates random unique appointment numbers.

## 3. Requirements

To run this system, you need to have the following installed:

* Python 3
* MySQL Server
* `mysql-connector-python` module (install via `pip install mysql-connector-python`)
* Tkinter (usually included with Python)

## 4. How It Works

1. The program first connects to a MySQL server using the `mysql.connector` module.
2. It checks if the database `Hospital2` exists, and creates it if not.
3. It defines two tables:

   * `appointment`: stores patient personal details.
   * `appointment_details`: stores information about the assigned doctor and appointment date.
4. The user interface allows data entry and submission, and displays messages using `tkinter.messagebox`.

## 5. Usage Instructions

1. Make sure your MySQL server is running.
2. Open the script file (`HospitalSystem.py`) in any Python IDE or terminal.
3. Run the script to launch the GUI.
4. Enter patient and appointment details in the fields provided.
5. Submit the form to save data in the database.

## 6. Notes

* The database credentials are hardcoded in the script. Update the `host`, `user`, and `password` fields according to your MySQL setup.
* Ensure that the MySQL service is running when you use the application.
* This system uses basic security; avoid using it in production environments without enhancements.

## 7. Future Improvements

* Add login authentication for hospital staff.
* Include a search and update feature for appointments.
* Improve data validation (e.g., phone number format, age constraints).
* Add PDF or print functionality for appointment slips.

