import sqlite3

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(Word, picture):
    try:
        sqlite_connection = sqlite3.connect('words.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO allwords
                                  (Word, picture) VALUES (?, ?)"""
        word_pic = convert_to_binary_data(picture)

        # Преобразование данных в формат кортежа
        data_tuple = (Word, word_pic)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблиу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


insert_blob("Sunflower", "pngtree-sunflower-landscape-yellow-flower-flower-png-image_3347616.png")