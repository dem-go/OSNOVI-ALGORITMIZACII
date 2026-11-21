import math


def section(number, title):
    """Печатает заголовок задания."""
    print()
    print("=" * 72)
    print(f"ЗАДАНИЕ {number}. {title}")
    print("=" * 72)


# ======================================================================
# БЛОК 1. Объявление производных классов (задания 1–5)
# ======================================================================

class Animal:
    """Базовый класс животного: имя и общий звук."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Возвращает звук животного (в базовом классе — нейтральный)."""
        return "Какой-то звук"

    def info(self):
        """Возвращает строку «имя: звук»."""
        return f"{self.name}: {self.speak()}"


class Dog(Animal):
    """Собака: добавляет породу и переопределяет speak()."""

    def __init__(self, name, breed="дворняга"):
        super().__init__(name)          # базовая часть инициализируется первой
        self.breed = breed              # собственный атрибут

    def speak(self):
        return "Гав!"


class Cat(Animal):
    """Кошка: своего __init__ нет, переопределён только speak()."""

    def speak(self):
        return "Мяу!"


class Cow(Animal):
    """Корова: своего __init__ нет, переопределён только speak()."""

    def speak(self):
        return "Муу!"


class Person:
    """Человек: имя и возраст."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Возвращает представление «Я Анна, мне 19 лет.»."""
        return f"Я {self.name}, мне {self.age} лет."


class Student(Person):
    """Студент: к человеку добавляется группа."""

    def __init__(self, name, age, group):
        super().__init__(name, age)     # инициализация базовой части
        self.group = group

    def introduce(self):
        """Дополняет базовое представление сведениями о группе."""
        return super().introduce() + f" Учусь в группе {self.group}."


class Device:
    """Устройство: атрибут класса vendor и метод включения."""

    vendor = "Неизвестный производитель"

    def turn_on(self):
        return f"{self.vendor}: устройство включено"


class Laptop(Device):
    """Ноутбук: наследует turn_on() и vendor, добавляет compile()."""

    def compile(self):
        return "Компиляция программы завершена"


def task01():
    """Задание 1. Иерархия животных Animal → Dog, Cat, Cow."""
    section(1, "Иерархия животных Animal → Dog, Cat, Cow")

    # Что добавляет каждый наследник:
    # Dog — атрибут breed и собственный __init__ (вызывает super().__init__);
    # Cat и Cow — только переопределённый speak(), __init__ наследуют.
    zoo = [Dog("Рекс", "овчарка"), Cat("Мурка"), Cow("Зорька")]

    for animal in zoo:
        print(animal.info())

    print("isinstance(zoo[0], Animal):", isinstance(zoo[0], Animal))
    print("issubclass(Cow, Animal):", issubclass(Cow, Animal))


def task02():
    """Задание 2. Person → Student: расширение метода через super()."""
    section(2, "Person → Student: расширение метода")

    person = Person("Анна", 19)
    student = Student("Анна", 19, "П-21")

    print("Person.introduce():", person.introduce())
    print("Student.introduce():", student.introduce())
    print("isinstance(person, Person):", isinstance(person, Person))
    print("isinstance(student, Person):", isinstance(student, Person))

    # Student не заменяет поведение Person, а дополняет его: строка
    # базового класса получена через super().introduce(), затем к ней
    # приписано упоминание группы.


def task03():
    """Задание 3. Проверка иерархии: issubclass, isinstance, __bases__."""
    section(3, "Проверка иерархии: issubclass, isinstance, __bases__")

    student = Student("Анна", 19, "П-21")

    print("issubclass(Dog, Animal):", issubclass(Dog, Animal))
    print("issubclass(Student, Person):", issubclass(Student, Person))
    print("issubclass(Person, Dog):", issubclass(Person, Dog))
    print("isinstance(student, Person):", isinstance(student, Person))
    print('isinstance("текст", Person):', isinstance("текст", Person))

    print("Dog.__bases__:", Dog.__bases__)
    print("Student.__bases__:", Student.__bases__)
    print("Person.__bases__:", Person.__bases__)

    # У Person в скобках не указан базовый класс, поэтому Python неявно
    # наследует его от object — общего корня всех классов. Именно поэтому
    # в __bases__ Person находится (object,), а isinstance(любой_объект,
    # object) всегда истинно.


