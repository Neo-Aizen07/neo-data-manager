import json
import sys
import qrcode
import time
import datetime
import uuid
import os
def time_save():
        time=datetime.datetime.now().isoformat(timespec="seconds")
        iso_time=str(time.replace("T","/"))
        return iso_time
def generate_id():
        id=uuid.uuid4().hex[:10]
        id_1=str(id)
        return id_1
def clear_proc():
    print("Initialising File Deletion", end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
def process_data():
    print("Initialising Data Loading",end=' ',flush=True)
    for i in range (3):
        time.sleep(0.3)
        print(".",end=" ",flush=True)
def process_menu():
    print("Loading",end='.',flush=True)
    for i in range(3):
        time.sleep(0.5)
    print(".",end=" \n", flush=True)
class RecordManager():
    def __init__(self): 
        self.records={}
        self.file_load(silent=True)
    def clear_menu(self):
        command=("cls"if os.name=="nt" else "clear")
        os.system(command)
        print("*" *50)
    def show_intro(self):
        print("-"*50)
        print("WELCOME TO DATABASE MANAGEMENT SYSTEM (JSON Based)")
        print("Version v1.2")
        print("="*50)
    def name_enter(self):
        username=input("Please enter a username :").strip()
        if not username or username.startswith('!_-@#$%^&*()+=[]{}|;:",.<>?/`~'):
            print("Invalid input, Username cannot be empty or start with special characters. Please try again.")
        if not username.islower(): 
            print("Invalid input, Username cannot contain uppercase letters. Please try again.")
            return
        name=input("Please enter your name :").strip()
        if not name:
            print("Invalid input, Name cannot be empty. Please try again.")
            return
        if name.isdigit() or not name.isalpha() or " " in name or not name.isascii() or any(char in '!_-@#$%^&*()+=[]{}|;:",.<>?/`~' for char in name):
            print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
            return
        if username not in self.records:
            self.records[username]={"Name": name, "ID" : generate_id(), "Last saved" :time_save()}
            self.save_names()
            print("Username, name and Unique ID added successfully")
            print(f'Your Unique ID : {self.records[username]["ID"]}')
        else:
            print("Username already exists, Please try again")
            return
        self.save_names()
    def delete_data(self):
        user_folder=self.records
        if not user_folder:
            print("Error: File is empty")
            return
        delete=input("Do you want to delete the entire data(enter 'entire data') or just a particular person's data (enter 'person') (Note: It is a permanent deletion, no way to recover the deleted data) :").lower()
        if delete=="entire data":
            print(f"Found Data :{user_folder}")
            input_y=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_y=="yes":
                clear_proc()
                try:
                    self.records.clear()
                    self.save_names()
                    print("Your data has been deleted successfully")
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error:,{e}")
            elif input_y=="no":
                print("Deletion cancelled,Returning to the main menu")
                return
            else:
                print("Data not found, Please Try Again")
        elif delete=="person":
            try:
                name=input("Please enter the username of whose data you want to remove :")
                if name in user_folder:
                    print(f"Found Data :{user_folder[name]}")
                    input_x=input("Is this the data you want to delete (Yes/No) :").lower()
                    if input_x=="yes":
                        clear_proc()
                        try:
                            del self.records[name]
                            self.save_names()
                            print(f"The data of the {name} has been deleted successfully")
                            print("Returning to main menu")
                        except FileNotFoundError as e:
                            print(f"Error: No data exists, {e}")
                        except Exception as e:
                            print(f"Error: {e}")
                    elif input_x=="no":
                        print("Deletion cancelled, Returning to main menu")
                        return
                    else:
                        print("Please enter a valid input, Returning to main menu")
                        return
                elif name not in user_folder:
                    print("Name not found, Try Again")
            except FileNotFoundError as e:
                print(f"Name not found, {e}")
        else:
            print("Invalid Input, Try Again")
    def search_name(self): # This function is used to search for a name and know whether it exists or not
        input_1=input("Do you want to search using ID, Username or Name :").lower()
        found=False
        if input_1=="name":
            name=input("Please enter your name to search :")
            for user,data in self.records.items():
                    data=self.records[user]
                    if data["Name"].lower()==name.lower():
                        print(f"Username :{user}")
                        print(f"Name : {name}")
                        print("Unique ID found :",data.get("ID"))
                        print(f"Last saved time :{data.get('Last saved')}")
                        found=True
                    else:
                        print("Name not found, Try Again")
        elif input_1=="id":
            id=input("Please enter your ID to search :")
            for username,data in self.records.items():
                data=self.records[username]
                if data["ID"] == id:
                    print(f"Username :{username}")
                    print(f"Name :", data.get("Name"))
                    print("Unique ID found :",data.get("ID"))
                    print(f"Last saved time :{data.get('Last saved')}")
                    found=True
        if not found:
            print("ID not found, Try Again")
        elif input_1=="username":
            user=input("Please enter your username to search :")
            if user in self.records:
                user_data=self.records[user]
                print(f"Username :", user)
                print(f"Name :", user_data.get("Name"))
                print("Unique ID found :",user_data.get("ID"))
                print(f"Last saved time :{user_data.get('Last saved')}")
                found=True
            else:
                print("Username not found, Try Again")
        else:
            print("Please enter a valid name or entry and try again")
            return
    def save_names(self): # This function is used to save the names to a json file and handle permission errors
        try:
            with open ("lost.json", "w") as f:
                json.dump(self.records,f,indent=4)
        except PermissionError as e:
            print(f" Error :Permission denied, {e}")
            return
        except json.JSONDecodeError as e:
            print(f"Error: failed encoding JSON, {e}")
            return
    def file_load(self,silent=False):
        try:
            with open("lost.json","r") as f:
                records_dict=json.load(f)
                self.records=records_dict
                if not silent:
                    process_data()
                    print("\nData Loaded")
                    name=input("Please enter your username to view the details :")
                    if name in self.records:
                        duplicate=self.records[name]
                        print("Your username is :",name)
                        print("Your name is :",duplicate["Name"])
                        print("Your unique ID is :",duplicate["ID"])
                        print ("last saved time :",duplicate["Last saved"])
                        print("Your file has been opened successfully")
                        silent=True
                        return
        except FileNotFoundError as e:
            if not silent:
                print(f"Error: File not found, {e}")
            return
        except json.JSONDecodeError as e:
            if not silent:
                print(f"Error: failed decoding JSON, {e}")
            return
    def qr_code(self):
        name=input("Please enter your username to search and provide the details using QR code :")
        if name not in self.records:
            print("Your username is not available in our databases")
            return
        details_0=self.records[name]
        details_1=details_0["Name"]
        details_2=details_0["ID"]
        details_3=details_0["Last saved"]
        main_details=(f"Username : {name}\n Name : {details_1}\n ID={details_2}\n Last saved={details_3}")
        img=qrcode.make(main_details)
        unique_id=uuid.uuid4().hex
        file=(f"{unique_id}qr.png")
        img.save(file)
        try:
            img.show()
            time.sleep(15.0)
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            print(f"Error: {e}")
    def menu(self): #This is the menu part where the options can be accessed
        while True:
            print("-"*15+"MENU for DATABASE MANAGEMENT SYSTEM"+"-"*15)
            print("1-Enter name")
            print("2-Search Name")
            print("3-Load Names")
            print("4-Exit")
            print("5-Generate QR Code")
            print("6- Delete")
            print("="*50)
            try:
                choice=int(input("Please enter your choice :"))
            except ValueError:
               print("Invalid input, Please enter a number")
               continue
            if choice==1:
                process_menu()
                self.name_enter()
            elif choice==2:
                 process_menu()
                 self.search_name()  
            elif choice==3:
                process_menu()
                self.file_load()
            elif choice==4:
                process_menu()
                self.save_names()
                print("Thank you for using the program, Your Progress has been saved")
                sys.exit()
            elif choice==5:
                process_menu()
                self.qr_code()
            elif choice==6:
                process_menu()
                self.delete_data()
            else:
                print("Invalid choice, Please try again")
                continue
manager=RecordManager()
manager.show_intro()
manager.menu()