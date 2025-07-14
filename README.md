# Mini Blog Platform:
A simple blog platform built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy (Sync)**. This project allows users to register (sign up), simulate login (using a dummy method), create blog posts, and retrieve their own posts.

# Features:
- User registration (store in DB)
- Simulated login via hardcoded user (can be upgraded to real auth)
- Create new blog posts (authenticated user only)
- Retrieve all posts for the current user
- Retrieve a specific post by ID (only if owned by the user)

📁 Project Structure
--------------------

mini_blog/
├── app/
│   ├── users/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── services.py
│   │   ├── routers.py
│   ├── posts/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── services.py
│   │   ├── routers.py
│   ├── database.py
│   ├── config.py
├── main.py
├── requirements.txt
└── README.txt

🛠️ How to Run the Project
--------------------------

1. Clone the Repo:
   git clone <your_repo_url>

2. Navigate to the project directory:
   cd mini_blog

3. Create virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

4. Configure `.env` file (use `.env.example` as a reference).

5. Start the server:
   uvicorn main:app --reload

🧪 How to Test Endpoints (via Swagger UI)
----------------------------------------

Visit: http://127.0.0.1:8000/docs

### USER Functionality (Dummy Auth for now)

- All endpoints use a simulated `get_current_user` method which returns a hardcoded UUID of an existing user.

- Ensure a user exists in the DB with this UUID before testing.

- Replace this UUID with a real one from your database if needed.

### POSTS Endpoints

- **POST /posts/** - Create a post (must be logged in via dummy user)
- **GET /posts/** - Retrieve all posts by current user
- **GET /posts/{post_id}** - Retrieve a single post (only if owned)

🧠 Implementation Approach
---------------------------

- `get_current_user` checks the user in DB using a hardcoded UUID.
- Posts are linked to the currently "logged in" user.
- Each route uses `Depends(get_current_user)` to simulate auth.
- Easily replaceable with real JWT-based auth later.
