import string
import time

#Имя приложения, которое будет использоваться при запуске,
# в коде менятся не должно, является константой
APPLICATION_NAME_CONST = "Academia Mate"

isRunning = True
exitKeyword = "Выход"
role1 = "Учитель"
role2 = "Ученик"

def print_role2_features():
    print("\nКак ученик вы можете:" +
          "\n1. Узнать своё расписание" +
          "\n2. Выяснить свою успеваемость" +
          "\n3. Посмотреть информацию об одноклассниках")

def print_role1_features():
    print("\nКак учитель вы можете:" +
          "\n1. Посмотреть всех учеников вашего класса" +
          "\n2. Выяснить успеваемость всех учеников по вашему предмету")

def display_role_features(userRole):
    if userRole == role1:
        print_role1_features()
    elif userRole == role2:
        print_role2_features()

def get_validated_user_role_or_loop_until_validate():
    validated = False

    while not validated:
        userRole = input("Введите 1 если вы учитель и 2 если ученик: ")
        if (userRole == "1"):
            userRole = role1
            validated = True
        elif (userRole == "2"):
            userRole = role2
            validated = True
        else:
            print("\nВы ввели неверную цифру, попробуйте ещё раз: ")
            validated = False

    return userRole

def show_all_pupils():
    print("\nВсе ученики:\n1. Иванов Александр\n2. Петрова Екатерина\n3. Смирнов Даниил\n4. Кузнецова Анна" +
          "\n5. Васнецов Артём\n6. Михайлова Виктория\n7. Козлов Илья\n8. Соколова Елена" +
          "\n9. Никитин Дмитрий 4\n10. Лебедева Анастасия\n11. Семёнов Артур\n12. Козырёва Юлия" +
          "\n13. Григорьев Максим\n14. Титова София\n15. Захаров Никита\n16. Медведева Алёна" +
          "\n17. Поляков Владислав\n18. Романова Елизавета\n19. Волков Аркадий\n20. Савельвева Арина")
    time.sleep(3)

def show_all_pupils_grades():
    print("\nУспеваемость учеников по предмету Математика:\n1. Иванов Александр 2 3 1\n2. Петрова Екатерина 5 5 5 5 4\n3. Смирнов Даниил 4 3 3 3\n4. Кузнецова Анна 2 5" +
          "\n5. Васнецов Артём 4 4 4 4 4\n6. Михайлова Виктория 3 2 4 5\n7. Козлов Илья\n8. Соколова Елена 1 1 1" +
          "\n9. Никитин Дмитрий 4\n10. Лебедева Анастасия 3 2 5\n11. Семёнов Артур 4 4 3\n12. Козырёва Юлия 5 5" +
          "\n13. Григорьев Максим 4 5 2 4 4\n14. Титова София 5 2 3 2\n15. Захаров Никита 4 4 3\n16. Медведева Алёна 5 5 4" +
          "\n17. Поляков Владислав 3 3 1 3\n18. Романова Елизавета 4 5 5 5 5\n19. Волков Аркадий 4 4 3 5\n20. Савельвева Арина 4 5 3 5")
    time.sleep(3)

def show_academic_performance_of_subject():
    print("У учеников учителя математики следующие оценки.."
          "\n1. Иванов Александр: 2 3 1\n2. Петрова Екатерина 5 5 5 5 4\n3. Смирнов Даниил 4 3 3 3\n4. Кузнецова Анна 2 5" +
          "\n5. Васнецов Артём 4 4 4 4 4\n6. Михайлова Виктория 3 2 4 5\n7. Козлов Илья\n8. Соколова Елена 1 1 1" +
          "\n9. Никитин Дмитрий 4\n10. Лебедева Анастасия 3 2 5\n11. Семёнов Артур 4 4 3\n12. Козырёва Юлия 5 5" +
          "\n13. Григорьев Максим 4 5 2 4 4\n14. Титова София 5 2 3 2\n15. Захаров Никита 4 4 3\n16. Медведева Алёна 5 5 4" +
          "\n17. Поляков Владислав 3 3 1 3\n18. Романова Елизавета 4 5 5 5 5\n19. Волков Аркадий 4 4 3 5\n20. Савельвева Арина 4 5 3 5")
    time.sleep(3)

