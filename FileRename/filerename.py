import os
from os import listdir
from os.path import isfile, join


def main():
    path = "C:\\Users\\jyoun\\Desktop\\C0D3\\PythonStuff\\FileRename\\TestFiles"
    
    print("**********FILE RENAMING TOOL**********")
    path = input("Provide folder path containing files: ")
    #path = path.replace("\\", "\\\\")
    print(path)
    print("Pick a naming convention:")
    print("1. No Spaces (test01)")
    print("2. Underscores (test_01)")
    print("3. Periods (test.01)")
    print("4. Uppercase (TEST01)")
    print("5. Lowercase (test01)")

    user_input = input("Your Choice: ")
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)

    rename(user_input, onlyfiles)

def rename(user_input, onlyfiles):
    style = {1:"", 2:"_", 3:"."}

    #UpperCase
    if user_input == 4:
        pass
    #LowerCase
    elif user_input == 5:
        pass
    #1-3
    else:
        pass

#Check for existing naming convention
def check_files(onlyfiles):
    pass

if __name__ == "__main__":   
    main()