import unittest
from unittest.mock import Mock

from ..book_service.book import BookService, BookRepository, Book


class BookServiceTest(unittest.TestCase):

    def setUp(self):
        self.bookRepository = Mock(BookRepository)
        self.bookService = BookService(self.bookRepository)

    def test_find_book_by_id(self):
        id_book = 1
        book = Book(id_book, "Title", "Author")
        self.bookRepository.find_by_id.return_value = book
        result = self.bookService.find_by_id(id_book)
        self.bookRepository.find_by_id.assert_called_once_with(id_book)
        self.assertEqual(book, result)

    def test_find_all_books(self):
        books = [
            Book(1, "Title1", "Author1"),
            Book(2, "Title2", "Author2")
        ]
        self.bookRepository.find_all.return_value = books
        result = self.bookService.find_all()
        self.bookRepository.find_all.assert_called_once()
        self.assertEqual(books, result)


if __name__ == '__main__':
    unittest.main()