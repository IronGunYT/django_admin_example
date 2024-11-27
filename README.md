# Django admin example

## Описание проекта

Этот проект представляет собой простое Django приложение с доступом только к административной панели. В проекте реализованы три модели: Author, Book, и Collection. Основная цель проекта — предоставить интерфейс для управления данными об авторах, книгах и их подборках с возможностью просмотра и редактирования в административной панели.

Проект задеплоен, за адресом обращаться к [@irongun](https://t.me/irongun)

### Модели:

1. Author: хранит информацию об авторах.
   - name (CharField): имя автора, максимум 100 символов.
   - biography (TextField): текстовая биография автора.
   - birth_date (DateField): дата рождения автора.
   - rating (DecimalField): рейтинг автора (до 4 знаков, из них 2 после запятой).
   
2. Book: хранит информацию о книгах.
   - title (CharField): название книги, максимум 200 символов.
   - description (TextField): описание книги.
   - publication_date (DateField): дата публикации книги.
   - pages (IntegerField): количество страниц.
   - price (DecimalField): стоимость книги (до 6 знаков, из них 2 после запятой).
   - author (ForeignKey): ссылка на автора книги, при удалении автора значение null.
   
3. Collection: представляет собой подборку книг.
   - title (CharField): название подборки, максимум 200 символов.
   - books (ManyToManyField): книги, входящие в подборку.

## Технологии

В проекте используются следующие технологии:

- Python - Основной язык программирования, на котором написано приложение.
- Django - Основной фреймворк для веб-разработки, административная панель использовалась в качестве основного интерфейса.
  - Django ORM - Для упрощения работы с базой данных использовалась встроенная в Django ORM система
- SQLite - Используется в качестве базы данных, запросы не писались благодаря ORM.

## Установка

Для установки и запуска проекта выполните следующие шаги:

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.10 и выше) и pip.

2. Склонируйте репозиторий проекта:
   ```shell
   git clone ...
   ```
3. Создайте и активируйте виртуальное окружение:
   ```shell
   python3 -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```
4. Установите зависимости:
   ```shell
   pip install -r requirements.txt
   ```
5. Выполните миграции базы данных:
   ```shell
   python manage.py migrate
   ```
6. Создайте суперпользователя для доступа к административной панели:
   ```shell
   python manage.py createsuperuser
   ```
7. Запустите сервер разработки:
   ```shell
   python manage.py runserver
   ```
8. Откройте в браузере http://localhost:8000/admin и войдите в административную панель с учётными данными суперпользователя.

## Деплой

Для деплоя проекта на продакшн сервере, следуйте стандартной процедуре для развертывания Django приложений с использованием Gunicorn и Nginx. Обязательно настройте переменные окружения и используйте современные практики безопасности (TLS, запароленные данные и т.д.).

## Схема базы данных

### Таблица Author

| Поле       | Тип данных   | Описание                      |
|------------|--------------|-------------------------------|
| id         | AutoField    | автоматический первичный ключ |
| name       | CharField    | имя автора                    |
| biography  | TextField    | биография автора              |
| birth_date | DateField    | дата рождения                 |
| rating     | DecimalField | рейтинг                       |

### Таблица Book

| Поле             | Тип данных   | Описание                                  |
|------------------|--------------|-------------------------------------------|
| id               | AutoField    | автоматический первичный ключ             |
| title            | CharField    | название                                  |
| description      | TextField    | описание                                  |
| publication_date | DateField    | дата публикации                           |
| pages            | IntegerField | количество страниц                        |
| price            | DecimalField | стоимость                                 |
| author_id        | ForeignKey   | ссылка на автора, связь "многие к одному" |

### Таблица Collection

| Поле  | Тип данных      | Описание                                             |
|-------|-----------------|------------------------------------------------------|
| id    | AutoField       | автоматический первичный ключ                        |
| title | CharField       | название                                             |
| books | ManyToManyField | книги, входящие в подборку, связь "многие ко многим" |

## Данные для базы данных

### Данные для модели Author

| ID  | Name               | Biography                                                                                  | Birth Date | Rating |
|-----|--------------------|--------------------------------------------------------------------------------------------|------------|--------|
| 1   | Leo Tolstoy        | A famous Russian author known for his epic novels like War and Peace and Anna Karenina.    | 1828-09-09 | 4.95   |
| 2   | Jane Austen        | English novelist known for romantic fiction, particularly Pride and Prejudice.             | 1775-12-16 | 4.80   |
| 3   | Mark Twain         | American writer acclaimed for his wit and humor. Author of Adventures of Huckleberry Finn. | 1835-11-30 | 4.75   |
| 4   | Arthur Conan Doyle | British writer best known for his detective stories featuring Sherlock Holmes.             | 1859-05-22 | 4.85   |
| 5   | J.K. Rowling       | British author best known for the Harry Potter series.                                     | 1965-07-31 | 4.90   |

### Данные для модели Book

| ID  | Title                                   | Description                                                                 | Publication Date | Pages | Price | Author ID |
|-----|-----------------------------------------|-----------------------------------------------------------------------------|------------------|-------|-------|-----------|
| 1   | War and Peace                           | An epic novel about the history of Russia during the Napoleonic era.        | 1869-01-01       | 1225  | 39.99 | 1         |
| 2   | Anna Karenina                           | A novel about love and betrayal among Russian aristocracy.                  | 1877-01-01       | 864   | 29.99 | 1         |
| 3   | Pride and Prejudice                     | A romantic novel that critiques the societal norms of 19th century England. | 1813-01-28       | 432   | 19.99 | 2         |
| 4   | Adventures of Huckleberry Finn          | A novel about a young boy's adventures on the Mississippi River.            | 1884-12-10       | 366   | 24.99 | 3         |
| 5   | The Adventures of Sherlock Holmes       | A collection of short stories featuring the detective Sherlock Holmes.      | 1892-10-14       | 307   | 27.99 | 4         |
| 6   | Harry Potter and the Sorcerer's Stone   | The first book in the Harry Potter series about a young wizard.             | 1997-06-26       | 309   | 34.99 | 5         |
| 7   | Harry Potter and the Chamber of Secrets | The second book in the Harry Potter series.                                 | 1998-07-02       | 341   | 34.99 | 5         |

### Данные для модели Collection
| ID  | Title              | Books   |
|-----|--------------------|---------|
| 1   | irongun collection | 6, 7    |
| 2   | alex collection    | 2, 4, 7 |

С проектом можно взаимодействовать через административную панель. Она предоставляет возможности для просмотра, изменения и поиска по данным всех трёх моделей.
