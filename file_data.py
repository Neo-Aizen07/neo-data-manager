import os
from logger import log_info
def verify():
        try:
            print(os.getcwd())
            BASE_DIR=os.path.dirname(os.path.abspath(__file__))
            file_path=os.path.join(BASE_DIR,"neo_data.db")
            print("Running from", os.path.abspath(__file__))
            print("BASE_DIR", os.path.dirname(os.path.abspath(__file__)))
            print("Files Here", os.listdir(os.path.dirname(os.path.abspath(__file__))))
            print("File Path:", file_path)
            print("BASE_DIR", BASE_DIR)
            print("Trying to open",file_path)
            print("File Path Exists?", os.path.exists(file_path))
            for name in os.listdir(BASE_DIR):
                print("Items Found", repr(name))
        except Exception as e:
             print("An Unknown Error Occured")
             log_info(f"ERROR : {e}",level="CRITICAL")