Live Demo: Expense Tracker
https://smartspend-sx51.onrender.com/

Tech Stack:
• Backend: Python (Flask)
• Database: PostgreSQL
• Validation: Pydantic
• Deployment: Render (CI/CD Pipeline)
• ORM: Flask-SQLAlchemy
• Version Control: Git/GitHub

Key Features:
• Dynamic Data Modeling: Implemented a relational database schema allowing for user-defined categories with associated real-time expense tracking.
• One-to-Many Relationships: Engineered the backend to support complex data associations, where each unique category dynamically aggregates its nested expense entries.
• User Authentication: Secure signup/login with Pydantic data validation and encrypted password storage.
• Expense Management: Create, read, update, and delete (CRUD) financial transactions.
• Data Integrity: Robust backend validation ensures every expense has a valid amount, date, and category.
• Cloud Hosted: Fully deployed on Render with an automated CI/CD pipeline.

Architecture and DevOps
This project isn't just a site; it's a demonstration of modern development workflows:
• CI/CD Pipeline: Integrated GitHub-to-Render deployment. Every code push automatically triggers a new build and deployment.
• Database Management: Uses Flask-Migrate to handle schema changes without data loss.
• Environment Security: Sensitive credentials (API keys, DB URLs) are managed through server-side environment variables, never exposed in the source code.