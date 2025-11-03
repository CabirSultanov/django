"""
class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} $")


    def set_price(self, new_price):
        self.price = new_price


    def repaint(self, new_color):
        self.color = new_color



car = Car("Camry", 2020, "Toyota", 2.5, "Черный", 30000)

print("\nИнформация об авто:\n")
car.display_info()

print("\nИзменим цвет и цену:\n")
car.repaint("Коричневый")
car.set_price(250000)

car.display_info()
===

===
class Book:                # Инкапсуляция
    def __init__(self, title, year, publisher, genre, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_publisher(self):
        return self.__publisher

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена должна быть положительной")

    def set_publisher(self, new_publisher):
        if new_publisher:
            self.__publisher = new_publisher
        else:
            print("Издатель не может быть пустым!")


    def display_info(self):
        print(f"Название: {self.__title}")
        print(f"Год издания: {self.__year}")
        print(f"Издатель: {self.__publisher}")
        print(f"Жанр: {self.__genre}")
        print(f"Автор: {self.__author}")
        print(f"Цена: {self.__price} $.")



book1 = Book("Война и мир", 1869, "Русский Вестник", "Роман", "Лев Толстой", 45)

print("\nИнформация о книге:\n")
book1.display_info()

print("\nИзменим издателя и цену:\n")
book1.set_publisher("Эксмо")
book1.set_price(60)

book1.display_info()


===
class Stadium:              # Инкапсуляция
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity


    def get_name(self):
        return self.__name

    def get_opening_date(self):
        return self.__opening_date

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_capacity(self):
        return self.__capacity

    def set_name(self, new_name):
        self.__name = new_name if new_name else self.__name

    def set_opening_date(self, new_date):
        self.__opening_date = new_date if new_date else self.__opening_date

    def set_country(self, new_country):
        self.__country = new_country if new_country else self.__country

    def set_city(self, new_city):
        self.__city = new_city if new_city else self.__city

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity if new_capacity > 0 else self.__capacity
        if new_capacity <= 0:
            print("Вместимость должна быть положительной")


    def display_info(self):
        print(f"Стадион: {self.__name}")
        print(f"Дата открытия: {self.__opening_date}")
        print(f"Страна: {self.__country}")
        print(f"Город: {self.__city}")
        print(f"Вместимость: {self.__capacity} зрителей")



stadium1 = Stadium("Олимпийский", "19 июля 1980", "Россия", "Москва", 78000)

print("\nИнформация о стадионе:\n")
stadium1.display_info()

print("\nИзменим город и вместимость:\n")
stadium1.set_city("Магадан")
stadium1.set_capacity(110000)

stadium1.display_info()
"""