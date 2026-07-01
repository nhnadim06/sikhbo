# Sikhbo.io 🎓

**Sikhbo** is a Django-based e-learning platform where users can browse courses, enroll, and learn. Users with the Admin role can create, update, and delete courses.


## 🎨 Design

The complete UI/UX design for this project is available on Figma:

🔗 **[Figma Design – Sikhbo.io](https://www.figma.com/design/HNWm7Og1X3n5w8uTwZiP77/Sikhbo.io?node-id=0-1&t=RwWNvF246uqMzC3Z-1)**

## ✨ Features

- 🔐 User authentication (Signup / Login / Logout)
- 👤 Role-based access control (Admin / User) with editable user profiles
- 📚 Course catalog with categories (Career Track, Foundation, Free courses)
- 📝 Course details page with related course suggestions
- 🛠️ Admin-only course management (create, update, delete)
- 📈 Enrollment tracking with live student count
- 📊 Platform statistics (total students, courses, videos, enrollments)
- 🖼️ Instructor profiles with social links

## 🧰 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Design:** Figma

## 📁 Project Structure

```
sikhbo/
├── base/            # Core Django app (models, views, forms, admin)
├── eLearning/        # Project settings, URLs, WSGI/ASGI config
├── media/            # Uploaded media (course thumbnails, category icons)
├── static/            # Static assets (CSS, images)
├── template/          # HTML templates
├── db.sqlite3         # SQLite database
└── manage.py          # Django management script
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/nhnadim06/sikhbo.git
cd sikhbo

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000/`

## 🤝 Contributing

Contributions are always welcome! Feel free to open an Issue or a Pull Request.

## 📄 License

This project currently has no license specified.

## 📬 Contact

Maintainer: [nhnadim06](https://github.com/nhnadim06)
