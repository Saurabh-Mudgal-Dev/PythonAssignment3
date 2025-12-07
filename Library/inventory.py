from pathlib import Path
import json
import logging
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:

    def __init__(self, filename="library.json"):
        self.file_path = Path(filename)
        self.books = []
        self._initialize()

    def _initialize(self):
        if self.file_path.is_file() is False:
            logging.info("No database found. Creating new inventory.")
            return

        try:
            raw = self.file_path.read_text()
            decoded = json.loads(raw)
            self.books = list(map(lambda x: Book(**x), decoded))
            logging.info("Database loaded successfully.")
        except json.JSONDecodeError:
            logging.error("Database file corrupted.")
            print("Error: Database file is corrupted.")
        except Exception as err:
            logging.error(f"Error loading database: {err}")

    def add_book(self, title, author, isbn):
        existing = next((b for b in self.books if b.isbn == isbn), None)

        if existing:
            logging.warning(f"Attempted to add duplicate ISBN: {isbn}")
            print("Error: A book with this ISBN already exists.")
            return

        obj = Book(title, author, isbn)
        self.books.append(obj)
        self.save_books()
        logging.info(f"Book added: {title} ({isbn})")
        print("Book added successfully.")

    def search_by_title(self, title):
         return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if len(self.books) == 0:
            print("No books in inventory.")
            return
        for entry in self.books:
            print(entry)

    def save_books(self):
        try:
            data = [book.to_dict() for book in self.books]
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as err:
            logging.error(f"Failed to save data: {err}")
            print("Error saving database.")