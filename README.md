🚗 Smart Parking Management System
This is a Smart Parking Management web application built with Python, Streamlit, SQLite, and Tesseract OCR. It allows users to book parking slots by uploading an image of their vehicle (with a visible number plate). The number plate is detected using image processing, and the data is saved with user login functionality. Admins can view all data, remove vehicles, and export records.

🛠️ Features
User Registration & Login
Admin Panel with secured access
Upload vehicle image for number plate detection
Automatic slot booking (first available)
View current parked vehicles
Remove vehicle after exit
Export all parking data to Excel (.xlsx)
Duration calculation of parking
🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/smart-parking-system.git
cd smart-parking-system
2. Install dependencies
Make sure Python 3.10+ is installed. Then install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Install Tesseract OCR
Download and install from Tesseract OCR Windows:

✅ Important: Note the install path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe) and update it in your number_plate_detection.py:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶️ Run the App
bash
Copy
Edit
streamlit run smart_parking_app.py
Visit: http://localhost:8501

Navigate to sidebar to Login/Register as user or admin.

👤 Admin Credentials
text
Copy
Edit
Username: admin
Password: admin123
📂 Project Structure
bash
Copy
Edit
smartpark/
│
├── smart_parking_app.py          # Main entry file
├── parking_db.py                 # Parking database functions
├── users_db.py                   # User login/register DB
├── number_plate_detection.py     # OCR detection code
├── pages/
│   ├── user_dashboard.py         # Logged-in user interface
│   └── admin_panel.py            # Admin features
│
├── vehicle_images/               # Uploaded vehicle images
├── requirements.txt
└── README.md
✅ Requirements
Python 3.10+

Streamlit

OpenCV (opencv-python)

Tesseract OCR

SQLite (default in Python)

Pandas

openpyxl

📦 requirements.txt
text
Copy
Edit
streamlit
opencv-python
pytesseract
pillow
pandas
openpyxl
🚀 Future Improvements
Manual slot selection

Email/SMS notification

Admin dashboard UI enhancement

Multiple admin roles

🙌 Authors
Yuvraj Rajure

TEAM AVINYA | Sanjivani College of Engineering




