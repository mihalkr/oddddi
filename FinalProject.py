import sqlite3

connection = sqlite3.connect('log.sl3')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Users (login TEXT, password TEXT, phone TEXT)")
connection.commit()

def user_login(cur):
    login = input("login: ")
    cur.execute("SELECT password, phone FROM Users WHERE login=?", (login,))
    result = cur.fetchone()
    if result:
        save_password = result[0]
        password = input("Password: ")
        if password == save_password:
            print(f"Вітаємо у системі {login}")
        else:
            print("Неправильні Дані!")

def user_reg(cur, connection):
    login = input("Придумайте логін: ")
    cur.execute("SELECT 1 FROM Users WHERE login=?", (login,))
    if cur.fetchone():
        print("Цей логін уже зайнятий!")
    else:
        password = input("Введіть пароль: ")
        phone = input("Введіть номер телефону: ")
        cur.execute("INSERT INTO Users (login, password, phone) VALUES (?, ?, ?)", (login, password, phone))
        print(f"{login} успішно зареєстрований!")
        connection.commit()

def main():
    print("Виберіть свою дію")
    print("1. Ввійти")
    print("2. Зареєструватися")
    log = input("Ваша дія: ")

    if log == "1":
        user_login(cur)
    elif log == "2":
        user_reg(cur, connection)
    else:
        print("Виберіть 1 або 2")

if __name__ == "__main__":
    main()
    connection.close()