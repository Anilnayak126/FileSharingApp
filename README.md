# 📁 File Sharing App

A robust file-sharing application built using **Django** and **Django REST Framework** (DRF), combined with **HTML** and **CSS** for the front-end. This project includes advanced REST API capabilities, along with secure file management, upload, and download functionalities. The app also incorporates the `shutil` module for creating ZIP files, enabling users to bundle multiple files for easy sharing and download.

---

## 📌 Features

- **File Upload & Management**: Users can upload files, view file details, and manage their uploads.
- **File Compression**: Multi-file compression into ZIP format using the `shutil` module for efficient storage and download.
- **Secure File Sharing**: Secure access to file downloads with REST API endpoints.
- **RESTful API**: Advanced API endpoints with authentication and authorization for file upload, retrieval, and download.
- **Responsive Design**: A clean, responsive design created with HTML and CSS.

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework, `shutil` for ZIP functionality
- **Frontend**: HTML, CSS
- **Database**: SQLite3

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. **Clone the Repository**

   ```bash
   https://github.com/Anilnayak126/FileSharingApp.git
   cd FileSharingApp



2. **Backend Setup**
   - Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- Install the necessary dependencies
   ```bash
    pip install -r requirements.txt
 - Set up the database and run migrations:
 ```bash
    python manage.py migrate
```
- Create a superuser to access the admin panel (optional):
```bash
python manage.py createsuperuser
```
- Start the Django development server:
```bash
python manage.py runserver
```

3. **📂 Project Structure**
 ```bash
file-sharing-app/
│
├── file_sharing/             # Main Django project directory
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project URL configurations
│   ├── views.py              # API and file management views
│   ├── serializers.py        # DRF serializers
│   ├── models.py             # Database models for file storage
│   └── admin.py              # Admin configurations
│
├── static/                   # HTML and CSS files
│   ├── css/                  # CSS styling for the front-end
│   └── templates/            # HTML templates
│
├── requirements.txt          # List of project dependencies
└── README.md                 # Project documentation
```
4. **🔥 Key Highlights**

- **Advanced API Development**: File management endpoints are structured with RESTful principles, featuring secure file access and comprehensive response handling.
- **File Compression**: Efficient use of Python's shutil to compress multiple files into a single ZIP file, enhancing download efficiency and usability.
- **Secure Access**: Token-based authentication for controlled access to file resources and actions.
- **Simple UI**: HTML/CSS-based front-end for straightforward file upload and management.

5. **📝 Future Improvements**
- **Frontend Framework Integration**: Consider integrating a JavaScript framework (like React or Vue.js) for a more dynamic user interface.
- **Cloud Storage Integration**: Implement cloud storage solutions (like AWS S3 or Google Cloud Storage) for enhanced scalability and file management.
- **User Notifications**: Add email or push notifications to inform users about file uploads or downloads.
**File Versioning**: Introduce file versioning to keep track of changes made to files over time.
   


### Instructions
1. Replace `https://github.com/Anilnayak126/FileSharingApp.git` with the actual URL of your GitHub repository.
2. Update the email address in the contact section to your actual email.
3. Save this content as `README.md` in your project directory.

This enhanced `README.md` provides a detailed overview of your project, guiding users on setup, features, and potential future improvements!

   

