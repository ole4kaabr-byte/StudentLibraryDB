import pandas as pd
from simpledbf import Dbf5

# Ваши DataFrame
genres = pd.DataFrame({
    'GenreID': [1, 2, 3, 4, 5],
    'GenreName': ['Фантастика', 'Детектив', 'Учебная литература', 'Роман', 'Наука']
})

students = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'LastName': ['Иванов', 'Петрова', 'Сидоров', 'Кузнецова', 'Морозов'],
    'FirstName': ['Петр', 'Анна', 'Алексей', 'Мария', 'Дмитрий'],
    'MiddleName': ['Александрович', 'Борисовна', 'Викторович', 'Игоревна', 'Павлович'],
    'Faculty': ['Факультет информатики', 'Факультет математики', 'Факультет физики', 'Факультет ...'],
    'Course': [3, 2, 4, 1, 3]
})

books = pd.DataFrame({
    'BookID': [1, 2, 3, 4, 5],
    'Title': ['Властелин колец', 'Шерлок Холмс', 'Основы программирования', 'Мастер и Маргарита', 'Граф Монте-Кристо'],
    'Author': ['Дж. Р. Р. Толкин', 'Агата Кристи', 'Иванов И.И.', 'Михаил Булгаков', 'Александр Дюма'],
    'Year': [1954, 1892, 2020, 1967, 2010],
    'GenreID': [1, 2, 3, 4, 5]
})

# Функция для сохранения DataFrame в .dbf файл с обработкой кодировки
def save_df_to_dbf(df, filename):
    temp_csv = filename.replace('.dbf', '_temp.csv')
    # Сохраняем DataFrame в CSV
    df.to_csv(temp_csv, index=False, encoding='utf-8')

    # Обработка CSV файла для устранения ошибок кодировки
    with open(temp_csv, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()

    # Перезаписываем файл с исправленным содержимым
    with open(temp_csv, 'w', encoding='utf-8') as f:
        f.write(data)

    # Создаем Dbf5 из исправленного CSV
    dbf = Dbf5(temp_csv)
    dbf.to_dbf(filename)

# Используйте функцию для каждого DataFrame
save_df_to_dbf(genres, 'genres.dbf')
save_df_to_dbf(students, 'students.dbf')
save_df_to_dbf(books, 'books.dbf')