def task04():
    """Задание 4. Employee → Manager: наследование без переопределений."""
    section(4, "Employee → Manager: наследование без переопределений")

    class Employee:
        """Сотрудник с именем и окладом."""

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def info(self):
            return f"{self.name}: оклад {self.salary}"

    class Manager(Employee):
        """Менеджер: базовая часть плюс отдел."""

        def __init__(self, name, salary, department):
            super().__init__(name, salary)  # сначала базовая часть
            self.department = department    # затем собственная

    manager = Manager("Анна", 80000, "ИТ-отдел")

    # info() в Manager не переопределён: работает унаследованный метод,
    # который видит атрибут name базовой части.
    print("info():", manager.info())
    print("name:", manager.name)
    print("salary:", manager.salary)
    print("department:", manager.department)
    print("isinstance(manager, Employee):", isinstance(manager, Employee))

    # Manager получил весь публичный интерфейс Employee (name, salary,
    # info) и добавил только department — дублирования кода нет.


def task05():
    """Задание 5. Что именно наследуется — эксперимент."""
    section(5, "Что именно наследуется — эксперимент")

    laptop = Laptop()

    print("hasattr(laptop, 'turn_on'):", hasattr(laptop, "turn_on"))
    print("hasattr(laptop, 'compile'):", hasattr(laptop, "compile"))
    print("hasattr(laptop, 'vendor'):", hasattr(laptop, "vendor"))
    print("isinstance(laptop, object):", isinstance(laptop, object))

    # Метод базового класса можно вызвать явно, передав ему объект-
    # наследник как self: поиск атрибутов идёт по цепочке классов, а
    # turn_on() использует только self.vendor, унаследованный от Device.
    print("Device.turn_on(laptop):", Device.turn_on(laptop))

    # Вывод: наследование — это поиск атрибута по цепочке классов;
    # turn_on и vendor найдены у Device, compile — у Laptop.


# ======================================================================
# БЛОК 2. super(): расширение инициализатора и методов (задания 6–10)
# ======================================================================

class Employee:
    """Сотрудник: оклад и строка о доходе."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def income(self):
        """Возвращает доход сотрудника (в базовом классе — оклад)."""
        return self.salary

    def info(self):
        """Возвращает строку о доходе; вызывает self.income()."""
        return f"{self.name}: доход {self.income():.0f} руб."


class Manager(Employee):
    """Руководитель: оклад плюс бонус."""

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)      # базовая часть
        self.bonus = bonus

    def income(self):
        # Расширение базового расчёта, а не его замена.
        return super().income() + self.bonus


class Developer(Employee):
    """Разработчик: надбавка за уровень."""

    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def income(self):
        k = {1: 1.0, 2: 1.2, 3: 1.5}.get(self.level, 1.0)
        return self.salary * k


class Intern(Employee):
    """Стажёр: почасовая оплата."""

    def __init__(self, name, hourly_rate, hours):
        super().__init__(name, 0)           # оклада нет
        self.hourly_rate = hourly_rate
        self.hours = hours

    def income(self):
        return self.hourly_rate * self.hours


def task06():
    """Задание 6. Расчётная иерархия сотрудников."""
    section(6, "Расчётная иерархия сотрудников")

    staff = [
        Manager("Анна", 80000, 15000),
        Developer("Борис", 70000, 3),
        Employee("Вера", 60000),
        Intern("Глеб", 500, 80),
    ]

    for person in staff:
        print(person.info())

    total = sum(person.income() for person in staff)
    print(f"Суммарный доход: {total:.0f} руб.")

    # info() объявлен только в Employee, но вызывает self.income() —
    # для каждого объекта выполняется своя переопределённая версия.


class Product:
    """Товар: название и цена."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class DiscountedProductBroken(Product):
    """Ошибочная версия товара со скидкой: пропущен super().__init__."""

    def __init__(self, name, price, discount):
        self.discount = discount            # ОШИБКА: name и price не созданы


