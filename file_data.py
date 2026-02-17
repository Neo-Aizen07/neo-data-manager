import os
def verify():
        print(os.getcwd())
        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(BASE_DIR,"data.json")
        print("Running from", os.path.abspath(__file__))
        print("BASE_DIR", os.path.dirname(os.path.abspath(__file__)))
        print("Files Here", os.listdir(os.path.dirname(os.path.abspath(__file__))))
        print("File Path:", file_path)
        print("BASE_DIR", BASE_DIR)
        print("Trying to open",file_path)
        print("File Path Exists?", os.path.exists(file_path))
        for root,dirs,files in os.walk("C:\\"):
            if "data.json" in files:
                print("file exists at:", os.path.join(root,"data.json"))
                break
        for name in os.listdir(BASE_DIR):
            print("Items Found", repr(name))