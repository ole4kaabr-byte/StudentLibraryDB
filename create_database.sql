-- Создание базы данных
CREATE DATABASE StudentLibrary;
USE StudentLibrary;

-- Создание таблицы Genres
CREATE TABLE Genres (
  GenreID INT AUTO_INCREMENT PRIMARY KEY,
  GenreName VARCHAR(50) NOT NULL
);

-- Создание таблицы Students
CREATE TABLE Students (
  StudentID INT AUTO_INCREMENT PRIMARY KEY,
  LastName VARCHAR(50),
  FirstName VARCHAR(50),
  MiddleName VARCHAR(50),
  Faculty VARCHAR(50),
  Course INT
);

-- Создание таблицы Books
CREATE TABLE Books (
  BookID INT AUTO_INCREMENT PRIMARY KEY,
  Title VARCHAR(100),
  Author VARCHAR(50),
  Year INT,
  GenreID INT,
  FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

-- Создание таблицы Issuance
CREATE TABLE Issuance (
  IssuanceID INT AUTO_INCREMENT PRIMARY KEY,
  StudentID INT,
  BookID INT,
  IssueDate DATE,
  ReturnDate DATE,
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

-- Создание таблицы Employees
CREATE TABLE Employees (
  EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
  LastName VARCHAR(50),
  FirstName VARCHAR(50),
  Position VARCHAR(50)
);

-- Вставка данных в таблицу Genres
INSERT INTO Genres (GenreName) VALUES
('Фантастика'),
('Детектив'),
('Учебная литература'),
('Роман'),
('Наука');

-- Вставка данных в таблицу Students
INSERT INTO Students (LastName, FirstName, MiddleName, Faculty, Course) VALUES
('Иванов', 'Петр', 'Александрович', 'Факультет информатики', 3),
('Петрова', 'Анна', 'Борисовна', 'Факультет математики', 2),
('Сидоров', 'Алексей', 'Викторович', 'Факультет физики', 4),
('Кузнецова', 'Мария', 'Игоревна', 'Факультет биологии', 1),
('Морозов', 'Дмитрий', 'Павлович', 'Факультет химии', 3);

-- Вставка данных в таблицу Books
INSERT INTO Books (Title, Author, Year, GenreID) VALUES
('Властелин колец', 'Дж. Р. Р. Толкин', 1954, 1),
('Шерлок Холмс', 'Агата Кристи', 1892, 2),
('Основы программирования', 'Иванов И.И.', 2020, 3),
('Мастер и Маргарита', 'Михаил Булгаков', 1967, 4),
('Краткая история науки', 'Леонард Эйлер', 2010, 5);

-- Примеры выборок и аналитических запросов:
...
