import shutil
import os
with open('my_data.txt', 'w', encoding='utf-8') as f:
    f.write('Python\n')
    f.write('JavaScript\n')

with open('my_data.txt', 'a', encoding='utf-8') as f:
    f.write('C++\n')
    f.write('Rust\n')

with open('my_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
    
shutil.copy('my_data.txt', 'my_data_backup.txt')

if os.path.exists("my_data_backup.txt"):
    os.remove("my_data.txt")