from RecordManager import RecordManager
from user_interface import show_intro,clear_menu
import sys
from file_data import verify
from logger import log_info,log_menu
manager=RecordManager()
def menu(manager):  
    while True:
        print("\n"+"="*50)
        print("-"*15+"MENU for DATABASE MANAGEMENT SYSTEM"+"-"*15)
        print("1-Enter Details(For First Time Data Entry)")
        print("2-Search Details(For Existing Data)")
        print("3- Delete Entire Data")
        print("4- Delete a particular user's data")
        print("5- Verify file location and existence")
        print("6- Open logs")
        print("7- Exit")
        print("="*50)
        try:
            choice=int(input("Please enter your choice in integers :"))
            log_info(f"User entered a value : {choice}",level="INFO")
        except ValueError:
            log_info("User entered invalid menu choice",level="WARNING")
            print("Invalid input, Please enter a number")
            continue
        except Exception as e:
            print("AN Unknown Error Occured")
            log_info(f"ERROR : {e}",level="ERROR")
        if choice==1:
            manager.name_enter()
        elif choice==2:
            manager.search_func()
        elif choice==3:
            manager.delete_data()
        elif choice==4:
            manager.delete_person()
        elif choice==5:
            verify()
        elif choice==6:
            log_menu()
        elif choice==7:
            log_info("Program has Exited",level="INFO")
            sys.exit()
        else:
            print("No Valid input found")
            log_info("User Entered an Incorrect Option",level="WARNING")
            continue
if __name__=="__main__":
    show_intro()
    menu(manager)