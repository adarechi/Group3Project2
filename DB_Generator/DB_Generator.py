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
    house_id = get_start_id(cursor, schema_name, table_house) - 5000
    for i in range(10000):
        id = id+1
        age = random.randint(18, 100)
        first_name = f'User_{i}_Group3'
        money = random.randint(100, 10000000000000000) #10 000 000 000 000 000
        second_name = f'UserSurname_{i}_Group3'
        sex = True if i % 2==0 else False
        if i <= 3000:
            house_id = house_id + 1
            # SQL-запрос для вставки данных
            insert_query = insert_into(schema_name, table_name,"id, age, first_name, money, second_name, sex, house_id")
            # Выполнение запроса
            cursor.execute(insert_query, (id, age, first_name, money, second_name, sex, house_id))
        else:
            # SQL-запрос для вставки данных
            insert_query = insert_into(schema_name, table_name,"id, age, first_name, money, second_name, sex, house_id")
            # Выполнение запроса
            cursor.execute(insert_query, (id, age, first_name, money, second_name, sex, None))

def house_generate(cursor, schema_name, table_name):
    # house: id, floor_count, price
    id = get_start_id(cursor, schema_name, table_name)
    for i in range(5000):
        id = id+1
        floor_count = random.randint(1, 10)
        price = random.randint(1000, 100000)

        # SQL-запрос для вставки данных
        insert_query = insert_into(schema_name, table_name, "id, floor_count, price")

        # Выполнение запроса
        cursor.execute(insert_query, (id, floor_count, price))

def car_generate(cursor, schema_name, table_name, table_person): # person_id начинается с первого id генерации person
    # car: id, mark, model, price, engine_type_id, person_id
    id = get_start_id(cursor, schema_name, table_name)
    person_id = get_start_id(cursor, schema_name, table_person) - 10000
    for i in range(5000):
        id = id + 1
        mark = f'Сar_{i}_Group3'
        model = f'Model_{i}_Group3'
        price = random.randint(100000, 3000000)
        engine_type_id = random.randint(1, 6)
        if i <= 4000:
            person_id = person_id + 1
            # SQL-запрос для вставки данных
            insert_query = insert_into(schema_name, table_name, "id, mark, model, price, engine_type_id, person_id")
            # Выполнение запроса
            cursor.execute(insert_query, (id, mark, model, price, engine_type_id, person_id))
        else:
            # SQL-запрос для вставки данных
            insert_query = insert_into(schema_name, table_name, "id, mark, model, price, engine_type_id, person_id")
            # Выполнение запроса
            cursor.execute(insert_query, (id, mark, model, price, engine_type_id, None))

def parking_place_generate(cursor, schema_name, table_name, table_house): # house_id начинается с первого id генерации house
    # parking_place: id, is_covered, is_warm, places_count, house_id
    id = get_start_id(cursor, schema_name, table_name)
    start_house_id = get_start_id(cursor, schema_name, table_house) - 5000
    lst_house_id = [start_house_id + i for i in range(1000)]
    for house in lst_house_id:
        for i in range(4):
            id = id + 1
            if i == 0:
                is_warm = True
                is_covered = True
                places_count = 1
            elif i == 1:
                is_warm = True
                is_covered = False
                places_count = 1
            elif i == 2:
                is_warm = False
                is_covered = True
                places_count = 1
            else:
                is_warm = False
                is_covered = False
                places_count = 2
            house_id = house

            # SQL-запрос для вставки данных
            insert_query = insert_into(schema_name, table_name, "id, is_covered, is_warm, places_count, house_id")

            # Выполнение запроса
            cursor.execute(insert_query, (id, is_covered, is_warm, places_count, house_id))


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
    '''
    # Генерация данных для таблицы "house": id, floor_count, price
    house_generate(cursor, schema_name, table_house)
    # Фиксация изменений в таблице house
    changes_fics(conn, table_house)
    
    # Генерация данных для таблицы "person": id, age, first_name, money, second_name, sex, house_id
    person_generate(cursor, schema_name, table_person)
    # Фиксация изменений в таблице person
    changes_fics(conn, table_person)
    
    # Генерация данных для таблицы "car": id, mark, model, price, engine_type_id, person_id
    car_generate(cursor, schema_name, table_car, table_person)
    # Фиксация изменений в таблице car
    changes_fics(conn, table_car)
    '''
    
    # Генерация данных для таблицы "parking_place": id, is_covered, is_warm, places_count, house_id
    parking_place_generate(cursor, schema_name, table_parking_place, table_house)
    # Фиксация изменений в таблице parking_place
    changes_fics(conn, table_parking_place)


except psycopg2.Error as e:
    print("Ошибка при работе с PostgreSQL:", e)

finally:
    # Закрытие курсора и соединения
    if cursor:
        cursor.close()
    if conn:
        conn.close()
