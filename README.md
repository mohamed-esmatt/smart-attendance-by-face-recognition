# Smart Attendance System Using Face Recognition

A modern attendance management system that uses facial recognition technology to automate the attendance tracking process. The system is built with Python and incorporates various technologies for a robust and user-friendly experience.

![Real World Example](readme%20images/smart-attendace.jpg)

## Demo

Here's how the face recognition works in action:

![Face Recognition](readme%20images/face%20recognition.jpg)

## Features

- 👤 Face Detection and Recognition
- 📝 Automated Attendance Tracking
- 🔐 Secure Login System with Admin/User roles
- 👥 Student Management System
- 📊 Real-time Data Processing
- 🎤 Voice Feedback System
- 📸 Real-time Camera Integration
- 📱 User-friendly GUI Interface

## Technologies Used

### Frontend

- Tkinter (GUI Framework)
- PIL (Python Imaging Library) for image processing
- Custom-designed user interfaces
- Interactive forms and data display

### Backend

- Python 3.x
- MySQL Database
- OpenCV (cv2) for face detection and recognition
- LBPH Face Recognizer
- Haar Cascade Classifier
- NumPy for numerical computations
- Pandas for data handling

### Additional Libraries

- pyttsx3 for text-to-speech
- tkcalendar for date handling
- mysql-connector-python for database connectivity

## System Requirements

- Python 3.x
- MySQL Server
- Webcam for face detection
- Required Python packages (see Installation section)

## Installation

1. Clone the repository

```bash
git clone https://github.com/mohamed-esmatt/smart-attendance-by-face-recognition.git
```

2. Install required Python packages

```bash
pip install opencv-python
pip install numpy
pip install pillow
pip install mysql-connector-python
pip install pandas
pip install pyttsx3
pip install tkcalendar
```

3. Set up MySQL Database

- Install MySQL Server
- Create a new database
- Configure database connection in the application

## Project Structure

- `login.py` - Main entry point and authentication system
- `face_recognition.py` - Core face detection and recognition functionality
- `student.py` - Student management system
- `train.py` - Training module for face recognition
- `help.py` - Help documentation and guidance
- `about_us.py` - Project information
- `data/` - Directory for storing face images
- `Images/` - UI assets and system images
- `haarcascade_frontalface_default.xml` - Face detection model
- `classifier.xml` - Trained face recognition data

## Usage

1. Start the application by running:

```bash
python login.py
```

![Login Interface](readme%20images/login.jpg)

2. Log in with appropriate credentials

3. Access student management to add or update student records:

![Student Management](readme%20images/inserting%20student.jpg)

4. Train the face recognition model:

![Training](readme%20images/train.jpg)

5. View attendance records:

![Attendance Records](readme%20images/excel.jpg)

6. Access help documentation if needed:

![Help Section](readme%20images/help.jpg)

7. View detailed attendance information:

![Attendance Details](readme%20images/students%20csv%20file.jpg)

- Admin: Full access to all features
- User: Limited access to viewing and attendance features

![Admin Dashboard](readme%20images/admin_dashboard.png)

3. Main Features:
   - Add/Update student information
   - Capture face data for recognition
   - Train the recognition model
   - Take attendance using face recognition
   - View and manage attendance records

## Features in Detail

### Student Management

- Add new students
- Update student information
- Delete student records
- Search and filter capabilities
- Photo sample collection

![Student Management](readme%20images/student_management.png)

### Face Recognition

![Face Recognition](readme%20images/face_recognition.png)

- Real-time face detection
- Accurate recognition system
- Automated attendance marking
- Multiple face detection capability

### Attendance System

- Automated attendance recording
- CSV export functionality
- Date and time tracking
- Attendance history management

![Attendance System](readme%20images/attendance_system.png)

## Security Features

- Secure login system
- Role-based access control
- Password protection
- Data validation and sanitization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenCV community
- Python-MySQL community
- Tkinter documentation
- Face recognition research papers and implementations

## Contact

Mohamed Esmat - [GitHub Profile](https://github.com/mohamed-esmatt)

Project Link: [https://github.com/mohamed-esmatt/smart-attendance-by-face-recognition](https://github.com/mohamed-esmatt/smart-attendance-by-face-recognition)
