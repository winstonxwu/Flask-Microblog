# Flask-Microblog

A simple yet robust microblogging application built with Flask, providing users with a platform to create and share short posts. This project serves as a foundational example for developing web applications using the Flask framework, demonstrating key concepts such as user authentication, database management, and templating.

## Table of Contents

* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## Features

* **User Authentication:** Secure user registration and login system.
* **Post Creation:** Users can create, view, and manage their microblog posts.
* **Database Integration:** Uses a SQLite database (or configurable to other SQL databases) for storing user and post data.
* **Templating:** Dynamic content rendering using Jinja2 templates.
* **Form Handling:** Secure form submission and validation using Flask-WTF.
* **Responsive Design:** Basic styling for a user-friendly experience.

---

## Technologies Used

* **Python:** The core programming language.
* **Flask:** Web framework for building the application.
* **Flask-SQLAlchemy:** ORM (Object Relational Mapper) for database interaction.
* **Flask-Migrate:** Database migrations with Alembic.
* **Flask-Login:** User session management.
* **Flask-WTF:** Form handling and CSRF protection.
* **SQLite:** Default database for development.
* **HTML/CSS:** Frontend structure and styling.

---

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/winstonxwu/Flask-Microblog.git
    cd Flask-Microblog
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Initialize the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
    If you encounter issues with `flask db`, ensure your `FLASK_APP` environment variable is set (e.g., `export FLASK_APP=app.py` or `set FLASK_APP=app.py`).

---

## Usage

1.  **Run the Flask application:**
    ```bash
    flask run
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address shown in your terminal).

3.  **Register and Log In:**
    Create a new user account or log in with existing credentials to start posting.

---
## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
