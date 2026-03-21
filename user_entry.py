from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from RecordManager import RecordManager
import os
from user_interface import time_save, generate_id
from logger import log_info
from Validation import user_valid
from rich.text import Text
from rich.console import Console
console=Console()
def name_enter(record_manager : 'RecordManager')->None:
    try:
        console.print(Text("NOTE : Username must contain min 5 and max 20 characters,only 4 Special Characters allowed",style="cyan"))
        username=input("Please enter a username :").strip()
        if not user_valid(username):
            log_info(f"Invalid username attempt: {username}", level="WARNING")
            return
        uid=generate_id()
        record_manager.update_record(username,uid,time_save())
        record_manager.display_id(uid)
        console.print(Text("Registration Successful!",style="green"))
        log_info(f"Registration successful: {username}", level="INFO")
        return
    except Exception as e:
        console.print(Text("An Unexpected Error Occured",style="bold red"))
        log_info(f"ERROR : {e}",level="CRITICAL")