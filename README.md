Flask-Microblog

A simple yet robust microblogging application built with Flask, providing users with a platform to create and share short posts. This project serves as a foundational example for developing web applications using the Flask framework, demonstrating key concepts such as user authentication, database management, and templating.
Table of Contents

    Features

    Technologies Used

    Installation

    Usage

    Project Structure

    Contributing

    License

    Contact

Features

    User Authentication: Secure user registration and login system.

    Post Creation: Users can create, view, and manage their microblog posts.

    Database Integration: Uses a SQLite database (or configurable to other SQL databases) for storing user and post data.

    Templating: Dynamic content rendering using Jinja2 templates.

    Form Handling: Secure form submission and validation using Flask-WTF.

    Responsive Design: Basic styling for a user-friendly experience.

Technologies Used

    Python: The core programming language.

    Flask: Web framework for building the application.

    Flask-SQLAlchemy: ORM (Object Relational Mapper) for database interaction.

    Flask-Migrate: Database migrations with Alembic.

    Flask-Login: User session management.

    Flask-WTF: Form handling and CSRF protection.

    SQLite: Default database for development.

    HTML/CSS: Frontend structure and styling.

Installation

To get a local copy up and running, follow these simple steps.
Prerequisites

    Python 3.x

    pip (Python package installer)

Steps

    Clone the repository:

    git clone https://github.com/winstonxwu/Flask-Microblog.git
    cd Flask-Microblog

    Create a virtual environment (recommended):

    python -m venv venv

    Activate the virtual environment:

        On Windows:

        .\venv\Scripts\activate

        On macOS/Linux:

        source venv/bin/activate

    Install the required dependencies:

    pip install -r requirements.txt

    Initialize the database:

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

    If you encounter issues with flask db, ensure your FLASK_APP environment variable is set (e.g., export FLASK_APP=app.py or set FLASK_APP=app.py).

Usage

    Run the Flask application:

    flask run

    Access the application:
    Open your web browser and navigate to http://127.0.0.1:5000/ (or the address shown in your terminal).

    Register and Log In:
    Create a new user account or log in with existing credentials to start posting.

Project Structure

Flask-Microblog/
├── app/
│   ├── __init__.py         # Application factory
│   ├── models.py           # Database models
│   ├── forms.py            # WTForms for user input
│   ├── routes.py           # URL routes and view functions
│   └── templates/          # Jinja2 HTML templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── ...
├── migrations/             # Alembic migration scripts
├── venv/                   # Python virtual environment
├── config.py               # Application configuration
├── requirements.txt        # Python dependencies
├── app.py                  # Main application entry point
├── boot.sh                 # (Optional) Script for deployment/startup
└── README.md               # This README file

Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

    Fork the repository.

    Create your feature branch (git checkout -b feature/AmazingFeature).

    Commit your changes (git commit -m 'Add some AmazingFeature').

    Push to the branch (git push origin feature/AmazingFeature).

    Open a Pull Request.

License

Distributed under the MIT License. See LICENSE for more information.
