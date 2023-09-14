import json
import datetime

def save_note_to_file(title, msg):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'title': title,
        'message': msg,
        'date': date_str
    }
    with open('notes.json', 'a') as file:
        json.dump(note, file)
        file.write("\n")

def create_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    save_note_to_file(title, msg)
    print("Заметка успешно сохранена")

def read_notes():
    try:
        with open('notes.json', 'r') as file:
            for line in file:
                note = json.loads(line.strip())
                print(note['date'], note['title'])
    except FileNotFoundError:
        print("Заметок пока нет.")


def edit_note():
    read_notes()
    title_to_edit = input("Введите заголовок заметки, которую хотите редактировать: ")
    edited_notes = []
    edited = False
    with open('notes.json', 'r') as file:
        for line in file:
            note = json.loads(line.strip())
            if note['title'] == title_to_edit:
                print(f"Редактирование заметки {title_to_edit}")
                new_title = input("Введите новый заголовок (оставьте пустым, чтобы оставить текущий): ")
                new_msg = input("Введите новое сообщение (оставьте пустым, чтобы оставить текущее): ")
                note['title'] = new_title if new_title else note['title']
                note['message'] = new_msg if new_msg else note['message']
                note['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                edited = True
            edited_notes.append(note)
    
    with open('notes.json', 'w') as file:
        for note in edited_notes:
            json.dump(note, file)
            file.write("\n")

    if edited:
        print("Заметка была отредактирована.")
    else:
        print("Заметка с данным заголовком не найдена.")

def delete_note():
    read_notes()
    title_to_delete = input("Введите заголовок заметки для удаления: ")
    remaining_notes = []
    deleted = False
    with open('notes.json', 'r') as file:
        for line in file:
            note = json.loads(line.strip())
            if note['title'] != title_to_delete:
                remaining_notes.append(note)
            else:
                deleted = True
    
    with open('notes.json', 'w') as file:
        for note in remaining_notes:
            json.dump(note, file)
            file.write("\n")

    if deleted:
        print("Заметка удалена.")
    else:
        print("Заметка с данным заголовком не найдена.")

def main():
    command = input("Введите команду: ")
    
    if command == 'add':
        create_note()
    elif command == 'list':
        read_notes()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()   
    else:
        print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()






















