from logger import log_info
from storage import connect_db,initialise_db,get_db
def search_func(record_manager):
    input_1=input("Do you want to search using ID or Username:").lower()
    if input_1=="id":
        search_id(record_manager)
    elif input_1=="username":
        user_in=input("Do you have the exact username('Enter 'username')or you want to search(Enter 'search') : ").lower().strip()
        if user_in=="username":
            search_username(record_manager)
        elif user_in=="search":
            par_search_username(record_manager)
        else:
            print("Please Enter A Valid Input")
            log_info(f"Invalid search type in search: {user_in}", level="WARNING")
            return
    else:
        print("Please enter a valid entry and try again")
        log_info(f"Invalid search type: {input_1}", level="WARNING")
        return
def search_id(record_manager):
    with get_db() as conn:
        try:
            enter_id=input("Please enter your ID to search :")
            cursor=conn.execute('select * from records where id is ?',(enter_id,))
            row=cursor.fetchone()
            if row:
                print(f"Username: {row['username']}  ID: {row['id']}  Last Saved: {row['last_saved']}")
                log_info(f"ID search successful: {enter_id}", level="INFO")
            else:
                print("ID not found, Try Again")
                log_info(f"ID search no results: {enter_id}", level="WARNING")
                return
        except Exception as e:
            print("An Unknown Error Occured")
            log_info(f"ERROR : {e}",level="CRITICAL")
def par_search_username(record_manager):
    with get_db() as conn:
        try:
            partial_input=input("Please enter your username to search :")
            cursor=conn.execute("select * from records where username like ?",(f"%{partial_input}%",))
            rows=cursor.fetchall()
            if rows:
                print(f"Found {len(rows)} result(s) :")
                for index, row in enumerate(rows,start=1):
                    print(f"{index}. {row['username']}")
                result=input("Please type the username you want the details about from the list above :").lower().strip()
                cursor=conn.execute("select * from records where username = ?",(result,))
                result_row=cursor.fetchone()
                if result_row:
                    print(f"Username: {result_row['username']}  ID: {result_row['id']}  Last Saved: {result_row['last_saved']}")
                    log_info(f"Username search successful: {result}", level="INFO")
            else:
                print("Username not found")
                log_info(f"Username not found for the search {partial_input}",level="WARNING")
                return
        except Exception as e:
            print(f"An Unexpected Error Occured")
            log_info(f"ERROR : {e}", level="ERROR")
def search_username(record_manager):
    with get_db() as conn: 
        try:
            input_1=input("Please Enter Your Username : ")
            cursor=conn.execute("select * from records where username= ?",(input_1,))
            row=cursor.fetchone()
            if row:
                print(f"Username: {row['username']}  ID: {row['id']}  Last Saved: {row['last_saved']}")
                log_info(f"Username search successful :{input_1}",level="INFO")
            else:
                print("Username not found")
                log_info(f"Username not found {input_1}",level="WARNING")
        except Exception as e:
            print("An Unknown Error Occured")
            log_info(f"ERROR : {e}",level="CRITICAL")