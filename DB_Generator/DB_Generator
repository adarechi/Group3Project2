import psycopg2
from psycopg2 import sql
import random
def get_start_id(cursor, schema_name, table_name):
    # Получение максимального значения id
    cursor.execute(sql.SQL("SELECT MAX(id) FROM {}.{}").format(sql.Identifier(schema_name), sql.Identifier(table_name)))
    max_id = cursor.fetchone()[0]
    # Если таблица пуста, начнем с id = 1
    if max_id is None:
        max_id = 0
    return max_id
def changes_fics(conn, table_name):
    conn.commit()
    print(f"Данные успешно вставлены в таблицу: {table_name}.")
def insert_into(schema_name, table_name, columns):
    count = len(list(columns.split(", ")))
    insert_query = sql.SQL(
        f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({', '.join(['%s'] * count)})")
    return insert_query
def person_generate(cursor, schema_name, table_name):
    id = get_start_id(cursor, schema_name, table_name)
    for i in range(1):
        id = id+1
        age = random.randint(18, 100)
        first_name = f'UserName_{i}_Group3'
        money = random.randint(100, 10000000000000000) #10 000 000 000 000 000
        second_name = f'UserSurname_{i}_Group3'
        sex = True if i % 2==0 else False
        house_id = None

        # SQL-запрос для вставки данных
        insert_query = insert_into(schema_name, table_name, "id, age, first_name, money, second_name, sex, house_id")

        # Выполнение запроса
        cursor.execute(insert_query, (id, age, first_name, money, second_name, sex, house_id))
def house_generate(cursor, schema_name, table_name):
    # house: id, floor_count, price
    id = get_start_id(cursor, schema_name, table_name)
    for i in range(1):
        id = id+1
        floor_count = random.randint(1, 10)
        price = random.randint(1000, 100000)

        # SQL-запрос для вставки данных
        insert_query = insert_into(schema_name, table_name, "id, floor_count, price")

        # Выполнение запроса
        cursor.execute(insert_query, (id, floor_count, price))

#def car_generate(cursor, schema_name, table_name, start_person_id): # person_id начинается с первого id генерации person
#def parking_place_generate(cursor, schema_name, table_name, start_house_id): # house_id начинается с первого id генерации house




# Параметры подключения к базе данных
connection_params = {
'dbname': 'pflb_trainingcenter',
'user': 'pflb-at',
'password': 'pflbSberAT41',
'host': '77.50.236.203',
'port': '4832'
}

# Подключение к базе данных
try:
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()

    # Схема и таблицы
    schema_name = 'public'

    table_person = 'person' # person: id, age, first_name, money, second_name, sex, house_id
    table_car = 'car' # car: id, mark, model, price, engine_type_id, person_id
    table_house = 'house' # house: id, floor_count, price
    table_parking_place = 'parking_place' # parking_place: id, is_covered, is_warm, places_count, house_id

    # Генерация данных

    # Генерация данных для таблицы "person": id, age, first_name, money, second_name, sex, house_id
    person_generate(cursor, schema_name, table_person)
    # Фиксация изменений в таблице person
    changes_fics(conn, table_person)

    # Генерация данных для таблицы "house": id, floor_count, price
    house_generate(cursor, table_house)
    # Фиксация изменений в таблице house
    changes_fics(conn, table_house)

except psycopg2.Error as e:
    print("Ошибка при работе с PostgreSQL:", e)

finally:
    # Закрытие курсора и соединения
    if cursor:
        cursor.close()
    if conn:
        conn.close()
