from logger import log_info
from storage import connect_db,initialise_db,get_db
class RecordManager():
    def __init__(self):
        conn=connect_db()
        initialise_db(conn)
        conn.close()
    def update_record(self,username,uid,last_saved):
        with get_db() as conn:
            conn.execute("""insert or replace into records values (?, ?, ?)""",
            (username,uid,last_saved))
            log_info(f"New record added: {username}", level="INFO")
    def display_id(self,uid):
        with get_db() as conn:
            cursor=conn.execute("select * from records where id=?",(uid,))
            row=cursor.fetchone()
            if row:
                print(f"User ID: {row['id']}")
    def delete_0(self):
        with get_db() as conn:
            cursor=conn.execute("delete from records")
    def delete_1(self,username):
        with get_db() as conn:
            cursor=conn.execute("delete from records where username =?",(username,))
            if cursor.rowcount==0:
                print("Username not found,Please Try Again")
                log_info(f"Delete failed, username not found: {username}", level="WARNING")
    def display_data(self):
        with get_db() as conn:
            cursor=conn.execute("select * from records")
            rows=cursor.fetchall()
            for row in rows:
                print(f"Username: {row['username']}  ID: {row['id']}  Last Saved: {row['last_saved']}")
            log_info(f"Total Record displayed", level="WARNING")
            if not rows:
                print("No records found")
    def display_user(self,username):
        with get_db() as conn:
            cursor=conn.execute("select * from records where username=?",(username,))
            row=cursor.fetchone()
            if row:
                print(f"Username: {row['username']}  ID: {row['id']}  Last Saved: {row['last_saved']}")
                log_info(f"Record displayed: {username}", level="WARNING")
            else:
                print("User not found")
                log_info("Record not displayed and found", level="CRITICAL")
    def delete_person(self):
        from operations import delete_person
        delete_person(self)
    def delete_data(self):
        from operations import delete_data
        delete_data(self)
    def search_func(self):
        from search import search_func
        search_func(self)
    def name_enter(self):
        from user_entry import name_enter as saving_entry
        saving_entry(self)