class DiscountedProduct(Product):
    """Исправленная версия: сначала базовая часть, затем скидка."""

    def __init__(self, name, price, discount):
        super().__init__(name, price)       # первая строка — базовая часть
        self.discount = discount

    def final_price(self):
        """Цена с учётом скидки."""
        return self.price * (1 - self.discount)


def task07():
    """Задание 7. Разбор ошибки: пропущенный super().__init__."""
    section(7, "Разбор ошибки: пропущенный super().__init__")

    broken = DiscountedProductBroken("Ноутбук", 50000, 0.1)
    try:
        print(broken.name)
    except AttributeError as exc:
        print("AttributeError:", exc)
        # Сообщение говорит, что у объекта нет атрибута name: производный
        # __init__ создал только discount и не вызвал инициализатор
        # Product, поэтому name и price не были созданы.

    fixed = DiscountedProduct("Ноутбук", 50000, 0.1)
    print("name:", fixed.name)
    print("price:", fixed.price)
    print("discount:", fixed.discount)
    print(f"Цена со скидкой: {fixed.final_price():.2f} руб.")

    # Правило: в переопределённом __init__ вызов super().__init__(...)
    # выполняется первой строкой, чтобы базовая часть была готова до
    # создания собственных атрибутов.


class Vehicle:
    """Транспортное средство: марка и модель."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"Транспорт: {self.brand} {self.model}"


class Car(Vehicle):
    """Автомобиль: добавляет число дверей."""

    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def describe(self):
        return super().describe() + f", дверей: {self.doors}"


class Bicycle(Vehicle):
    """Велосипед: добавляет тип рамы."""

    def __init__(self, brand, model, frame_type):
        super().__init__(brand, model)
        self.frame_type = frame_type

    def describe(self):
        return super().describe() + f", рама: {self.frame_type}"


def task08():
    """Задание 8. Транспорт: Vehicle → Car, Bicycle."""
    section(8, "Транспорт: Vehicle → Car, Bicycle")

    vehicles = [
        Car("Lada", "Vesta", 4),
        Bicycle("Stels", "Navigator", "горная"),
        Car("Toyota", "Camry", 4),
        Bicycle("Forward", "Apache", "городская"),
    ]

    for vehicle in vehicles:
        print(vehicle.describe())

    # describe() наследников вызывает super().describe(), поэтому строка
    # содержит базовую часть и собственное дополнение.


class Point2D:
    """Точка на плоскости."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """Расстояние до другой точки на плоскости."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Point ({self.x}; {self.y})"


class Point3D(Point2D):
    """Точка в пространстве: добавляет координату z."""

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance_to(self, other):
        """Расстояние до другой точки в пространстве."""
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )

    def __str__(self):
        # Дополняем базовую строку: вставляем z перед закрывающей скобкой.
        return f"{super().__str__()[:-1]}; {self.z})"


def task09():
    """Задание 9. Точка на плоскости → точка в пространстве."""
    section(9, "Точка на плоскости → точка в пространстве")

    a = Point2D(0, 0)
    b = Point2D(3, 4)
    print(a, "→", b, ":", a.distance_to(b))

    p = Point3D(0, 0, 0)
    q = Point3D(1, 2, 2)
    print(p, "→", q, ":", p.distance_to(q))

    # Переопределение заменяет метод: Point3D.distance_to() считает уже
    # три координаты. super() позволяет не заменять, а дополнять: новая
    # __str__ строится на строке базового класса.


