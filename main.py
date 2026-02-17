from RecordManager import RecordManager
from user_interface import show_intro,clear_menu
import sys
from file_data import verify
manager=RecordManager()
def menu(record_manager):   
    while True:
        print("\n"+"="*50)
        print("-"*15+"MENU for DATABASE MANAGEMENT SYSTEM"+"-"*15)
        print("1-Enter name")
        print("2-Search Name")
        print("3-Load Names")
        print("4-Generate QR Code")
        print("5- Delete Entire Data")
        print("6- Delete a particular person's data")
        print("7- Verify file location and existence")
        print("8- Exit")
        print("="*50)
        try:
            choice=int(input("Please enter your choice :"))
        except ValueError:
            print("Invalid input, Please enter a number")
            continue
        if choice==1:
            manager.name_enter()
        elif choice==2:
            manager.search_func()
        elif choice==3:
            manager.file_load()
        elif choice==4:
            manager.qr_code()
        elif choice==5:
            manager.delete_data()
        elif choice==6:
            manager.delete_person()
        elif choice==7:
            verify()
        elif choice==8:
            record_manager.save_names()
            print("Thank you for using the program, Your Progress has been saved")
            sys.exit()
            break
        else:
            print("Invalid choice, Please try again")
            continue
if __name__=="__main__":
    show_intro()
    menu(manager)