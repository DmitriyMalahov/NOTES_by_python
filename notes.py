import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

notes = load_notes()

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


# def print_notes():

# def delete_note():

# def edit_note():

# def add_note():

# def filter_notes():


while True:
    print("Доступные команды для ввода:")
    print("add - добавить новую заметку")
    print("edit - изменить существующую заметку")
    print("delete - удалить существующую заметку")
    print("filter - отфильтровать заметки по дате")
    print("print - показать все существующие заметки")
    print("exit - выйте изпрограммы")
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