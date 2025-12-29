def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local  

def write_todos(todos_arg,filepath ="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(type(__name__))
if __name__ == "__main__":
    print("Hello from functions.")  
    print(get_todos())     

"""def count(phrase):
    return phrase.count('.')"""
