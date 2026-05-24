from dbfread import DBF
import pandas as pd

try:
    # Попытка загрузить файл genres.dbf
    dbf = DBF('genres.dbf')
    genres = [record for record in dbf]
    genres_df = pd.DataFrame(genres)
    print("Данные из genres.dbf успешно загружены:")
except FileNotFoundError:
    # Если файл не найден, создаем пример DataFrame
    print("Файл genres.dbf не найден. Используем пример данных.")
    genres_df = pd.DataFrame({
        'GenreID': [1, 2, 3],
        'GenreName': ['Фантастика', 'Драма', 'Комедия']
    })

# Выводим DataFrame
print("\nDataFrame genres:")
print(genres_df)
