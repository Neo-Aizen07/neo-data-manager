from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from RecordManager import RecordManager
import time
from logger import log_info
from storage import get_db
from rich.console import Console
from rich.text import Text
console=Console()
def clear_proc()->None:
    print("Initialising File Deletion", end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
def delete_data(record_manager : 'RecordManager')->None:
        with get_db() as conn:
            console.print(Text("Warning: This will permanently delete all data", style="bold red"))
            cursor=conn.execute("select * from records")
            rows=cursor.fetchall()
        if not rows:
            console.print(Text("Database is empty — nothing to delete", style="yellow"))
            log_info("Attempted Deletion on Empty Database",level="WARNING")
            return
        delete_confirm=input("Do you want to proceed with the deletion (Yes/No) :").lower()
        if delete_confirm=="yes":
            console.print(Text(f"Found Data : {record_manager.display_data()}",style="green"))
            input_y=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_y=="yes":
                clear_proc()
                try:
                    record_manager.delete_0()
                    console.print(Text("All data deleted successfully", style="green"))
                    log_info("All records deleted successfully", level="WARNING")
                except Exception as e:
                    console.print(Text("An error occurred during deletion", style="bold red"))
                    log_info(f"ERROR :{e}",level="CRITICAL")
            elif input_y=="no":
                console.print(Text("Deletion cancelled", style="yellow"))
                log_info("Full deletion cancelled by user", level="INFO")
                return
            else:
                console.print(Text("Invalid input, returning to menu", style="yellow"))
                log_info("Data Not Found",level="ERROR")
                return
        if delete_confirm=="no":
            console.print(Text("Deletion cancelled", style="yellow"))
            log_info("Full deletion cancelled by user", level="INFO")
            return
def delete_person(record_manager : 'RecordManager')->None:
        with get_db() as conn:
            try:
                name=input("Please enter the username of whose data you want to remove :")
                console.print(Text(f"Found Data : {record_manager.display_user(name)}",style="green"))
                cursor=conn.execute("select * from records where username is ?",(name,))
                rows=cursor.fetchone()
                if not rows:
                    console.print(Text(f"User '{name}' not found", style="bold red"))
                    log_info("Attempted Deletion on Empty Database",level="WARNING")
                    return
                input_x=input("Is this the data you want to delete (Yes/No) :").lower()
                if input_x=="yes":
                    clear_proc()
                    try:
                        record_manager.delete_1(name)
                        console.print(Text(f"User '{name}' deleted successfully", style="green"))
                        log_info(f"User deleted: {name}", level="WARNING")
                        console.print(Text("Returning to main menu",style="yellow"))
                        return
                    except Exception as e:
                        console.print(Text("An error occurred", style="bold red"))
                        log_info(f"ERROR : {e}", level="CRITICAL")
                elif input_x=="no":
                    console.print(Text("Deletion cancelled, Returning to main menu",style="yellow"))
                    log_info(f"User deletion cancelled: {name}", level="INFO")
                    return
                else:
                    console.print(Text("Please enter a valid input, Returning to main menu",style="yellow"))
                    log_info(f"User not found during deletion {name}", level="ERROR")
                    return
            except Exception as e:
                console.print(Text("An Unknown Error Occurred", style="bold red"))
                log_info(f"ERROR : {e}", level="CRITICAL")