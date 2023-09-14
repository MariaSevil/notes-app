import json
import datetime


def create_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    # TODO: Сохранение заметки
    print("Заметка успешно сохранена")

def main():
    command = input("Введите команду: ")
    
    if command == 'add':
        create_note()
    elif command == 'list':
        read_notes()
    else:
        print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()


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




















