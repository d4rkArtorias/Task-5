'''1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку)
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.
 
Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
3. Выложите проект на github:
4. Можно сдать задание в виде pull request:
5. Посмотреть разбор дз по функциям, если требуется, то сделать работу надо ошибками.1. Создать новый проект ""Консольный файловый менеджер"'''
import os
import shutil
import sys
from famous_persons import get_random_person, get_person_and_question
while True:
    print('1. Создать папку')
    print('2. Удалить папку')
    print('3. Копировать файл')
    print('4. Показать содержимое директории')
    print("5. Посмотреть информацию об операционной системе")
    print('6. Cоздатель программы')
    print('7. Играть в викторину')
    print('8. Мой банковский счет')
    print('9. Выход')
    choise = int(input("Выберите пункт: "))
    if choise == 1:
        folder = input("Пункт: создать папку, введите название папки: ")
        os.mkdir(f"D:\Python\console_file_manager\{folder}")
    elif choise == 2:
        folder_delete = input("Пункт: удалить папку, введите название папки: ")
        os.rmdir(f"D:\Python\console_file_manager\{folder_delete}")
    elif choise == 3:
        copy_file = str(input("Пункт: копировать файл, введите название файла который хотите копировать "))
        shutil.copy(f"D:\Python\console_file_manager\{copy_file}.py", "D:\Python\console_file_manager\copy.py")
    elif choise == 4:
        print(os.listdir("D:\Python\console_file_manager"))
    elif choise == 5:
        print(f"Информация об операционной системе: {sys.platform}, {sys.getwindowsversion()}")
    elif choise == 6:
        print("Создатель программы: Tuzee :)")
    elif choise == 7:
        rounds = int(input('Сколько раз вы хотите играть?'))
        for i in range(rounds):
            get_person_and_question()
    elif choise == 8:
        buy_list = []
        your_account = 0

        while True:
            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. выход')
            print(f'5. Ваш счет: {your_account}')

            choice = input('Выберите пункт меню ')
            if choice == '1':
                replenishment = int(input("Введите на какую сумму поплнить счет: " ))
                your_account += replenishment
            elif choice == '2':
                replenishment = int(input("Введите сумму покупки: " ))
                if replenishment > your_account:
                    print("Недостаточно средств")
                else:
                    your_account -= replenishment
                    buy_name = input("Введите название покупки: ")
                    buy_list.append(buy_name)
            elif choice == '3':
                print(f"Ваши покупки: {buy_list}")
            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')
    else:
        break