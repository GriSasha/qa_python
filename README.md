# qa_python

Было покрыто тестами приложение BookCollector. Покрытие составило более 90%.

Удалось реализовать 6 тестов с положительными и 4 с негативными сценариями. Все тесты прошли успешно.

Тест test_add_new_book_add_two_books добавляет в список две книги и проверяет, что добавилось именно две.

Тест test_add_new_book_add_book_with_fifty_symbols проверяет, что в список не было добавлено книги, длина которой составляет 50 символов.

Тест test_set_book_genre_set_exist_genre присваивает имеющейся в списке книге существующий в условиях жанр.

Тест test_set_book_genre_set_not_exist_genre проверяет, что имеющейся в списке книге не присваивается несуществующий в условиях жанр.

Тест test_get_books_with_specific_genre_get_exist_genre проверяет, что выводится книга с определенным жанром.

Тест test_get_books_for_children_get_allowed_genre проверяет, что в список книг для детей добавляются книги с разрешенным жанром.

Тест test_get_books_for_children_get_banned_genre проверяет, что в список книг для детей не добавляются книги с запрещенным жанром.

Тест test_add_book_in_favorites_book_added проверяет, что книги добавляются в Избранное.

Тест test_add_book_in_favorites_book_copy_not_added проверяет, что одна и та же книга не добавляется в Избранное.

Тест test_delete_book_from_favorites_book_deleted проверяет, что книга удаляется из Изюранного.