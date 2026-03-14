from storage import connect_db,initialise_db,get_db
def user_valid(record_manager,username):
    with get_db() as conn:
        SPECIAL_CHAR="'!_-@#$%^&*()+=[]{}|;:,.<>?/`~"
        count=sum(1 for char in username if char in SPECIAL_CHAR)
        cursor=conn.execute("select * from records where username=?",(username,))
        row=cursor.fetchone()
        if row:
            print("Username Already Exists, Please Try Again")
            return False
        if username.lower()!=username:
            print("Username must not contain any uppercase letters")
            return False
        if len(username)<3 or len(username)>=20:
            print("Invalid Number of Characters in username")
            return False
        elif not username:
            print("Invalid input, Username cannot be empty. Please try again.")
            return False
        elif count>=4:
            print("Invaid Input, Exceeds the number of Special Characters")
            return False
        elif " " in username:
            print("No spaces allowed in Username")
            return False
        return True