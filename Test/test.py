import unittest
from Library.book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        b = Book("Grokking Algorithms", "SAURABH", "19901")
        self.assertEqual(b.title, "Grokking Algorithms")
        self.assertEqual(b.status, "available")

    def test_issue_return(self):
        b = Book("Test Book", "Author", "999")

        self.assertTrue(b.issue())

        self.assertEqual(b.status, "issued")
        self.assertFalse(b.issue())

        b.return_book()
        self.assertEqual(b.status, "available")

if __name__ == '__main__':
    unittest.main()