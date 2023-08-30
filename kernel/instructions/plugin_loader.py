import os
import sys
import importlib
import importlib.util
from os.path import join


class PluginLoader:

    def __init__(self):
        self.class_space = {}  # Ссылки на классы
        self.plugin_path = [
            join(".", "kernel", "official_plugins"),
            join(".", "plugins")
        ]

    @staticmethod
    def import_plugin(executable_name: str, file_path: str):  # Импорт main.py
        spec = importlib.util.spec_from_file_location(executable_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    def import_all_plugins(self):
        if self.class_space:
            self.class_space = {}

        for path in self.plugin_path:
            for root, directory, file in os.walk(path):
                for files_plugin in file:
                    if files_plugin != "main.py":
                        continue
                    sys.path.append(root)
                    try:
                        plugin = self.import_plugin("main.py", f"{root}\\{files_plugin}")
                    except:
                        continue
                    try:
                        for args in plugin.run():
                            # Ключ = (Имя плагина).(имя класса); Значение = ссылка на класс;
                            self.class_space[f"{plugin.PLUGIN_NAME}.{args.__name__}"] = args
                    except AttributeError:
                        continue
                    except TypeError:
                        continue

        return self.class_space
