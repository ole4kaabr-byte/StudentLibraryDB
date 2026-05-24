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
    'Faculty': ['Факультет информатики', 'Факультет математики', 'Факультет физики', 'Факультет биологии', 'Факультет химии'],
    'Course': [3, 2, 4, 1, 3]
})

books = pd.DataFrame({
    'BookID': [1, 2, 3, 4, 5],
    'Title': ['Властелин колец', 'Шерлок Холмс', 'Основы программирования', 'Мастер и Маргарита', 'Краткая история науки'],
    'Author': ['Дж. Р. Р. Толкин', 'Агата Кристи', 'Иванов И.И.', 'Михаил Булгаков', 'Леонард Эйлер'],
    'Year': [1954, 1892, 2020, 1967, 2010],
    'GenreID': [1, 2, 3, 4, 5]
})

# Функция для сохранения DataFrame в .dbf файл
def save_df_to_dbf(df, filename):
    # Создаем временный CSV файл
    temp_csv = filename.replace('.dbf', '.csv')
    df.to_csv(temp_csv, index=False)
    # Загружаем CSV в Dbf5
    dbf = Dbf5(temp_csv)
    # Сохраняем как .dbf
    dbf.to_dbf(filename)

# Сохраняем файлы
save_df_to_dbf(genres, 'genres.dbf')
save_df_to_dbf(students, 'students.dbf')
save_df_to_dbf(books, 'books.dbf')
