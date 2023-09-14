

def main():
    command = input("Введите команду: ")
    print(f"Вы ввели команду: {command}")

if __name__ == "__main__":
    main()

def create_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    # TODO: Сохранение заметки
    print("Заметка успешно сохранена")

def main():
    command = input("Введите команду: ")
    
    if command == 'add':
        create_note()
    else:
        print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()
