import os
import json
def save_names(record_manager):
        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(BASE_DIR,"data.json")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        temp_path=os.path.join(BASE_DIR,"Data.temp")
        data_to_save=record_manager.records
        try:
            if os.path.exists(file_path):
                print("The data is stored locally on ", os.path.abspath(__file__))
                with open(temp_path,"w",encoding="utf-8") as f:
                    json.dump(data_to_save,f, indent=4, ensure_ascii=False)
                    print("Data saved successfully")
                os.replace(temp_path, file_path)
                print("Data file created successfully")
                return record_manager.records
            else:
                with open(file_path,"w",encoding="utf-8") as f:
                    json.dump({},f, indent=4, ensure_ascii=False)
                    print("data.json file created successfully")
                return record_manager.records
        except Exception as e:
            print(f"Error: {e}")
        except PermissionError as e:
            print(f" Error :Permission denied, {e}")
            return
        except json.JSONDecodeError as e:
            print(f"Error: failed encoding JSON, {e}")
            return
def file_load(record_manager,silent=False):
    try:
        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(BASE_DIR,"data.json")
        print("Data in :",(BASE_DIR))
        print("Trying to open :",os.path.abspath(file_path))
        print("Does the data exists in JSON :",os.path.exists(file_path))
        if os.path.exists(file_path):
            with open(file_path,"r") as f:
                records_dict=json.load(f)
                record_manager=records_dict
                return records_dict
        if os.path.exists(file_path):
            if not silent:
                print("\nData Loaded :")
                name=input("Please enter your username to search and provide the details :")
                if name in record_manager:
                    duplicate=record_manager[name]
                    print("Your username is :",name)
                    print("Your name is :",duplicate["Name"])
                    print("Your unique ID is :",duplicate["ID"])
                    print ("last saved time :",duplicate["Last saved"])
                    print("Your file has been opened successfully")
                    silent=True
                    return
            elif not os.path.exists(file_path):
                if not silent:
                    print("No data found, Please Try again after checking the files")
    except FileNotFoundError as e:
        if not silent:
            print(f"Error: File not found, {e}")
        return
    except json.JSONDecodeError as e:
        if not silent:
            print(f"Error: failed decoding JSON, {e}")
        return
    return records_dict