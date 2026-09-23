users = {
    "Dmytro": {
        "password": "1234",
        "grades": [12, 12, 12, 12, 12]
    },
    "Nazar": {
        "password": "password",
        "grades": [10, 9, 7, 11]
    },
    "Roman": {
        "password": "1111",
        "grades": [2, 3, 4, 5, 6]
    },
    "Yarik": {
        "password": "yarik1234",
        "grades": [9, 10, 12, 11, 11]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]

    print("\nВаші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("Задовільних оцінок (5-12):", satisfactory)
    print("Незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")