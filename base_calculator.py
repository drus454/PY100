def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Ошибка: деление на 0"
    return a / b

def calculator():
    print("Выберите операцию")
    print("1: Сложение")
    print("2: Вычитание")
    print("3: Умножение")
    print("4: Деление")

    while True:
        choice = input("Введите номер операции '1', '2', '3', '4', или 'q' для выхода: ")

        if choice == 'q':
            print("Выход из калькулятора")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите корректные числа")
                continue

            if choice == '1':
                print(f"{num_1} + {num_2} = {addition(num_1, num_2)}")
            elif choice == '2':
                print(f"{num_1} - {num_2} = {subtraction(num_1, num_2)}")
            elif choice == '3':
                print(f"{num_1} * {num_2} = {multiplication(num_1, num_2)}")
            elif choice == '4':
                print(f"{num_1} / {num_2} = {division(num_1, num_2)}")
        else:
            print("Неверный ввод. Пожалуйста, выберите операцию из списка.")

if __name__ == "__main__":
    calculator()

