from app import app, db

# Ensure that the app context is created before creating the database
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
