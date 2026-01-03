# 📚 Django Digital Library System

A clean, production-ready Django project to manage a physical library: books inventory, categories, statuses (available, sold, rented), and profit reporting. Built to practice CMS patterns and offer a practical tool for small libraries.



## 📖 Project Overview
This isn’t just a bookstore UI—it’s a real library management system.  
Track total books, available vs. sold vs. rented, and compute profits from sales and rentals, with quick search and AJAX filters for category and status.

---

## ✨ Key Features
- **Dashboard:** Instant stats for total, available, sold, and rented books.  
- **Book CRUD:** Create, update, delete directly from the UI.  
- **Book fields:** Title, author, cover image, price, page count.  
- **Categories:** Dynamic category creation and assignment.  
- **Status tracking:** Available, Sold, Rented with quick toggles.  
- **Financials:** Automatic profits from sales and rentals.  
- **Search and filters:** Text search, category filter, and AJAX status filter.  



## 🛠 Tech Stack
- **Backend:** Python, Django  
- **Database:** SQLite (default)  
- **Frontend:** HTML, CSS, Bootstrap, JavaScript (AJAX)  



## ⚙️ Setup

1. Clone the repository
2. git clone https://github.com/abdalahhamwi/Django-Digital-Library-System.git 
3. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the development server
python manage.py runserver
6. Open in browser
http://127.0.0.1:8000
