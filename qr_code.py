import qrcode
import uuid
import os
def qr_code(record_manager):
        username=input("Please enter your username to find in records and generate a Qr code :")
        if username in record_manager.records:
            user_records=record_manager.records
            details_0=record_manager.records[username]
            details_1=record_manager.records[username]["Name"]
            details_2=record_manager.records[username]["ID"]
            details_3=record_manager.records[username]["Last saved"]
            main_details=(f"Username : {details_0}\n Name : {details_1}\n ID : {details_2}\n Last saved : {details_3}")
            img=qrcode.make(main_details)
            unique_id=uuid.uuid4().hex
            file=(f"{unique_id}qr.png")
            img.save(file)
            try:
                img.show()
                input("Press enter to close the QR code and delete the file")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if os.path.exists(file):
                    os.remove(file)