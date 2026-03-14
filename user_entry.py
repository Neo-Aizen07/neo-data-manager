import os
from user_interface import time_save, generate_id
from logger import log_info
from Validation import user_valid
def name_enter(record_manager):
    try:
        print("The data will be stores locally on ", os.path.abspath(__file__))
        print("NOTE : Usermane must contain 3 min characters and max 20 characters,only 4 Special Characters are allowed")
        username=input("Please enter a username :").strip()
        if not user_valid(record_manager,username):
            log_info(f"Invalid username attempt: {username}", level="WARNING")
            return
        uid=generate_id()
        record_manager.update_record(username,uid,time_save())
        record_manager.display_id(uid)
        print("Registration Successful!")
        log_info(f"Registration successful: {username}", level="INFO")
        return
    except Exception as e:
        print("An Unexpected Error Occured")
        log_info(f"ERROR : {e}",level="CRITICAL")