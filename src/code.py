import os

def run(name):
    exec(open(name).read(), globals())
    
def get_py_files():
    return [
        name
        for name in os.listdir()
        if all([
            name.lower().endswith('.py'),
            not name.startswith('.'),
            not name.lower() in [
                'code.py',
                'secrets.py',
            ],
        ])
    ]
    
def clr():
    print('\n' * 10)


clr()
python_file_names = get_py_files()
while True: # for run multiple file
    while True: # for select file
        for i, name in enumerate(python_file_names):
            print(i, name)
        input_text = input('Select index to start: ')
        try:
            selected_index = int(input_text)
            selected_file_name = python_file_names[selected_index]
            break
        except:
            clr()
            print(f'please input an int in between 0 and {len(python_file_names)-1}')
    
    clr()
    print(f'START RUNNING {selected_file_name}')
    run(selected_file_name)
    print(f'DONE RUNNING {selected_file_name}')
    
    print('Enter to continue')
    input()
    clr()