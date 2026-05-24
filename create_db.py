import sqlite3

# Создаем соединение с базой данных SQLite
conn = sqlite3.connect('StudentLibrary.db')

# Создаем курсор
c = conn.cursor()

# Создаем таблицу Genres
c.execute('''
CREATE TABLE IF NOT EXISTS Genres (
    GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
    GenreName TEXT NOT NULL
);
''')

# Создаем таблицу Students
c.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName TEXT,
    FirstName TEXT,
    MiddleName TEXT,
    Faculty TEXT,
    Course INTEGER
);
''')

# Создаем таблицу Books
c.execute('''
CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Author TEXT,
    Year INTEGER,
    GenreID INTEGER,
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);
''')

# Вставляем примерные данные в таблицу Genres
genres = [
    ('Фантастика',),
    ('Драма',),
    ('Комедия',)
]
c.executemany('INSERT INTO Genres (GenreName) VALUES (?)', genres)

# Вставляем примерные данные в таблицу Students
students = [
    ('Иванов', 'Иван', 'Иванович', 'Факультет ИТ', 2),
    ('Петров', 'Петр', 'Петрович', 'Факультет Механики', 3)
]
c.executemany('''
INSERT INTO Students (LastName, FirstName, MiddleName, Faculty, Course)
VALUES (?, ?, ?, ?, ?)
''', students)

# Вставляем примерные данные в таблицу Books
books = [
    ('Гарри Поттер', 'Дж.К.Роулинг', 1997, 1),
    ('Война и Мир', 'Лев Толстой', 1869, 2),
    ('Автостопом по галактике', 'Дуглас Адамс', 1979, 1)
]
c.executemany('''
INSERT INTO Books (Title, Author, Year, GenreID)
VALUES (?, ?, ?, ?)
''', books)

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("База данных StudentLibrary.db успешно создана и заполнена примерными данными.")
