import os
from os import listdir
from os.path import isfile, join


def main():
    #path = "C:\\Users\\jyoun\\Desktop\\C0D3\\PythonStuff\\FileRename\\TestFiles"
    
    print("**********FILE RENAMING TOOL**********")
    path = input("Provide folder path containing files: ")
    print(path)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(f"Files in given directory: {onlyfiles}")

    print("Pick a naming convention:")
    print("1. No Spaces (test01)")
    print("2. Underscores (test_01)")
    print("3. Uppercase (TEST01)")
    print("4. Lowercase (test01)")
    print("5. Rename Individual File")

    user_input = int(input("Your Choice: "))

    rename_file(path, user_input, onlyfiles)

def rename_file(path, user_input, onlyfiles):

    #No Spaces
    if user_input == 1:
        for i in range(len(onlyfiles)):
            if " " in onlyfiles[i]:
                #onlyfiles[i] = onlyfiles[i].replace(" ", "")
                os.rename(path + "\\" + onlyfiles[i], path + "\\" + onlyfiles[i].replace(" ", ""))

    #UnderScores
    elif user_input == 2:
        pass
    #UpperCase
    elif user_input == 3:
        pass
    #LowerCase
    elif user_input == 4:
        pass
    #Rename Individual
    else:
        pass

#Check for existing naming convention
def check_files(onlyfiles):
    pass

if __name__ == "__main__":   
    main()