from pymongo import MongoClient
import os 
from dotenv import load_dotenv
load_dotenv()
client = MongoClient(os.getenv('MONGO_URI'))
db = client['phonebook_db']
collection = db['entries']


def insert_from_console():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    collection.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    })

def update_data():
    identifier = input("Введите имя или номер телефона для обновления: ")
    key_to_update = "first_name" if not identifier.isdigit() else "phone"
    new_value = input(f"Введите новое значение для {key_to_update}: ")
    collection.update_one({key_to_update: identifier}, {"$set": {key_to_update: new_value}})

def query_data():
    key = input("Введите ключ для поиска (first_name, last_name, phone): ")
    value = input("Введите значение для поиска: ")
    results = collection.find({key: value})
    for result in results:
        print(result)

def delete_data():
    identifier = input("Введите имя или номер телефона для удаления: ")
    key_to_delete = "first_name" if not identifier.isdigit() else "phone"
    collection.delete_one({key_to_delete: identifier})

def main():
    while True:
        print("\nВсе возможные операции:")
        print("1. Добавить данные с консоли")
        print("2. Обновить данные")
        print("3. Фильтрация")
        print("4. Удаление")
        print("5. Выход")
        choice = input("Выбери какую нибудь из них: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            update_data()
        elif choice == '3':
            query_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Пока пока...")
            break
        else:
            print("ЭМ.")

if __name__ == '__main__':
    main()