def task10():
    """Задание 10. Rectangle → Square: преобразование аргументов."""
    section(10, "Rectangle → Square: преобразование аргументов")

    class Rectangle:
        """Прямоугольник с шириной и высотой."""

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    class Square(Rectangle):
        """Квадрат: один параметр side превращается в width = height."""

        def __init__(self, side):
            super().__init__(side, side)    # повторное использование __init__

    square = Square(5)
    print("Сторона: 5")
    print("area():", square.area())
    print("perimeter():", square.perimeter())
    print("isinstance(square, Rectangle):", isinstance(square, Rectangle))

    # Квадрат является прямоугольником (частный случай с равными
    # сторонами), поэтому наследование уместно. Square.__init__ не
    # дублирует создание атрибутов, а передаёт side в базовый
    # инициализатор через super().__init__(side, side).


# ======================================================================
# БЛОК 3. Переопределение методов и диспетчеризация (задания 11–15)
# ======================================================================

class Shape:
    """Геометрическая фигура с именем."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Площадь; у абстрактной фигуры — 0.0."""
        return 0.0

    def __str__(self):
        return f"{self.name}: площадь {self.area():.2f}"


class Rectangle(Shape):
    """Прямоугольник."""

    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    """Круг."""

    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def task11():
    """Задание 11. Фигуры: Shape → Rectangle, Circle."""
    section(11, "Фигуры: Shape → Rectangle, Circle")

    figures = [
        Rectangle(3, 4),
        Circle(2),
        Rectangle(5, 2),
        Circle(1),
        Rectangle(1, 1),
    ]

    print("area() базового Shape:", Shape("Абстрактная фигура").area())
    print("Фигуры по возрастанию площади:")
    for figure in sorted(figures, key=lambda f: f.area()):
        print(" ", figure)

    # key=lambda f: f.area() вызывает метод без проверки типов: у каждой
    # фигуры есть area(), а нужная реализация выбирается по классу объекта.


class Notification:
    """Базовое уведомление."""

    def send(self):
        return "Базовое уведомление"


class EmailNotification(Notification):
    """Уведомление по электронной почте."""

    def __init__(self, address):
        self.address = address

    def send(self):
        return f"Email на {self.address}: подтвердите заказ"


class SmsNotification(Notification):
    """SMS-уведомление."""

    def __init__(self, phone):
        self.phone = phone

    def send(self):
        return f"SMS на {self.phone}: код подтверждения 1234"


class PushNotification(Notification):
    """Push-уведомление."""

    def __init__(self, device):
        self.device = device

    def send(self):
        return f"Push на {self.device}: новое сообщение"


def broadcast(messages):
    """Печатает результат send() для каждого уведомления.

    Функция ничего не знает о конкретных классах: ей достаточно
    контракта «у уведомления есть метод send()».
    """
    for message in messages:
        print(message.send())


def task12():
    """Задание 12. Диспетчеризация: функция работает с базовым классом."""
    section(12, "Диспетчеризация: функция работает с базовым классом")

    broadcast([
        EmailNotification("student@example.com"),
        SmsNotification("+7 900 000-00-00"),
        PushNotification("смартфон"),
    ])

    # PushNotification добавлен после написания broadcast(), но функция
    # заработала без изменений: вызывается n.send(), а конкретная
    # реализация выбирается динамически по классу объекта.


class Greeter:
    """Приветствие."""

    def hello(self):
        return "Привет!"


class FormalGreeter(Greeter):
    """Официальное приветствие."""

    def hello(self):
        # Способ 1: super() — автоматически идёт по MRO.
        return super().hello() + " Добрый день!"

    def hello_direct(self):
        # Способ 2: прямой вызов метода базового класса по имени.
        return Greeter.hello(self) + " Добрый день!"


def task13():
    """Задание 13. Два способа вызвать базовый метод."""
    section(13, "Два способа вызвать базовый метод")

    greeter = FormalGreeter()
    print("super().hello():", greeter.hello())
    print("Greeter.hello(self):", greeter.hello_direct())
    print("Результаты совпадают:", greeter.hello() == greeter.hello_direct())

    # super() предпочтительнее: он автоматически находит ближайшую
    # реализацию по MRO. При изменении иерархии (например, при появлении
    # промежуточного класса) super() продолжит работать, а жёстко
    # прописанный Greeter.hello(self) — нет.


