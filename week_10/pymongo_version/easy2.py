from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv('MONGO_URI'))
db = client['phonebook_db']
collection = db['entries']

def find_by_pattern(pattern):
    regex_pattern = {'$regex': pattern, '$options': 'i'} 
    results = collection.find({
        '$or': [
            {'first_name': regex_pattern},
            {'last_name': regex_pattern},
            {'phone': regex_pattern}
        ]
    })
    return list(results)

def upsert_user(first_name, last_name, phone):
    result = collection.update_one(
        {'first_name': first_name, 'last_name': last_name},
        {'$set': {'phone': phone}},
        upsert=True
    )
    return result

def validate_phone(phone):
    return phone.isdigit() and 10 <= len(phone) <= 13

def query_with_pagination(limit, offset):
    return list(collection.find().skip(offset).limit(limit))

def delete_by_username_or_phone(identifier):
    query = {'$or': [{'first_name': identifier}, {'phone': identifier}]}
    result = collection.delete_one(query)
    return result

def insert_from_console():
    first_name = input("Как вас зовут? ")
    last_name = input("А ваша фамилия? ")
    phone = input("Номерок? ")
    if validate_phone(phone):
        document = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
        collection.insert_one(document)
        print("Я вас успешно записал в свою бд.")
    else:
        print("А номерок не правильный-то")

def interactive_menu():
    while True:
        print("""
PhoneBook Operations:
1. Добавить запись из консоли
2. Обновить запись
3. Поиск по шаблону
4. Запрос с пагинацией
5. Удалить запись
6. Выход
""")
        choice = input("Выберите операцию:")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            first_name = input("Напиши имя чтобы обновить: ")
            last_name = input("Напиши фамилию чтобы обновить: ")
            phone = input("Теперь номер напиши: ")
            upsert_user(first_name, last_name, phone)
            print("Вы успешно обновили данные")
        elif choice == '3':
            pattern = input("Введите паттерн поиска: ")
            results = find_by_pattern(pattern)
            print("Все результаты:", results)
        elif choice == '4':
            limit = int(input("Введите лимит: "))
            offset = int(input("Введите страницу: "))
            results = query_with_pagination(limit, offset)
            print("Пагинейшн:", results)
        elif choice == '5':
            identifier = input("Напиши номер или имя чтобы удалить с базы даннных: ")
            delete_by_username_or_phone(identifier)
            print("Человек был удалён.")
        elif choice == '6':
            print("ПОКА...")
            break
        else:
            print("Список для чего?")

if __name__ == "__main__":
    interactive_menu()