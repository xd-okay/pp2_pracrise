
with open('my_data.txt', 'w', encoding='utf-8') as f:
    f.write('Python\n')
    f.write('JavaScript\n')

with open('my_data.txt', 'a', encoding='utf-8') as f:
    f.write('C++\n')
    f.write('Rust\n')

with open('my_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)