class Account:
    """Счёт с приватным балансом и контролируемым интерфейсом."""

    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.owner = owner
        self.__balance = float(balance)     # приватный атрибут

    @property
    def balance(self):
        """Баланс только для чтения."""
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount

    def __str__(self):
        return f"Счёт ({self.owner}): {self.__balance:.2f} руб."


class CreditAccount(Account):
    """Кредитный счёт: к балансу добавляется кредитный лимит."""

    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.limit = limit

    def available(self):
        """Доступная сумма: баланс плюс лимит."""
        return self.balance + self.limit

    def read_private(self):
        """Провокация ошибки: прямое обращение к __balance базового класса.

        После name mangling имя превращается в _CreditAccount__balance,
        которого не существует (реальное имя — _Account__balance).
        """
        return self.__balance


def task14():
    """Задание 14. Приватное состояние и наследование."""
    section(14, "Приватное состояние и наследование")

    account = CreditAccount("Смирнов А. А.", 10000, 5000)
    print("Начало:", account)
    print(f"available(): {account.available():.2f}")

    account.deposit(3000)
    print("После пополнения на 3000:", account)
    account.withdraw(2000)
    print("После снятия 2000:", account)
    print(f"available(): {account.available():.2f}")

    # Обязательная демонстрация реакции на некорректные данные.
    try:
        account.deposit(-100)
    except ValueError as exc:
        print("ValueError (пополнение -100):", exc)

    try:
        account.withdraw(999999)
    except ValueError as exc:
        print("ValueError (снятие 999999):", exc)

    try:
        account.read_private()
    except AttributeError as exc:
        print("AttributeError:", exc)
        print("Причина: name mangling превращает self.__balance в "
              "_CreditAccount__balance; реальный атрибут называется "
              "_Account__balance.")

    # Наследник работает с состоянием базового класса только через его
    # интерфейс: свойство balance (чтение), deposit()/withdraw()
    # (изменение). Так сохраняются все проверки корректности.


def task15():
    """Задание 15. Многоуровневая иерархия: Person → Employee → Manager."""
    section(15, "Многоуровневая иерархия: Person → Employee → Manager")

    class Person:
        """Человек."""

        def __init__(self, name):
            self.name = name

        def introduce(self):
            return f"Я {self.name}"

    class Employee(Person):
        """Сотрудник: человек плюс оклад."""

        def __init__(self, name, salary):
            super().__init__(name)
            self.salary = salary

        def introduce(self):
            return (super().introduce()
                    + f", работаю за {self.salary:.0f} руб.")

    class Manager(Employee):
        """Менеджер: сотрудник плюс отдел."""

        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department = department

        def introduce(self):
            return (super().introduce()
                    + f", руковожу отделом {self.department}")

    person = Person("Анна")
    employee = Employee("Борис", 70000)
    manager = Manager("Вера", 90000, "ИТ-отдел")

    print(person.introduce())
    print(employee.introduce())
    print(manager.introduce())
    print("Manager.__mro__:", Manager.__mro__)
    print("isinstance(manager, Person):", isinstance(manager, Person))
    print("issubclass(Manager, Person):", issubclass(Manager, Person))

    # Каждый уровень дополняет строку предыдущего через super(), поэтому
    # представления становятся всё полнее, а код не дублируется.


# ======================================================================
# БЛОК 4. Иерархии с инкапсуляцией и полиморфные списки (16–18)
# ======================================================================

