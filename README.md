
## **[MathDeck]**

*Example: "MathDeck is an educational platform for students and teachers, designed to simplify math learning through interactive exercises and personalized material generation."*

-----

### **Features**

A list of the application's key functionalities:

- **Account Management:** User registration and login for students and teachers.
- **Teacher Dashboard:**
  - Student management.
  - Creating and assigning tasks.
  - Sharing educational materials (e.g., PDFs).
- **Student Dashboard:**
  - Access to assigned tasks and materials.
  - Solving and checking tasks in real-time.
- **Security:** Password hashing and secure user session management.

-----

### **Technical & DevOps Architecture**

This project was developed with a focus on showcasing DevOps skills. Below are the core technologies and methodologies used.

#### **Backend**

- **Flask:** A lightweight and flexible web framework in Python.
- **Flask-SQLAlchemy:** Used for database communication, based on the **ORM (Object-Relational Mapping)** technique.
- **Flask-Login:** For managing user sessions and authentication.
- **Database:** **PostgreSQL** — a reliable, scalable database, running as a separate service.

#### **Infrastructure & DevOps**

- **Containerization (Docker):** The application and the database run in isolated containers. This ensures a consistent development and production environment.
- **Orchestration (Docker Compose):** Used to define and run the entire infrastructure (app + database) with a single command.
- **Testing:** (Optional: If you implement this stage) Describe how you implemented unit tests (e.g., using `pytest`) to verify the correct functionality of key features.
- **CI/CD (GitHub Actions):** (Optional: If you implement this stage) Explain how you automated the testing and deployment of code.

-----

### **How to Run the Project Locally**

#### **Prerequisites**

- **Docker Desktop** installed.

#### **Instructions**

1. Clone the repository: `git clone https://github.com/Kacper-Slezak/MathDeck.git`
2. Navigate to the project directory: `cd MathDeck`
3. Create a `.env` file and add the environment variables, e.g., `DATABASE_URL=postgresql://user:password@db:5432/mydatabase` and `SECRET_KEY=your_random_key`.
4. Launch the application and database using Docker Compose: `docker-compose up --build -d`
5. Initialize the database (create tables): `docker-compose exec web flask init-db`
6. The application will be available at: `http://localhost:5000`

-----

### **Roadmap**

A brief list of ideas for future development:

- Generating more complex tasks (e.g., with graphs).
- A module for tracking student progress.
- An API for integration with other applications.
- Deployment to a free cloud hosting service (e.g., Heroku, AWS Free Tier).

-----

### **Author**

*Kacper*

- **GitHub:** [https://github.com/Kacper-Slezak](https://www.google.com/search?q=https://github.com/Kacper-Slezak)
