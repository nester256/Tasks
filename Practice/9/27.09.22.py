# Пример использования модуля os

import os

for path, dirs, files in os.walk("/home/nester/Рабочий стол/Directory"):
    print("-" * path.count("/"), end="" + path + "\n")
    print(dirs)
    print(files)
    print("-" * 30)
