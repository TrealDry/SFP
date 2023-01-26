class CliDev:

    def __init__(self, low_api=None):
        self.low_api = low_api
        print("cli-dev loading...")

    def command(self, command):
        if command == "?exit":
            exit()
        elif command == "?method_list":
            return self.low_api.get_method_list()

    def run_hapi(self):
        print(self.low_api.get_method_list())
        while True:
            input_command = input(">>> ")
            if input_command:
                args = input_command.split("&")
                packed_args = None

                if args[0][0] == "?":
                    print(self.command(args[0]))
                    continue
                if args[-1] == "?array":
                    args.pop(-1)
                    packed_args = [args[1:]]

                if not packed_args:
                    print(self.low_api.method_call(args[0], args[1:]))
                else:
                    print(self.low_api.method_call(args[0], packed_args))


PLUGIN_NAME = "test-cli"


def run():
    return [CliDev]
