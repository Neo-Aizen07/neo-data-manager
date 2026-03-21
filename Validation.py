from storage import get_db
from rich.console import Console
from rich.text import Text
console=Console()
def user_valid(username : str)->bool:
    with get_db() as conn:
        SPECIAL_CHAR="'!_-@#$%^&*()+=[]{}|;:,.<>?/`~"
        count=sum(1 for char in username if char in SPECIAL_CHAR)
        if username.lower()!=username:
            console.print(Text("Username must not contain any uppercase letters",style="bold red"))
            return False
        if len(username)<5 or len(username)>=20:
            console.print(Text("Invalid Number of Characters in username",style="bold red"))
            return False
        elif not username:
            console.print(Text("Invalid input, Username cannot be empty. Please try again.",style="bold red"))
            return False
        elif count>=4:
            console.print(Text("Invalid Input, Exceeds the number of Special Characters",style="bold red"))
            return False
        elif " " in username:
            console.print(Text("No spaces allowed in Username",style="bold red"))
            return False
        return True