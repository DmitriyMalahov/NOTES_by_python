import json
import datetime

def load_notes(): # функция чтения из файла
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

notes = load_notes()

def save_notes(notes): # функция сохранения/создания файла
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def print_notes(): # функция показа всех заметок
    notes = load_notes()
    if len(notes) == 0:
        print("У вас нет заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст заметки: {note['message']}")
            print(f"Дата/Время: {note['timestamp']}")
            print()

# def delete_note():

# def edit_note():

def add_note(): # Функция добавления/создания новой заметки в файл.
    heading = input("Введите заголовок заметки: ")
    message = input("Ввделите текс заметки: ")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'heading': heading,
        'message': message,
        'time': time
    }
    notes.append(note)
    save_notes(notes)
    print("Новая заметка создана")

# def filter_notes():


while True:
    print("Доступные команды для ввода:")
    print("add - добавить новую заметку")
    print("edit - изменить существующую заметку")
    print("delete - удалить существующую заметку")
    print("filter - отфильтровать заметки по дате")
    print("print - показать все существующие заметки")
    print("exit - выход из программы")
    command = input("Введите команду: ")
   
    if command == "add":
        add_note()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "filter":
        filter_notes()
    elif command == "print":
        print_notes()
    elif command == "exit":
        break
    else:
        print("Введена некорректная команда")