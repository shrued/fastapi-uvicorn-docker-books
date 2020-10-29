from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Book(BaseModel):
  title: str
  author: str 

@app.get('/')
def index():
  return {'key' : 'value'}

@app.get('/books')
def get_books():
  return db

@app.get('/books/{book_id}')
def get_book(book_id: int):
  return db[book_id-1]

@app.post('/books')
def create_book(book: Book):
  db.append(book.dict())
  return db[-1]

@app.delete('/books/{book_id}')
def delete_book(book_id: int):
  db.pop(book_id-1)
  return {}