from os import getenv, chdir, mkdir, rmdir, listdir, getcwd, remove
from shutil import copy
from distutils.dir_util import copy_tree
try:
    user_input = input("USER ")
    password_input = input("PASSWORD ")
except KeyboardInterrupt:
    print("\nProgram ended by keyboard interruption")
    exit()
def authenticate(user, password):
    user_authorized = getenv("USER")
    if (user != user_authorized):
        return False
    password_authorized = getenv("PASSWORD")
    if (password != password_authorized):
        return False
    return True    
if (authenticate(user_input, password_input)):
    login = True
    print("Login successfully")
else:
    login = False
    print("Access denied")
home_dir = getenv("HOMEDIR")
chdir(home_dir)
atual_directory = home_dir
options = ("new", "del", "ls", "mkdir", "rmdir", "cp", "mv", "cd", "backup", "help", "exit")
while login == True:
    try:
        user_input = input(f"{atual_directory}> ")
        command = user_input.split(" ")[0]    
        while command not in options:
            print("Command not found. Type `help' to see command list")
            break
        try:
            if command == "new":
                file_name = user_input.split(" ")[1]
                open(file_name, "x")
            if command == "del":
                file_name = user_input.split(" ")[1]
                remove(file_name)
            if command == "ls":        
                for item in listdir(atual_directory):
                    print(" " , item)
            if command == "mkdir":
                create_dir_name = user_input.split(" ")[1]
                mkdir(create_dir_name)          
            if command == "rmdir":
                remove_dir_name = user_input.split(" ")[1]
                rmdir(remove_dir_name)
            if command == "cp":
                file_name = user_input.split(" ")[1]
                end_point = user_input.split(" ")[2]
                copy(file_name, end_point)
            if command == "mv":
                file_name = user_input.split(" ")[1]
                end_point = user_input.split(" ")[2]
                copy(file_name, end_point)
                remove(file_name)
            if command == "cd":
                path = user_input.split(" ")[1]
                chdir(path)
                path = getcwd()
                atual_directory = path
            if command == "backup":
                backup_path = getenv("BACKUP")
                copy_tree(atual_directory, backup_path)
            if command == "help":
                for option in options:
                    print(" " , option)
            if command == "exit":
                break
                exit()
        except FileExistsError:
            print("File or Directory already exists")
        except FileNotFoundError:
            print("File or Directory not found")
        except OSError:
            print("Path name is incorrect")
        except IndexError:
            print("Incorrect command")
    except KeyboardInterrupt:
            print("\nProgram ended by keyboard interruption")
            break
            exit()
