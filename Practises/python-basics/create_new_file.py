import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "structure.txt")

with open(file_path, "r", encoding="utf-8") as file:
    content = [line.rstrip("\n") for line in file]

# чистим псевдографику дерева
content = [item.replace('├── ', '')
                 .replace('│   ', '')
                 .replace('└── ', '')
                 .replace('/', '')
           for item in content]

root_dir = content[0]
last_file = content[-1]

# создаём корневую папку
os.makedirs(root_dir, exist_ok=True)

# создаём последний файл
open(os.path.join(root_dir, last_file), "w").close()

# убираем их из списка
content = content[1:-1]

current_path = root_dir

for item in content:
    if '.' not in item:
        # это папка
        current_path = os.path.join(root_dir, item)
        os.makedirs(current_path, exist_ok=True)
    else:
        # это файл
        open(os.path.join(current_path, item), "w").close()