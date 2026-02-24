from main import BooksCollector

import pytest

book = ['Оно']
genre = ['Детектив']
book_genre = [('Оно', 'Детективы')]
books_allow_border = ['А', 'Аа', 'Тайна старого замка на холме у реки тут', 'Тайна старого замка на холме у реки тутъ']
books_not_allow_border = ['', 'Тайна старого замка на холме у реки тутъъ', 'Когда на небе полная луна, в лесу можно услышать в']

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Четыре лапы')
        collector.add_new_book('Хвост')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('border', books_not_allow_border)
    def test_add_new_book_chek_not_allowed_borders(self, collector, border):

        collector.add_new_book(border)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('border', books_allow_border)
    def test_add_new_book_check_books_allow_borders(self, collector, border):

        collector.add_new_book(border)
        assert border in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', book_genre)
    def test_set_book_genre_set_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_book_genre(name)) != 0

    @pytest.mark.parametrize('name, genre', [('Оно', 'Медицина')])
    def test_set_book_genre_set_not_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_book_genre(name)) == 0


    @pytest.mark.parametrize('name, genre', book_genre)
    def test_get_books_with_specific_genre_get_exist_genre(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('book', book)
    def test_get_books_for_children_get_allowed_genre(self, collector, book):

        collector.add_new_book(book)
        collector.set_book_genre(book, 'Фантастика')

        assert book in collector.get_books_for_children()
    
    @pytest.mark.parametrize('book', book)
    def test_get_books_for_children_get_banned_genre(self, collector, book):

        collector.add_new_book(book)
        collector.set_book_genre(book, 'Ужасы')
        

        assert len(collector.get_books_for_children()) == 0

    @pytest.mark.parametrize('book', book)
    def test_add_book_in_favorites_book_added(self, collector, book):

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book', book)
    def test_add_book_in_favorites_book_copy_not_added(self, collector, book):

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('book', book)
    def test_delete_book_from_favorites_book_deleted(self, collector, book):

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()
