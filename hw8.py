import sqlite3

def display_cities():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")
    return cities

def display_students_by_city(city_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    query = """
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()

    if students:
        for student in students:
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город проживания: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет студентов в данном городе.")
    conn.close()

def main():
    while True:
        cities = display_cities()
        try:
            city_id = int(input("Введите id города: "))
            if city_id == 0:
                print("Выход из программы.")
                break
            city_ids = [city[0] for city in cities]
            if city_id in city_ids:
                display_students_by_city(city_id)
            else:
                print("Неверный id города. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

if __name__ == "__main__":
    main()

# CREATE TABLE countries (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL
# );
#
# INSERT INTO countries (title) VALUES ('Кыргызстан');
# INSERT INTO countries (title) VALUES ('Германия');
# INSERT INTO countries (title) VALUES ('Китай');
#
# CREATE TABLE cities  (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     area REAL DEFAULT 0,
#     country_id INTEGER,
#     FOREIGN KEY (country_id) REFERENCES countries (id)
# );
#
# INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 127, 1);
# INSERT INTO cities (title, area, country_id) VALUES ('Ош', 182, 1);
# INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 891.8, 2);
# INSERT INTO cities (title, area, country_id) VALUES ('Мюнхен', 310.7, 2);
# INSERT INTO cities (title, area, country_id) VALUES ('Гуанчжоу', 7434.4, 3);
# INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 16410.5, 3);
# INSERT INTO cities (title, area, country_id) VALUES ('Шанхай', 6340.5, 3);
#
# CREATE TABLE students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     city_id INTEGER,
#     FOREIGN KEY (city_id) REFERENCES cities (id)
# );
#
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Алина', 'Ким', 1);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Ерлан', 'Мусаев', 2);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Лена', 'Штайн', 3);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Макс', 'Хофманн', 4);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Чжан', 'Вэй', 5);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Ли', 'Ху', 6);
# INSERT INTO students (first_name, last_name, city_id) VALUES ('Хуан', 'Мин', 7);