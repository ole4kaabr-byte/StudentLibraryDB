from dbfread import DBF
import pandas as pd

# Импортируем данные из файла genres.dbf
try:
    dbf = DBF('genres.dbf')
    genres = [record for record in dbf]
    genres_df = pd.DataFrame(genres)
    print("Данные из genres.dbf успешно загружены:")
    print(genres_df)
except FileNotFoundError:
    print("Файл genres.dbf не найден. Создаем пример DataFrame.")

    # Пример исправленного DataFrame, если файла нет
    genres_df = pd.DataFrame({
        'GenreID': [1, 2, 3],
        'GenreName': ['Фантастика', 'Драма', 'Комедия']
    })

# Выводим пример DataFrame
print("\nПример DataFrame genres:")
print(genres_df)

# Создаем дополнительные DataFrame для примера
movies = pd.DataFrame({
    'MovieID': [101, 102, 103],
    'Title': ['Фильм 1', 'Фильм 2', 'Фильм 3'],
    'GenreID': [1, 2, 3]
})

# Можно объединить таблицы или выполнить другие операции
movies_with_genres = pd.merge(movies, genres_df, on='GenreID', how='left')

print("\nТаблица фильмов с жанрами:")
print(movies_with_genres)
