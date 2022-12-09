import json

class JsonWorker:
    def __init__(self, path: str) -> None:
        with open(path, "rt") as file:
            data = file.read()
            try:
                conf_data = json.loads(data)
            except Exception as e:
                print("Assert exeption as read file")
                raise e
            try:
                self.ip = conf_data["ip"]
                self.name = conf_data["name"]
                self.device = conf_data["device"]
                self.ports = {port["port"] : [port["name"], port["device"]] \
                              for port in conf_data["ports"]}
            except KeyError:
                print("Doesnt exist attr")


class Request:
    def __init__(self, port: int, attr: str, value=None) -> None:
        try:
            self.port = int(port)
            self.attr = str(attr)
            self.value = value
        except ValueError:
            print("Exeption for invalid attrs or port")
            if self.value:
                pass
            else:
                pass


first = JsonWorker("config.json")
print(first.ports)


