import time
import os
import datetime
import uuid
def time_save():
        time=datetime.datetime.now().isoformat(timespec="seconds")
        iso_time=str(time.replace("T","/"))
        return iso_time
def generate_id():
        id=uuid.uuid4().hex[:10]
        id_1=str(id)
        return id_1
def clear_menu():
        command=("cls"if os.name=="nt" else "clear")
        os.system(command)
        print("*" *50)
def show_intro():
        print(__file__)
        print("-"*50)
        print("WELCOME TO DATABASE MANAGEMENT SYSTEM (JSON Based)")
        print("Version v1.3")