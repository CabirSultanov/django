""""
class Car:
    def __init__(self, model="Неизвестно", year=0, manufacturer="Неизвестно", engine_volume=0.0, color="Не указан", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price


    def display_info(self, show_price=True):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        if show_price:
            print(f"Цена: {self.price} $")

    def set_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        elif isinstance(new_price, str) and new_price.endswith("%"):
            percent = float(new_price.strip("%"))
            self.price += self.price * (percent / 100)
        else:
            print("Некорректный формат цены")

    def repaint(self, new_color):
        self.color = new_color


car = Car("Camry", 2020, "Toyota", 2.5, "Черный", 30000)
print("\nИнформация об авто:\n")
car.display_info()

print("\nИзменим цвет и цену:\n")
car.repaint("Коричневый")
car.set_price("10%")
car.display_info()


#
class Book:
    def __init__(self, title="Без названия", year=0, publisher="Неизвестно", genre="Не указан", author="Неизвестен", price=0.0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price


    @classmethod
    def short(cls, title, author):
        return cls(title=title, author=author)


    def display_info(self, show_price=True):
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        if show_price:
            print(f"Цена: {self.__price} $")
        print(f"Год издания: {self.__year}")
        print(f"Издатель: {self.__publisher}")
        print(f"Жанр: {self.__genre}")

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


book1 = Book("Война и мир", 1869, "Русский Вестник", "Роман", "Лев Толстой", 45)
book2 = Book.short("Преступление и наказание", "Ф. Достоевский")

print("\nИнформация о книге 1:\n")
book1.display_info()

print("\nИнформация о книге 2 (короткий конструктор):\n")
book2.display_info(show_price=False)



class Stadium:
    def __init__(self, name="Без названия", opening_date="Неизвестна", country="Не указано", city="Не указан", capacity=0):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity


    def set_capacity(self, new_capacity):
        if isinstance(new_capacity, str) and new_capacity.lower().endswith("k"):
            self.__capacity = int(float(new_capacity[:-1]) * 1000)
        elif isinstance(new_capacity, int) and new_capacity > 0:
            self.__capacity = new_capacity
        else:
            print("Вместимость должна быть положительным числом")


    def display_info(self, show_country=True):
        print(f"Стадион: {self.__name}")
        print(f"Дата открытия: {self.__opening_date}")
        if show_country:
            print(f"Страна: {self.__country}")
        print(f"Город: {self.__city}")
        print(f"Вместимость: {self.__capacity} зрителей")


stadium1 = Stadium("Олимпийский", "19 июля 1980", "Россия", "Москва", 78000)
print("\nИнформация о стадионе:\n")
stadium1.display_info()

print("\nИзменим вместимость строкой '110k':\n")
stadium1.set_capacity("110k")
stadium1.display_info()
"""