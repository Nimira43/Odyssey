from fastapi import FastAPI, HTTPException

app = FastAPI()

BOOKS = [
    {'title': 'The Lord of the Rings', 'author': 'JRR Tolkien', 'category': 'Fantasy'},
    {'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'category': 'Dystopian'},
    {'title': 'The Lion, the Witch and the Wardrobe', 'author': 'CS Lewis', 'category': 'Fantasy'},
    {'title': 'Dune', 'author': 'Frank Herbert', 'category': 'Science Fiction'},
    {'title': 'The Hobbit', 'author': 'JRR Tolkien', 'category': 'Fantasy'},
    {'title': 'War and Peace', 'author': 'Leo Tolstoy', 'category': 'Historical'},
    {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'category': 'Gothic'},
    {'title': 'The Odyssey', 'author': 'Homer', 'category': 'Epic'},
    {'title': '2001: A Space Odyssey', 'author': 'Arthur C. Clarke', 'category': 'Science Fiction'},
]

@app.get('/books')
async def read_all_books():
  return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
  for book in BOOKS:
    if book.get('title').casefold() == book_title.casefold():
      return book
  raise HTTPException(status_code=404, detail="Book not found")