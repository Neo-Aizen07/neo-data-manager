import os
import datetime
import uuid
from storage import save_names
from user_interface import time_save, generate_id
def name_enter(record_manager):
        from storage import save_names
        try:
            print("The data will be stores locally on ", os.path.abspath(__file__))
            username=input("Please enter a username :").strip()
            if username in record_manager.records:
                print("Username already exists, Please try again")
                return
            if not username:
                print("Invalid input, Username cannot be empty. Please try again.")
                return
            name_first=input("Please enter your first name :").strip()
            name_last=input("Please enter your Last name (optional if exsists):").strip()
            if not name_first:
                print("Invalid input, Name cannot be empty. Please try again.")
                return
            elif not name_first.isalpha():
                print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
                return
            if not name_first.isalpha():
                print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
                return
            if name_last and not name_last.isalpha():
                print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
                return
            if " " in name_first:
                print("Invalid input, Name cannot contain spaces. Please try again.")
                return
            elif any(char in '!_-@#$%^&*()+=[]{}|;:",.<>?/`~' for char in name_first):
                print("Invalid input, Name cannot contain special characters. Please try again.")
                return
            elif "  " in name_last:
                print("Invalid input, Name cannot contain spaces. Please try again.")
                return
            elif any(char in '!_-@#$%^&*()+=[]{}|;:",.<>?/`~' for char in name_last):
                print("Invalid input, Name cannot contain special characters. Please try again.")
                return
            name=(name_first+" "+name_last).strip()
            if username not in record_manager.records:
                record_manager.records[username]={"Name": name, "ID" : generate_id(), "Last saved" :time_save()}
                save_names(record_manager)
                print("Username, name and Unique ID added successfully")
                print(f'Your Unique ID : {record_manager.records[username]["ID"]}')
            else:
                print("Data already exists, Please try again")
                return
        except Exception as e:
            print(f"Error: {e}")