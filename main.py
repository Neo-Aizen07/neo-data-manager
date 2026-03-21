from RecordManager import RecordManager
from user_interface import show_intro,clear_menu
import sys
from file_data import verify
from logger import log_info,log_menu
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
console=Console()
manager=RecordManager()
def menu(manager):  
  while True:
        console.print(Panel(
            "[1] Register New User\n"
            "[2] Search Records\n"
            "[3] Delete All Data\n"
            "[4] Delete a User\n"
            "[5] System Status\n"
            "[6] Open Logs\n"
            "[7] Exit",
            title="Neo Data Manager v1.7",
            style="bold cyan"
        ))
        try:
            choice=int(input("Please enter your choice in integers :"))
            log_info(f"User entered a value : {choice}",level="INFO")
        except ValueError:
            log_info("User entered invalid menu choice",level="WARNING")
            console.print(Text("Invalid input, Please enter a number", style="bold red"))
            continue
        except Exception as e:
            console.print(Text("An Unknown Error Occurred", style="bold red"))
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
            console.print(Text("Invalid option, Please try again", style="yellow"))
            log_info("User Entered an Incorrect Option",level="WARNING")
            continue
if __name__=="__main__":
    show_intro()
    menu(manager)