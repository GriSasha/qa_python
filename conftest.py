import pytest

from main import BooksCollector

@pytest.fixture
def book():
    book = ['Муму', 'Вий']
    return book

@pytest.fixture
def child_books():
    child_books = ['Коты воители', 'Кот']
    return child_books

@pytest.fixture
def adult_books():
    adult_books = ['Шерлок', 'Вий']
    return adult_books