def task16():
    """Задание 16. Ведомость доходов."""
    section(16, "Ведомость доходов")

    staff = [
        Manager("Анна", 80000, 15000),
        Developer("Борис", 70000, 3),
        Employee("Вера", 60000),
        Intern("Глеб", 500, 80),
        Manager("Дина", 90000, 20000),
        Developer("Егор", 65000, 2),
    ]

    total = sum(person.income() for person in staff)
    average = total / len(staff)
    best = max(staff, key=lambda person: person.income())
    above_average = [p for p in staff if p.income() > average]

    for person in staff:
        print(person.info())

    print(f"Фонд оплаты труда: {total:.0f} руб.")
    print("Максимальный доход:", best.info())
    print(f"Средний доход: {average:.2f} руб.")
    print("Сотрудников с доходом выше среднего:", len(above_average))

    # В коде обработки нет ни одного isinstance: все объекты понимают
    # info() и income(), а нужная реализация выбирается динамически.


class LibraryItem:
    """Материал библиотеки: название и год."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        return f"{self.title} ({self.year})"


class Book(LibraryItem):
    """Книга: автор и число страниц."""

    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def describe(self):
        return (super().describe()
                + f", {self.author}, {self.pages} с.")


class Magazine(LibraryItem):
    """Журнал: номер и месяц."""

    def __init__(self, title, year, issue, month):
        super().__init__(title, year)
        self.issue = issue
        self.month = month

    def describe(self):
        return (super().describe()
                + f", № {self.issue}, {self.month}")


class Library:
    """Контейнер материалов с приватным списком."""

    def __init__(self):
        self.__items = []                   # инкапсулированный список

    def add_item(self, item):
        """Добавляет материал; не LibraryItem — ошибка TypeError."""
        if not isinstance(item, LibraryItem):
            raise TypeError(
                "Библиотека принимает только объекты LibraryItem"
            )
        self.__items.append(item)

    def show_all(self):
        """Полиморфно выводит describe() всех материалов."""
        for item in self.__items:
            print(item.describe())

    def count_by_class(self, cls):
        """Считает материалы указанного класса (с учётом наследников)."""
        return sum(1 for item in self.__items if isinstance(item, cls))


def task18():
    """Задание 18. Библиотека: иерархия материалов и контейнер."""
    section(18, "Библиотека: иерархия материалов и контейнер")

    library = Library()
    library.add_item(Book("Война и мир", 1873, "Л. Н. Толстой", 1225))
    library.add_item(
        Book("Преступление и наказание", 1866, "Ф. М. Достоевский", 672)
    )
    library.add_item(Book("Мастер и Маргарита", 1967, "М. А. Булгаков", 480))
    library.add_item(Magazine("Наука и жизнь", 2024, 5, "май"))
    library.add_item(Magazine("Квант", 2024, 7, "июль"))

    print("Все материалы:")
    library.show_all()
    print("Книг:", library.count_by_class(Book))
    print("Журналов:", library.count_by_class(Magazine))

    try:
        library.add_item("просто строка")
    except TypeError as exc:
        print("TypeError:", exc)

    # Library не наследует LibraryItem: библиотека «имеет» материалы
    # (has-a), поэтому здесь композиция — приватный список __items.


# ======================================================================
# БЛОК 5. Задания повышенной сложности (19–20)
# ======================================================================

def task19():
    """Задание 19*. Трёхуровневая иерархия счетов."""
    section(19, "Трёхуровневая иерархия счетов (повышенная сложность)")

    class SavingsAccount(Account):
        """Накопительный счёт: приватная ставка и начисление процентов."""

        def __init__(self, owner, balance=0.0, rate=0.05):
            super().__init__(owner, balance)    # базовый уровень
            if rate <= 0:
                raise ValueError("Ставка должна быть положительной")
            self.__rate = rate                  # приватная ставка

        @property
        def rate(self):
            return self.__rate

        def add_interest(self):
            """Начисляет проценты через deposit(), возвращает сумму."""
            interest = self.balance * self.__rate   # чтение через свойство
            self.deposit(interest)                  # изменение через метод
            return interest

        def __str__(self):
            return super().__str__() + f" | ставка {self.__rate:.0%}"

    class VipSavingsAccount(SavingsAccount):
        """VIP-счёт: повышенная ставка и лояльностный бонус."""

        def __init__(self, owner, balance=0.0, rate=0.10):
            super().__init__(owner, balance, rate)

        def add_loyalty_bonus(self, amount=1000.0):
            self.deposit(amount)                # только через метод базы

        def __str__(self):
            return super().__str__() + " | VIP"

    accounts = [
        Account("Иванов И. И.", 10000),
        SavingsAccount("Петров П. П.", 20000, rate=0.05),
        VipSavingsAccount("Сидоров С. С.", 50000),
        SavingsAccount("Кузнецова К. К.", 15000, rate=0.07),
    ]

    for account in accounts:
        if isinstance(account, SavingsAccount):
            interest = account.add_interest()
            print(f"Начислены проценты: {interest:.2f} руб.")
        if isinstance(account, VipSavingsAccount):
            account.add_loyalty_bonus()
            print("Начислен VIP-бонус: 1000.00 руб.")
        print(account)

    try:
        SavingsAccount("Ошибка", 1000, rate=0)
    except ValueError as exc:
        print("ValueError:", exc)

    # Три уровня иерархии: Account хранит баланс, SavingsAccount добавляет
    # ставку и проценты, VipSavingsAccount — бонус и пометку VIP. Каждый
    # __str__ строится на строке предыдущего уровня через super().


def task20():
    """Задание 20*. Фабрика объектов и группировка по типам."""
    section(20, "Фабрика объектов и группировка по типам (повышенная "
                "сложность)")

    factory = {"dog": Dog, "cat": Cat, "cow": Cow}
    specs = [
        ("dog", "Рекс", "овчарка"),
        ("cat", "Мурка"),
        ("cow", "Зорька"),
    ]

    animals = []
    for spec in specs:
        code, args = spec[0], spec[1:]
        animals.append(factory[code](*args))    # класс вызывается как функция

    for animal in animals:
        print(animal.info())

    counts = {
        cls.__name__: sum(1 for a in animals if isinstance(a, cls))
        for cls in (Dog, Cat, Cow)
    }
    print("Количество по типам:", counts)

    # Классы в Python — объекты первого класса: их можно хранить в
    # словаре, передавать и вызывать как функции. Новый вид животного
    # добавляется одной строкой в factory, остальной код не меняется.


# ======================================================================
# Точка входа
# ======================================================================

def task17():
    """Задание 17. Фигуры: сортировка, агрегаты и подсчёт по типам."""
    section(17, "Фигуры: сортировка, агрегаты и подсчёт по типам")

    figures = [
        Rectangle(2, 3),
        Circle(1),
        Rectangle(5, 4),
        Circle(2.5),
        Rectangle(1, 7),
        Circle(0.5),
        Rectangle(3, 3),
    ]

    print("Фигуры по убыванию площади:")
    for figure in sorted(figures, key=lambda f: f.area(), reverse=True):
        print(" ", figure)

    total = sum(figure.area() for figure in figures)
    largest = max(figures, key=lambda f: f.area())
    circles = sum(1 for figure in figures if isinstance(figure, Circle))
    rectangles = sum(
        1 for figure in figures if isinstance(figure, Rectangle)
    )

    print(f"Суммарная площадь: {total:.2f}")
    print("Самая большая фигура:", largest)
    print("Кругов:", circles)
    print("Прямоугольников:", rectangles)

    # Единый интерфейс area() позволяет сортировать, суммировать и
    # выбирать максимум без проверки типов; isinstance нужен только для
    # подсчёта количества по конкретным классам.


def main():
    """Выполняет все задания по порядку."""
    print("ПРАКТИЧЕСКАЯ РАБОТА № 3. НАСЛЕДОВАНИЕ В PYTHON")

    task01()
    task02()
    task03()
    task04()
    task05()
    task06()
    task07()
    task08()
    task09()
    task10()
    task11()
    task12()
    task13()
    task14()
    task15()
    task16()
    task17()
    task18()
    task19()
    task20()


if __name__ == "__main__":
    main()

