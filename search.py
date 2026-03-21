from logger import log_info
from storage import get_db
from rich.console import Console
from rich.table import Table
from rich.text import Text
console=Console()
def combined_search()->None:
    with get_db() as conn:
        try:
            query=input("Search (Enter ID or Username):")
            row=conn.execute('select * from records where id is ?',(query,)).fetchone()
            if row:
                table = Table(title="Search Result")
                table.add_column("Username", style="cyan")
                table.add_column("ID", style="magenta")
                table.add_column("Last Saved", style="green")
                table.add_row(row['username'], row['id'], row['last_saved'])
                console.print(table)
                log_info(f"ID search successful: {query}", level="INFO")
                return
            cursor=conn.execute("select * from records where username= ?",(query,))
            row=cursor.fetchone()
            if row:
                table = Table(title="Search Result")
                table.add_column("Username", style="cyan")
                table.add_column("ID", style="magenta")
                table.add_column("Last Saved", style="green")
                table.add_row(row['username'], row['id'], row['last_saved'])
                console.print(table)
                log_info(f"Username search successful :{query}",level="INFO")
                return
            row=conn.execute("select * from records where username like ?",(f"%{query}%",)).fetchall()
            if row:
                table = Table(title=f"Found {len(row)} result(s)")
                table.add_column("No.", style="white")
                table.add_column("Username", style="cyan")
                for index, row in enumerate(row,start=1):
                    table.add_row(str(index), row['username'])
                console.print(table)
                result=input("Please type the username you want the details about from the list above :").lower().strip()
                cursor=conn.execute("select * from records where username = ?",(result,))
                result_row=cursor.fetchone()
                if result_row:
                    detail_table = Table(title="User Record")
                    detail_table.add_column("Username", style="cyan")
                    detail_table.add_column("ID", style="magenta")
                    detail_table.add_column("Last Saved", style="green")
                    detail_table.add_row(result_row['username'], result_row['id'], result_row['last_saved'])
                    console.print(detail_table)
                    log_info(f"Username search successful: {result}", level="INFO")
                    return
                else:
                    console.print(Text("Username Not Found",style="bold red"))
            else:
                console.print(Text(f"{query} not found", style="bold red"))
                log_info(f"Username not found {query}",level="WARNING")
                return
        except Exception as e:
            console.print(Text("An Unknown Error Occurred", style="bold red"))
            log_info(f"ERROR : {e}",level="CRITICAL")