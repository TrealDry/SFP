class LowAPI:

    def __init__(self, class_space):
        self.hapi_method = None
        self.method_space = {}
        self.class_space = class_space

    def init_method_space(self):  # Инициализация списка методов
        for name_class, this_class in self.class_space.items():  # Перебираем классы
            method_list = []

            for attribute in dir(this_class):  # Ищем методы в классе
                attribute_value = getattr(this_class, attribute)
                if not callable(attribute_value):
                    continue
                if attribute.startswith('__') is not False:
                    continue
                method_list.append(attribute)

            this_object = this_class(self)  # Создаём объект класса, чтобы вынуть методы из него

            for method in method_list:
                method_object = getattr(this_object, method)

                # Ключ = (Имя Плагина).(Имя класса).(Метод класса); Значение = ссылка на метод объекта;
                self.method_space[f"{name_class}.{method}"] = method_object

                # Моментально запускаем метод run
                if method == "run":
                    method_object()
                elif method == "run_hapi":
                    self.hapi_method = method_object

        # Только один метод с именем run_hapi может работать с пользователем
        if self.hapi_method:
            self.hapi_method()

    def get_method_list(self):  # Получаем все методы ввиде массива
        method_list = []
        for method, _ in self.method_space.items():
            method_list.append(method)
        return method_list

    def method_call(self, method, args):  # Вызовы функций других плагин
        try:
            if args:
                return self.method_space[method](*args)
            return self.method_space[method]()
        except KeyError:
            return "this method does not exist"
        except TypeError:
            return "invalid arguments"

    def get_method(self, method_name):  # Возвращает ссылку на метод
        try:
            return self.method_space[method_name]
        except KeyError:
            return None
