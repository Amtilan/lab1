import psycopg2
from config import load_config


def collecting_info(check):
        
        """ Извлекать данные из таблицы поставщиков """
        config = load_config()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT user_id,name,phone_number FROM phonebook ORDER BY user_id")
                    rows = cur.fetchall()
                    print("The number of parts : ",cur.rowcount)
                    for row in rows:
                        if check == "1":
                            print(row[0])
                        elif check == "2":
                            print(row[1])
                        elif check == "3":
                            print(row[2])
                        else:
                            print(row)
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)


def update_info(user_id, name, phone_number):
    """ Обновление контакта """

    update_row_count = 0
    
    sql = """UPDATE phonebook
             SET name = %s, phone_number = %s
             WHERE user_id = %s"""
    
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение SQL-запроса UPDATE
                cur.execute(sql, (name, phone_number, user_id))
                update_row_count = cur.rowcount

            # Подтверждение изменений в базе данных
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return update_row_count 


def delete_info(user_id):
    """ Удаление контакта """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
               
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount
            
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


def insert_contact(name, phone_number):
    flag = True
    """ Вставка нового контакта в таблицу phonebook или обновление номера телефона, если контакт уже существует """
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем, существует ли контакт с таким именем
                cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
                count = cur.fetchone()[0]

                if count > 0:
                    # Если контакт существует, обновляем его номер телефона
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                else:
                    # Если контакт не существует, вставляем новый контакт
                    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))

                # Подтверждение изменений в базе данных
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        flag = False
        print(error)
    return flag

def insert_contact_by_list(data_list):
    flag = True
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for item in data_list:
                    id = item[0]
                    name = item[1]
                    phone_number = item[2]

                    # Проверка формата имени
                    if not isinstance(name, str):
                        print(f"Ошибка: Некорректный формат имени для контакта с ID '{id}': {name}")
                        flag = False
                        return flag

                    # Проверка формата номера телефона
                    try:
                        int(phone_number)
                    except ValueError:
                        print(f"Ошибка: Некорректный формат номера телефона для контакта '{name}': {phone_number}")
                        flag = False
                        return flag

                    cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
                    count = cur.fetchone()[0]

                    if count > 0:
                        # Если контакт существует, обновляем его номер телефона
                        cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                    else:
                        # Если контакт не существует, вставляем новый контакт
                        cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))

                # Подтверждение изменений в базе данных
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        flag = False
        print(error)
    return flag


def collecting_info_by_limit(limit):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT user_id, name, phone_number FROM phonebook ORDER BY user_id LIMIT {limit}")
                rows = cur.fetchall()
                print("The number of rows: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def collecting_info_by_offset(offset):

        config = load_config()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT user_id,name,phone_number FROM phonebook ORDER BY user_id OFFSET {offset}")
                    rows = cur.fetchall()
                    print("The number of parts : ",cur.rowcount)
                    for row in rows:
                        print(row)
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)


def delete_info_by_name(name):
    """ Удаление контакта по имени  """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE name = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                cur.execute(sql, (name,))
                rows_deleted = cur.rowcount
            
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


def delete_info_by_number(number):
    """ Удаление контакта по имени  """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE phone_number = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                cur.execute(sql, (phone_number,))
                rows_deleted = cur.rowcount
            
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


if __name__ == '__main__':
    list = [[18,"name2",4444]]
    operation = input("Выберите\n1 - записать контакт\n2 - обновить контакт\n3 - пройтись по всем контактам\n4 - удаление контакта\n5 - Записать несколько контактов : ")
    if operation == "1":
        name = input("Введите имя нового контакта : ")
        phone_number = int(input("Введите номер телефон : "))
        user_id = insert_contact(name,phone_number)  
        if user_id :
            print("Контакт успешно добавлен. ID:")
        else:
            print("Ошибка при добавлении контакта.")
    
    elif operation == "2":
        user_id = input("Введите айди контакта которого хотите обновить : ")
        name = input("Введите новое имя для контакта : ")
        phone_number = int(input("Введите новый номер телефон : "))
        updt = update_info(user_id,name,phone_number)
        if updt is not None:
            print("Контакт успешно изменен")
        else:
            print("Ошибка при изменений")

    elif operation == "3":
        pattern = input("Введите паттерн\n1 - Id :\n2 - Имя :\n3 - номер телефона : ")
        if pattern == "1" or pattern == "2" or pattern == "3":
            clt = collecting_info(pattern)
        else:     
            limit_or_offset = input("Хотите ли лимит или оффсет на запрос 1 - Да,2 - Нет : ")
            if limit_or_offset == "1":
                limit = int(input("Введите лимит : "))
                offset = int(input("Введите оффсет : "))

                if limit != 0:
                    lmt = collecting_info_by_limit(limit)
                if offset != 0:
                    ofst = collecting_info_by_offset(offset)
                
            else:
                clct = collecting_info(pattern)

    elif operation == "4":
        prtn = input("Введите паттерн для удаление контакта 1 - ID\n2 - Имя\n3 - Номер телефона : ")
        if prtn == "1":
            user_id = int(input("Введите айди контакта которого хотите удалить : "))
            dlt = delete_info(user_id)
            if dlt is not None:
                print("Контакт успешно удален")
            else:
                print("Ошибка при удалений")        
        elif prtn == "2":
            name = input("Введите имя контакта : ")
            dlt_2 = delete_info_by_name(name)
            if dlt_2 is not None:
                print("Контакт успешно удален")
            else:
                print("Ошибка при удалений")  
        elif prtn == "3":
            number = int(input("Введите номер телефона : "))
            dlt_3 = delete_info_by_number(number)
            if dlt_3 is not None:
                print("Контакт успешно удален")
            else:
                print("Ошибка при удалений")  
    
    elif operation == "5":
        insert_many_users = insert_contact_by_list(list)
        if insert_many_users:
            print("Контакты успешно добавлены")
        else:
            print("Ошибка")
