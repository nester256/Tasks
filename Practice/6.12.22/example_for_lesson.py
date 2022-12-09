# Приимер библиотеки
from multiprocessing import Process, Queue, Lock, Event
from random import randint
from time import sleep


# Методы чтобы выводить цветной текст
def print_yellow(text: str):
    print("\033[33m{}\033[0m".format(text))


def print_green(text: str):
    print("\033[32m{}\033[0m".format(text))


def print_red(text):
    print("\033[31m{}\033[0m" .format(text))


class Client:
    ACTIONS = "GET", "HAND"     # Получить / Сдать книгу

    def __init__(self, name: str, book: str, action: str):
        self.name = name    # Имя клиента
        self.book = book    # Имя клиента
        self.action = action    # Действие (получить/взять)

    def is_valid(self):     # Проверка валидности всех атрибутов класса клиент
        if all([isinstance(v, str) for v in self.__dict__.values()]):
            return self.action in Client.ACTIONS
        return False

    def __str__(self): # Вывод информации клиента
        return "Имя: {}, Действие: {} книгу {}".format(self.name, self.action, self.book)


class Library:
    def __init__(self, database: dict, q_size: int):
        self.q_size = q_size                        # Максимальный размер очереди
        self.database = database                    # Книги (Сама бибилиотека книг) - это словарь.
        self.__queue = Queue(maxsize=q_size)        # Очередь класса очередь (для поточности исполнения)
        self.__worker = Librarian(database)         # Работник библиотеки
        self.__process = Process(target=self.work)  # Передача метода в процесс
        self.mutex = Lock()                         # Колокольчик (блокировка) для

    def open(self): # Метод открытия бибилиотеки
        print("Библиотека открывается, мест в очереди: {0}".format(self.q_size))
        self.__process.start()

    def close(self): # Метод закрытия бибилиотеки
        print("Библиотека закрывается")
        items = self.database.items()
        free = list(filter((lambda item : item[1]), items))
        taken = list(filter((lambda item: not item[1]), items))
        print_green('Доступные для прочения: {}'.format([name for name, _ in free]))
        print_red('Не доступные для прочения: {}'.format([name for name, _ in taken]))

    def enter(self, client: Client):
        with self.mutex:
            print("Клиент {0}, пришёл в бибилиотеку".format(client.name))
            if self.__queue.full(): # Если очередь переполнена
                print("Клиент {}, пошёл домой - мест нет".format(client.name))
            else: # Если в очереди есть место
                values = client.name, client.action, client.book
                print("Клиент {} хочет {} книгу: {}".format(*values))
                self.__queue.put(client)
                self.__worker.call()

    # Метод работы библиотеки.
    # Библиотекарь либо работает в бибилиотеке, либо работает с клиентами
    def work(self):
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result, db = self.__worker.work()
                self.database = db
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)


class Librarian:
    TIMEOUT = 10    # Время ожидания перед закрытием
    WORK_INTERVAL = (1, 3)

    def __init__(self, database: dict):
        self.database = database
        self.__client_came = Event()

    def work(self): # Метод работы бибилиотекаря
        print_yellow("Библиотекарь работает с книгами")
        result = self.__client_came.wait(timeout=Librarian.TIMEOUT) # Ждём событие
        return result, self.database

    def give(self, client: Client):
        if client.book in self.database.keys():
            if not self.database[client.book]:
                sleep(randint(*Librarian.WORK_INTERVAL)) # Время за которое он ищет книгу
                print("Библиотекарь отдал книгу {0}, клиенту {1}".format(client.book, client.name))
                self.database[client.book] = client.name
            else:
                print("Этой книги {} нет сейчас".format(client.book))
        else:
            print("Этой книги {} нет в бибилиотеке".format(client.book))

    def take(self, client: Client):
        if client.book in self.database.keys():
            if self.database[client.book] == client.name:
                print("Библиотекарь забрал книгу {0}, у клиента {1}".format(client.book, client.name))
            else:
                print("Книга {} у другого клиента".format(client.book))
        else:
            print("Книга {}, не существует".format(client.book))

    def greet(self, client: Client):  # Метод приветствия клиента
        self.__client_came.clear()
        print("Библиотекарь приветствует клиента: {0}".format(client.name))
        if client.action == "GET":
            self.give(client)
        else:
            self.take(client)
        print("Клиент {} - обслужен".format(client.name))

    def call(self):             # Метод вызова библиотекаря
        self.__client_came.set()    # Устанавливает событие что пришёл клиент


SIZE_QUEUE = 3
ENTER_TIME_INTERVAL = (1, 3)
BOOKS = [
    'Энциклопедия',
    'Мир Животных',
    'My mammy',
    'Идиот',
]

if __name__ == '__main__':
    lock = Lock()
    database = {book: None for book in BOOKS}
    clients_borrowed = [Client(str(i), book, 'GET') for i, book in enumerate(BOOKS)]
    clients_handed = [Client(str(i), book, 'HAND') for i, book in enumerate(BOOKS)]
    clients = clients_borrowed + clients_handed
    library = Library(database, SIZE_QUEUE)
    library.open()
    for client in clients:
        library.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