def show_schedule():
    print("\nРасписание на неделю:" + "\nПонедельник:\n1.Русский язык\n2.Математика\n3.Информатика\n4.История\n" +
          "\nВторник:\n1.Обществознание\n2.Физика\n3.Физическая культура\n4.Литература\n" +
          "\nСреда:\n1.Английский язык\n2.Биология\n3.География\n4.Технология\n" +
          "\nЧетверг:\n1.Физическая культура\n2.Химия\n3.Математика\n4.Немецкий язык\n" +
          "\nПятница:\n1.Литература\n2.Информатика\n3.Обществознание\n4.Исскуство\n" +
          "\nСуббота и Воскресенье - отдых!")
    time.sleep(3)

def show_grades():
    print("\nВаша текущая успеваемость в школе" +
          "\n1. Русский язык: 4 3 1\n2. Математика: 4 5 5\n3. Информатика: 5\n4. История: 4 4 4 4\n5. Обществознание: 3 2 4 5 1 2" +
          "\n6. Физика: 5 3 3\n7. Английский язык: 4 5 5 5 5\n8. Биология: 3 3 3\n9. Физическая культура: 3\n10. Литература: 5 4" +
          "\n11. География: 5 3 3\n12. Технология: 4 4\n13. Химия: 2 2 2\n14. Немецкий Язык: 3 2\n15. Исскуство: 4 5 5 5 4")
    time.sleep(3)

def match_user_features_input(userInput, userRole):
    if userRole is role1:
        if userInput == "1":
            time.sleep(1)
            show_all_pupils()
        elif userInput == "2":
            time.sleep(1)
            show_all_pupils_grades()

    elif userRole == role2:
        if userInput == "1":
            time.sleep(1)
            show_schedule()
        elif userInput == "2":
            time.sleep(1)
            show_grades()
        elif userInput == "3":
            time.sleep(1)
            show_all_pupils()

def get_login_n_password_from_user_input():
    login = input("Самое время установить новый логин, а именно..: ")

    while not login != '':
        login = input("Видимо вы оставили поле ввода логина пустым, попробуем ещё раз!: ")

    password = input("Теперь пришло время установить элегантный пароль: ")

    while not password != '':
        password = input("Ваш пароль совсем не элегантный! Он пустой, попробуем ещё раз: ")

    return login, password

def get_validated_name_n_surname_from_user_input(userRole):
    validated = False
    if userRole is role1:
        print("\nТеперь вы учитель")
        teacherNameSurnamePatronymic = input("Введите свою Фамилию Имя Отчество в указанном порядке: ")

        while not teacherNameSurnamePatronymic != '':
            teacherNameSurnamePatronymic = input("\nВозможно вы не заполнили строки символами, попробуйте ещё раз: ")
            validated = teacherNameSurnamePatronymic == ''

        return teacherNameSurnamePatronymic

    elif userRole is role2:
        print("\nТеперь вы ученик")
        pupilNameSurname = input("Введите свою Фамилию и Имя в указанном порядке: ")

        while not pupilNameSurname != '':
            pupilNameSurname = input("\nВозможно вы оставили строки пустыми, попробуйте вновь: ")
            validated = pupilNameSurname == ''

        return pupilNameSurname

def try_to_register_user():
    userRole = get_validated_user_role_or_loop_until_validate()
    userFullName = get_validated_name_n_surname_from_user_input(userRole)
    login, password = get_login_n_password_from_user_input()

    print("\nПоздравляю с регистрацией! Ваша информация:" + "\nИмя: " + userFullName + ", " +  userRole + '\n' + "Логин: " + login + '\n' + "Пароль: " + password)
    time.sleep(2)

    return userRole, userFullName, login, password

print("Добро пожаловать в " + APPLICATION_NAME_CONST)
time.sleep(1.5)
print("Видимо вы используете наше приложение впервые, для продолжения нужно зарегистрироваться")
time.sleep(1)

userRole, userFullName, userLogin, userPassword = try_to_register_user()

while isRunning:
    display_role_features(userRole)
    userInput = input("\n Введите цифру команды или " + exitKeyword + " для выхода: ")

    while not userInput != '':
        userInput = input("\n Возможно вы ошиблись цифрой, или неправильно написали слово " + exitKeyword + "!: ")

    if userInput == exitKeyword:
        isRunning = False
        break

    match_user_features_input(userInput, userRole)

print("Спасибо за использование нашего приложения, мы это ценим! До новых встреч!")
