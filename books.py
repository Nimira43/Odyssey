from fastapi import FastAPI

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

@app.get('/api-endpoint')
async def first_api():
  return BOOKS