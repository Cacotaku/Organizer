from pathlib import Path
import os
import datetime

def _cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

new_Folder = "OrganizadorDeArquivos" ### specify the name of the new folder

path = os.getcwd() ### get the current working directory

_cleanScreen() ### clean screen

print(f"Default directory: {path}") ### print the default directory

option_input = input(f"Do you want to change the directory? (y/n)").lower().strip() ### ask user if they want to change the directory

while(option_input not in ['y', 'n']): ### validate user input

    option_input = input(f"Invalid option! Do you want to change the directory? (y/n)").lower().strip() ### ask user if they want to change the directory

if(option_input == 'y'):  ### if user wants to change the directory
    
    path = input(f"""Type the new directory path: 
                 Exemple: {os.getcwd()}""").strip() ### ask user for the new directory path
    
    if(os.path.exists(path) is True):  ### if the path exists

        print(f"Path {path} found!")

    else:

        while(os.path.exists(path) is False):  ### while the path does not exist
        
            print(f"Path {path} does not exists!")
            path = input(f"""Type the new directory path: 
                Exemple: {os.getcwd()}""").strip() ### ask user for the new directory path
        

os.chdir(path)  ### change the current working directory to the new path
print(f"Current folder: {os.getcwd()}")  ## print the current working directory


if(not os.path.exists(new_Folder)): ### check if the new folder exists
    
    os.mkdir(new_Folder)  ### create the new folder
    print(f"Folder {new_Folder} created sucessfully!")

else:
    
    print(f"Folder {new_Folder} already exists.")

for files in os.listdir():  ### iterate through the files in the current directory
    
    print(files)
    
    if os.path.isfile(files): ### check if it is a file

        extension = files.split(".")[-1]  ### get the file extension

        if ("." in files):  ### check if the file has an extension

            if(extension in ["lnk", "exe", "ini", "sys"]):  ### skip system files
                
                continue

            elif(not os.path.exists(f"{new_Folder}//{extension}")):  ### check if the folder for the extension exists

                os.mkdir(f"{new_Folder}//{extension}")  ### create the folder for the extension
                print(f"Folder {extension} created sucessfully!")

            else:

                print(f"Folder {extension} already exists.")    
            
            os.replace(files, f"{new_Folder}/{extension}/{files}")  ### move the file to the folder for the extension
            print(f"File {files} moved to folder {extension} successfully!")
    