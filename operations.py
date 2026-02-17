import os
import time
from storage import save_names
def clear_proc():
    print("Initialising File Deletion", end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
def search_func(record_manager):
    input_1=input("Do you want to search using ID, Username or Name :").lower()
    found=False
    if input_1=="name":
        search_names(record_manager)
    elif input_1=="id":
        search_id(record_manager)
    elif input_1=="username":
        search_username(record_manager)
    else:
        print("Please enter a valid entry and try again")
        return
def search_names(record_manager):
    name=input("Please enter your name to search :").lower()
    for user,data in record_manager.records.items():
        if data["Name"].lower().strip()==name.lower():
            username=user
            name=data.get("Name")
            uid=data.get("ID")
            last=data.get("Last saved")
            print(f"Username : {username} \n Name : {name}\n ID : {uid}\n Last Saved : {last}")
            found=True
            break
    if not found:
        print("Name not found, Try Again")
def search_id(record_manager):
    id=input("Please enter your ID to search :")
    found=False
    for user,details in record_manager.records.items():
        if details["ID"] == id:
            username=user
            name=details.get("Name")
            uid=details.get("ID")
            last=details.get("Last saved")
            print(f"Username : {username} \n Name : {name}\n ID : {uid}\n Last Saved : {last}")
            found=True
            break
    if not found:
        print("ID not found, Try Again")
def search_username(record_manager):
    user=input("Please enter your username to search :")
    if user in record_manager.records:
        data=record_manager.records[user]
        username=user
        name=data.get("Name")
        uid=data.get("ID")
        last=data.get("Last saved")
        print(f"Username : {username} \n Name : {name}\n ID : {uid}\n Last Saved : {last}")
        found=True
    else:
        print("Username not found, Try Again")
def delete_data(record_manager):
        print("Warning: This action will permanently delete your data, Please be sure before proceeding")
        user_folder=record_manager.records
        if not user_folder:
            print("Error: File is empty")
            return
        delete_confirm=input("Do you want to proceed with the deletion (Yes/No) :").lower()
        if delete_confirm=="yes":
            print(f"Found Data :{user_folder}")
            input_y=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_y=="yes":
                clear_proc()
                try:
                    record_manager.clear()
                    save_names(record_manager)
                    print("Your data has been deleted successfully")
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error:{e}")
            elif input_y=="no":
                print("Deletion cancelled,Returning to the main menu")
                return
            else:
                print("Data not found, Please Try Again")
                return
        if delete_confirm=="no":
            print("Deletion cancelled, Returning to the main menu")
            return
def delete_person(record_manager):
            user_folder=record_manager.records
            try:
                name=input("Please enter the username of whose data you want to remove :")
                if name in user_folder:
                    print("Data present at : ", os.path.abspath(__file__))
                    print("Data file name : data.json")
                    print(f"Found Data :{user_folder[name]}")
                    input_x=input("Is this the data you want to delete (Yes/No) :").lower()
                    if input_x=="yes":
                        clear_proc()
                        try:
                            del record_manager.records[name]
                            save_names(record_manager.records)
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
            except Exception as e:
                print(f"Error: {e}")