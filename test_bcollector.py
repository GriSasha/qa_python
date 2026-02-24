from main import BooksCollector

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector, book):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book(book[0])
        collector.add_new_book(book[1])

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_book_with_fifty_symbols(self, collector):

        collector.add_new_book('Когда на небе полная луна, в лесу можно услышать в')

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre', [['Шерлок', 'Детективы'], ['Оно', 'Ужасы']])
    def test_set_book_genre_set_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_book_genre(name)) != 0

    @pytest.mark.parametrize('name, genre', [['Шерлок', 'Медицина'], ['Оно', 'Клоуны']])
    def test_set_book_genre_set_not_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_book_genre(name)) == 0


    @pytest.mark.parametrize('name, genre', [['Шерлок', 'Детективы'], ['Оно', 'Ужасы']])
    def test_get_books_with_specific_genre_get_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_with_specific_genre(genre)

    def test_get_books_for_children_get_allowed_genre(self, collector, child_books):

        collector.add_new_book(child_books[0])
        collector.add_new_book(child_books[1])
        collector.set_book_genre(child_books[0], 'Фантастика')
        collector.set_book_genre(child_books[1], 'Комедии')

        assert collector.get_books_for_children() == child_books
    
    def test_get_books_for_children_get_banned_genre(self, collector, adult_books):

        collector.add_new_book(adult_books[0])
        collector.add_new_book(adult_books[1])
        collector.set_book_genre(adult_books[0], 'Ужасы')
        collector.set_book_genre(adult_books[1], 'Детективы')

        assert len(collector.get_books_for_children()) == 0


    def test_add_book_in_favorites_book_added(self, collector, book):

        collector.add_new_book(book[0])
        collector.add_new_book(book[1])
        collector.add_book_in_favorites(book[0])
        collector.add_book_in_favorites(book[1])

        assert book == collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Оно', 'Муму'])
    def test_add_book_in_favorites_book_copy_not_added(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('name', ['Оно', 'Муму', 'Шатура'])
    def test_delete_book_from_favorites_book_deleted(self, collector, name):

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.get_list_of_favorites_books()

    