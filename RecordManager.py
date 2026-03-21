from logger import log_info
from storage import connect_db,initialise_db,get_db
import sqlite3
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
console=Console()
class RecordManager():
    def __init__(self)->None:
        conn=connect_db()
        initialise_db(conn)
        conn.close()
    def update_record(self,username : str ,uid : str ,last_saved : str)->None:
        try:
            with get_db() as conn:
                conn.execute("""insert into records values (?, ?, ?)""",
                (username,uid,last_saved))
                log_info(f"New record added: {username}", level="INFO")
        except sqlite3.IntegrityError:
            console.print(Text("Username already exists, Please Try Again", style="bold red"))
            log_info(f"Duplicate username attempt : {username}", level="WARNING")
    def display_id(self,uid : str)->None:
        with get_db() as conn:
            cursor=conn.execute("select * from records where id=?",(uid,))
            row=cursor.fetchone()
            if row:
                console.print(Panel(f"Your ID: [bold cyan]{row['id']}[/bold cyan]", title="Registration"))
    def delete_0(self)->None:
        with get_db() as conn:
            conn.execute("delete from records")
    def delete_1(self,username : str)->None:
        with get_db() as conn:
            cursor=conn.execute("delete from records where username =?",(username,))
            if cursor.rowcount==0:
                console.print(Text("Username not found, Please Try Again", style="bold red"))
                log_info(f"Delete failed, username not found: {username}", level="WARNING")
    def display_data(self)->None:
        with get_db() as conn:
            cursor=conn.execute("select * from records")
            rows=cursor.fetchall()
            table = Table(title="All Records")
            table.add_column("Username", style="cyan")
            table.add_column("ID", style="magenta")
            table.add_column("Last Saved", style="green")
            for row in rows:
                table.add_row(row['username'], row['id'], row['last_saved'])
            console.print(table)
            log_info(f"Total Record displayed", level="WARNING")
            if not rows:
                console.print(Text("No records found", style="yellow"))
    def display_user(self,username : str)->None:
        with get_db() as conn:
            cursor=conn.execute("select * from records where username=?",(username,))
            row=cursor.fetchone()
            if row:
                content = f"Username: [cyan]{row['username']}[/cyan]\nID: [magenta]{row['id']}[/magenta]\nLast Saved: [green]{row['last_saved']}[/green]"
                console.print(Panel(content, title="User Record"))
                log_info(f"Record displayed: {username}", level="WARNING")
            else:
                console.print(Text("User not found", style="bold red"))
                log_info("Record not found for display", level="WARNING")
    def delete_person(self)->None:
        from operations import delete_person
        delete_person(self)
    def delete_data(self)->None:
        from operations import delete_data
        delete_data(self)
    def search_func(self)->None:
        from search import combined_search
        combined_search()
    def name_enter(self)->None:
        from user_entry import name_enter as saving_entry
        saving_entry(self)