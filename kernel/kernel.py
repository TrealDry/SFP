class Kernel:

    def __init__(self, instructions):
        self.plugin_loader = instructions.PluginLoader
        self.low_api = instructions.LowAPI

    def start(self):
        self.plugin_loader = self.plugin_loader()

        self.low_api = self.low_api(
            self.plugin_loader.import_all_plugins()
        )
        self.low_api.init_method_space()
