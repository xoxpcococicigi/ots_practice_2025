# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Зиновьев Михаил Владимирович

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    system_info = {
        "student_name": "Зиновьев Михаил Владимирович",
        "academic_group": "ИВТИИбд-14",
        "github_link": "https://github.com/xoxpcococicigi"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
