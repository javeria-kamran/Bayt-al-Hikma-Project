from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# SQLite database
DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()  # Create a session object

Base = declarative_base()

# Book model
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    added_on = Column(Date, default=date.today)
    read = Column(Boolean, default=False)

# Drop the table if it exists and recreate it
Base.metadata.drop_all(engine)  # Drop all tables
Base.metadata.create_all(engine)  # Recreate tables

# Function to seed the database with sample books
def seed_database():
    sample_books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "read": True},
        {"title": "1984", "author": "George Orwell", "genre": "Sci-Fi", "read": False},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "read": False},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction", "read": True},
    ]
    for book_data in sample_books:
        book = Book(**book_data)
        session.add(book)
    session.commit()

# Seed the database with sample books
seed_database()

# CRUD functions
def add_book(title, author, genre, read=False):
    book = Book(title=title, author=author, genre=genre, read=read)
    session.add(book)
    session.commit()

def get_all_books():
    return session.query(Book).all()

def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()

# Export the session object
def get_session():
    return session